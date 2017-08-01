# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import fields, http
from odoo.http import request

from odoo.addons.website_portal_medical_patient.controllers.main import (
    WebsiteMedical
)


class WebsiteMedical(WebsiteMedical):

    @http.route(
        ['/my/medical', '/medical'],
        type='http',
        auth="user",
        website=True,
    )
    def my_medical(self, **kw):
        """ Add insurances to medical account page """
        response = super(WebsiteMedical, self).my_medical()

        patients = response.qcontext['patients']
        date_now = fields.Date.today()
        insurance_plans = patients.mapped('insurance_plan_ids').sorted(
            lambda r: r.insurance_template_id.sudo().insurance_company_id.name,
        )
        active_plans = insurance_plans.filtered(
            lambda r: not r.member_exp or r.member_exp > date_now
        )

        response.qcontext.update({
            'insurance_plans': active_plans.sudo(),
        })
        return response

    @http.route(
        ['/medical/insurance/plan/<int:plan_id>'],
        type='http',
        auth='user',
        website=True,
        methods=['GET'],
    )
    def insurance_plan_show(self, plan_id=None, redirect=None, **kwargs):
        values = {
            'error': {},
            'error_message': [],
            'success_page': kwargs.get('success_page', '/my/medical')
        }
        Plans = http.request.env['medical.insurance.plan']
        if plan_id:
            plan = Plans.browse(plan_id)
        else:
            plan = Plans.browse()
        values.update({
            'insurance_plan': plan and plan.sudo(),
        })
        return request.render(
            'website_portal_medical_insurance_us.insurance_plan', values,
        )
