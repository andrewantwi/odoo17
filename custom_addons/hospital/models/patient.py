from odoo import api, fields, models
from odoo.exceptions import ValidationError

class Hospital(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread']
    _description = 'Patient Master'


    name = fields.Char(string="Name", required=True, tracking=True)
    date_of_birth = fields.Date(string='DOB', tracking=True)
    gender = fields.Selection([('Male', 'male'), ('Female', 'female')], tracking=True)
    tag_ids = fields.Many2many('patient.tag', 'patient_tag_rel', 'patient_tag_id',
                               'tag_id', string="Tags")


# function that runs when you try to delete a record in this model
    def unlink(self):
        for rec in self:
            print('This function is running',rec.name)
            domain = [('patient_id', '=', rec.id)]
            appointments = self.env['hospital.appointment'].search(domain)
            if appointments:
                raise ValidationError('You cannot delete the patients now,\n Appointments exist for patient:%s' %rec.name)
        return super().unlink()
