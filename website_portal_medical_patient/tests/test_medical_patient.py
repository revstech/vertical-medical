# -*- coding: utf-8 -*-
# Copyright 2016-2017 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo.tests.common import TransactionCase


class TestMedicalPatient(TransactionCase):

    def setUp(self):
        super(TestMedicalPatient, self).setUp()
        self.patient_1 = self.env.ref(
            'medical.medical_patient_patient_1'
        )
        self.portal_user = self.env.ref(
            'portal.demo_user0'
        )
        self.Patient = self.env['medical.patient']

    def test_compute_website_url(self):
        """ Test website_url returns correct id """
        self.assertEquals(
            self.patient_1.website_url,
            '/medical/patient/%s' % self.patient_1.id,
        )

    def test_search_related_patients(self):
        """ It should return related patients """
        self.env.user.partner_id = self.portal_user.partner_id
        self.assertIn(
            self.patient_1,
            self.Patient.search_related_patients(),
        )
