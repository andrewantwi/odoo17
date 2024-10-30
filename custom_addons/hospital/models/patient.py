from odoo import api, fields, models


class Hospital(models.Model):
    _name = 'hospital.patient'
    _description = 'Patient Master'

    name = fields.Char(string="Name", required=True)
    date_of_birth = fields.Date(string='DOB')
    gender = fields.Selection([('Male', 'male'),('Female', 'female')])


