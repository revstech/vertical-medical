# -*- coding: utf-8 -*-
# Copyright 2017 LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl)

from odoo.tests import HttpCase


class TestUi(HttpCase):

    def test_subtotals(self):
        tour_module = 'odoo.__DEBUG__.services["web_tour.tour"]'
        self.phantom_js(
            url_path='/my/medical',
            code='%s.run("website_portal_medical_insurance_us")' % tour_module,
            ready='%s.tours.website_portal_medical_insurance_us.ready' % tour_module,
            login='portal',
        )
