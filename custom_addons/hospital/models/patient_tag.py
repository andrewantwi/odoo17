from odoo import api, fields, models


class PatientTag(models.Model):
    _name = 'patient.tag'
    _description = 'Patient Tag'

    name = fields.Char(string="Name", required=True)

    sequence = fields.Integer("Sequence", default=10)




