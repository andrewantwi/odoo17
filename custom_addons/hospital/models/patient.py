from odoo import api, fields, models


class Hospital(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread']
    _description = 'Patient Master'

    name = fields.Char(string="Name", required=True, tracking=True)
    date_of_birth = fields.Date(string='DOB', tracking=True)
    gender = fields.Selection([('Male', 'male'), ('Female', 'female')], tracking=True)
    tag_ids = fields.Many2many('patient.tag', 'patient_tag_rel', 'patient_tag_id',
                               'tag_id', string="Tags")
