from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Patient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread']
    _description = 'Patient'

    name = fields.Char(string="Name", required=True, tracking=True)
    date_of_birth = fields.Date(string='DOB', tracking=True)
    gender = fields.Selection([('Male', 'male'), ('Female', 'female')], tracking=True)
    tag_ids = fields.Many2many('patient.tag', 'patient_tag_rel', 'patient_tag_id', 'tag_id', string="Tags")
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor')  # Inverse field for Doctor model
    symptoms = fields.Char(string='Symptoms')
    medication = fields.Char(string='Medication')


    # function that runs when you try to delete a record in this model
    def unlink(self):
        for rec in self:
            print('This function is running', rec.name)
            domain = [('patient_id', '=', rec.id)]
            appointments = self.env['hospital.appointment'].search(domain)
            if appointments:
                # UserError can also be used instead of ValidationError
                raise ValidationError(
                    'You cannot delete the patients now,\n Appointments exist for patient:%s' % rec.name)
        return super().unlink()

# Different way of running a function when something is deleted

# @api.ondelete(at_uninstall=False)
# def _check_patient_appointments(self):
#     for rec in self:
#         print('This function is running', rec.name)
#         domain = [('patient_id', '=', rec.id)]
#         appointments = self.env['hospital.appointment'].search(domain)
#         if appointments:
#             # UserError can also be used instead of ValidationError
#             raise ValidationError('You cannot delete the patients now,\n Appointments exist for patient:%s' % rec.name)
#
