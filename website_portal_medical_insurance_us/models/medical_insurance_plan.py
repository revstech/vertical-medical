# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import api, fields, models


class MedicalInsurancePlan(models.Model):

    _name = 'medical.insurance.plan'
    _inherit = ['medical.insurance.plan',
                'website.published.mixin',
                'mail.thread',
                ]

    @api.multi
    def action_invalidate(self):
        return self.write({'member_exp': fields.Date.today()})

    @api.multi
    def _compute_website_url(self):
        for record in self:
            record.website_url = "/medical/insurance/plan/%d" % (record.id)
