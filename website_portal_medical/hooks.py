# -*- coding: utf-8 -*-
# Copyright 2017 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

import logging

from odoo import api, SUPERUSER_ID


_logger = logging.getLogger(__name__)


def _update_patients_legal_rep(cr, registry):
    with cr.savepoint():
        env = api.Environment(cr, SUPERUSER_ID, {})
        patient_model = env['medical.patient']

        try:
            patients = patient_model.search([
                ('parent_id', '=', env.ref('base.partner_demo').id)
            ])
            patients.write(
                {'parent_id': env.ref('portal.demo_user0_res_partner').id}
            )
        except ValueError:
            _logger.debug(
                'Demo partner not found - skipping the fix for it.',
            )
