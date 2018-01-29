# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import http
from odoo.http import request

from odoo.addons.website_portal_medical.controllers.main import (
    WebsiteMedical
)


class WebsiteMedical(WebsiteMedical):

    @http.route(
        ['/my/medical', '/medical'],
        type='http',
        auth="user",
        website=True,
    )
    def my_medical(self):
        response = super(WebsiteMedical, self).my_medical()
        patients = request.env['medical.patient'].search_related_patients()
        response.qcontext.update({
            'patients': patients,
        })
        return response

    @http.route(
        ['/medical/patients'],
        type='http',
        auth="user",
        website=True,
    )
    def medical_patients(self):
        patients = request.env['medical.patient'].search_related_patients()
        values = {
            'patients': patients,
            'user': request.env.user,
        }
        return request.render(
            'website_portal_medical_patient.medical_my_patients', values,
        )

    def _inject_medical_detail_vals(self, patient=None, **kwargs):
        vals = super(WebsiteMedical, self)._inject_medical_detail_vals()
        countries = request.env['res.country'].sudo().search([])
        states = request.env['res.country.state'].sudo().search([])

        if not patient:
            patient = request.env['medical.patient'].browse()

        kgm_categ = request.env.ref('product.product_uom_categ_kgm')
        product_uoms = request.env['product.uom'].search([
            ('category_id', '=', kgm_categ.id)
        ])

        if len(patient):
            partner_id = patient.partner_id
        else:
            partner_id = request.env.user.partner_id
        vals.update({
            'countries': countries,
            'states': states,
            'patient': patient,
            'patient_website_attr': 'website_url',
            'partner': partner_id,
            'weight_uoms': product_uoms,
        })
        return vals

    @http.route(
        ['/medical/patient/<int:patient_id>'],
        type='http',
        auth='user',
        website=True,
        methods=['GET'],
    )
    def patient(self, patient_id, redirect=None, **kwargs):
        values = {
            'error': {},
            'error_message': [],
            'success_page': kwargs.get('success_page', '/medical/patients')
        }
        patient = request.env['medical.patient'].browse(patient_id)

        if not patient:
            return request.render('website.404')

        values.update(
            self._inject_medical_detail_vals(patient)
        )
        return request.render(
            'website_portal_medical_patient.patient', values,
        )

    @http.route(
        ['/medical/patient'],
        type='http',
        auth='user',
        website=True,
        methods=['GET'],
    )
    def new_patient(self, redirect=None, **kwargs):
        values = {
            'error': {},
            'error_message': [],
            'success_page': kwargs.get('success_page', '/medical/patients')
        }
        values.update(
            self._inject_medical_detail_vals()
        )
        return request.render(
            'website_portal_medical_patient.patient', values,
        )
