# -*- coding: utf-8 -*-
# Copyright 2016-2017 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests.common import TransactionCase


class MedicalLuhnAbstractTestMixer(TransactionCase):

    def setUp(self):
        super(MedicalLuhnAbstractTestMixer, self).setUp()
        self.model_obj = self.env['medical.abstract.luhn']
        self.valid = [
            4532015112830366,
            6011514433546201,
            6771549495586802,
        ]
        self.invalid = [
            4531015112830366,
            6011514438546201,
            1771549495586802,
        ]
        self.country_us = self.env['res.country'].search([
            ('code', '=', 'US'),
        ],
            limit=1,
        )


class TestMedicalLuhnAbstract(MedicalLuhnAbstractTestMixer):

    def test_valid_int(self):
        """ Test _luhn_is_valid returns True if valid int input """
        for i in self.valid:
            self.assertTrue(
                self.model_obj._luhn_is_valid(i),
                'Luhn validity check on int %s did not pass for valid' % i,
            )

    def test_valid_str(self):
        """ Test _luhn_is_valid returns True if valid str input """
        for i in self.valid:
            self.assertTrue(
                self.model_obj._luhn_is_valid(str(i)),
                'Luhn validity check on str %s did not pass for valid' % i,
            )

    def test_invalid_int(self):
        """ Test _luhn_is_valid returns False if invalid int input """
        for i in self.invalid:
            self.assertFalse(
                self.model_obj._luhn_is_valid(i),
                'Luhn validity check on int %s did not fail for invalid' % i,
            )

    def test_invalid_str(self):
        """ Test _luhn_is_valid returns False if invalid str input """
        for i in self.invalid:
            self.assertFalse(
                self.model_obj._luhn_is_valid(str(i)),
                'Luhn validity check on str %s did not fail for invalid' % i,
            )

    def test_false(self):
        """ Test _luhn_is_valid fails greacefully if given no/Falsey input """
        self.assertFalse(
            self.model_obj._luhn_is_valid(False),
            'Luhn validity check on False did not fail gracefully',
        )
