# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.tests.common import TransactionCase
from openerp import api, fields, models
from openerp.exceptions import ValidationError


class MedicalNpiAbstractTestMixer(TransactionCase):

    def setUp(self, model_name='medical.abstract.npi'):
        super(MedicalNpiAbstractTestMixer, self).setUp()
        self.model_obj = self.env[model_name]
        self.valid = [
            1538596788,
            1659779064,
        ]
        self.invalid = [
            1659779062,
            1538696788,
            4949558680,
        ]
        self.country_us = self.env['res.country'].search([
            ('code', '=', 'US'),
        ],
            limit=1,
        )


class TestMedicalNpiAbstract(MedicalNpiAbstractTestMixer):

    def test_valid_int(self):
        """ Test _npi_is_valid returns True if valid int input """
        for i in self.valid:
            self.assertTrue(
                self.model_obj._npi_is_valid(i),
                'Npi validity check on int %s did not pass for valid' % i,
            )

    def test_valid_str(self):
        """ Test _npi_is_valid returns True if valid str input """
        for i in self.valid:
            self.assertTrue(
                self.model_obj._npi_is_valid(str(i)),
                'Npi validity check on str %s did not pass for valid' % i,
            )

    def test_invalid_int(self):
        """ Test _npi_is_valid returns False if invalid int input """
        for i in self.invalid:
            self.assertFalse(
                self.model_obj._npi_is_valid(i),
                'Npi validity check on int %s did not fail for invalid' % i,
            )

    def test_invalid_str(self):
        """ Test _npi_is_valid returns False if invalid str input """
        for i in self.invalid:
            self.assertFalse(
                self.model_obj._npi_is_valid(str(i)),
                'Npi validity check on str %s did not fail for invalid' % i,
            )

    def test_false(self):
        """ Test _npi_is_valid fails greacefully if given no/Falsey input """
        self.assertFalse(
            self.model_obj._npi_is_valid(False),
            'Npi validity check on False did not fail gracefully',
        )
