# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields


class MedicalMedicamentControl(models.Model):
    _name = 'medical.medicament.control'
    _description = 'Medical Medicament Control'

    name = fields.Char(
        string='Code',
        required=True,
    )

