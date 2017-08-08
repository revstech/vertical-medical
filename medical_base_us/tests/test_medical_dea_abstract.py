# -*- coding: utf-8 -*-
# Copyright 2016-2017 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests.common import TransactionCase


class MedicalDeaAbstractTestMixer(TransactionCase):

    def setUp(self):
        super(MedicalDeaAbstractTestMixer, self).setUp()
        self.model_obj = self.env['medical.abstract.dea']
        self.valid = [
            'AP5836727',
        ]
        self.invalid = [
            'AP5836729',
            'Invalid00',
        ]
        self.country_us = self.env['res.country'].search([
            ('code', '=', 'US'),
        ],
            limit=1,
        )


class TestMedicalDeaAbstract(MedicalDeaAbstractTestMixer):

    def test_valid(self):
        """ Test _dea_is_valid returns True if valid str input """
        for i in self.valid:
            self.assertTrue(
                self.model_obj._dea_is_valid(i),
                'DEA validity check on str %s did not pass for valid' % i,
            )

    def test_invalid(self):
        """ Test _dea_is_valid returns False if invalid str input """
        for i in self.invalid:
            self.assertFalse(
                self.model_obj._dea_is_valid(i),
                'DEA validity check on str %s did not fail for invalid' % i,
            )

    def test_false(self):
        """ Test _dea_is_valid fails gracefully if given no/Falsey data """
        self.assertFalse(
            self.model_obj._dea_is_valid(False),
            'DEA validity check on False did not fail gracefully',
        )
