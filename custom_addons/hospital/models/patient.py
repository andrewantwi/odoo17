from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Patient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread']
    _description = 'Patient'

    # Core Fields
    name = fields.Char(
        string="Name",
        required=True,
        tracking=True,
        help="The full name of the patient."
    )
    date_of_birth = fields.Date(
        string='Date of Birth',
        tracking=True,
        help="The patient's date of birth."
    )
    gender = fields.Selection(
        [('Male', 'Male'), ('Female', 'Female')],
        tracking=True,
        help="The patient's gender."
    )
    contact_info = fields.Char(
        string='Contact Information',
        tracking=True,
        help="The patient's phone number or email address."
    )

    # Tagging and Relationships
    tag_ids = fields.Many2many(
        'patient.tag',
        'patient_tag_rel',
        'patient_tag_id',
        'tag_id',
        string="Tags",
        help="Tags to classify patients (e.g., VIP, Chronic)."
    )
    consultation_ids = fields.One2many(
        'hospital.consultation',
        'patient_id',
        string='Consultations',
        help="List of consultations associated with the patient."
    )

    # State for Kanban View
    kanban_state = fields.Selection(
        [('normal', 'Normal'), ('blocked', 'Blocked')],
        default='normal',
        string="Kanban State",
        help="Use this field to visually track patient status in Kanban view."
    )

    # Override Unlink Method
    def unlink(self):
        for rec in self:
            print('This function is running', rec.name)
            domain = [('patient_id', '=', rec.id)]
            appointments = self.env['hospital.appointment'].search(domain)
            if appointments:
                raise ValidationError(
                    'You cannot delete the patient "%s" because appointments exist.' % rec.name
                )
        return super().unlink()

    # Validation on Deletion (Alternative Method)
    # @api.ondelete(at_uninstall=False)
    # def _check_patient_appointments(self):
    #     for rec in self:
    #         print('This function is running', rec.name)
    #         domain = [('patient_id', '=', rec.id)]
    #         appointments = self.env['hospital.appointment'].search(domain)
    #         if appointments:
    #             raise ValidationError(
    #                 'You cannot delete the patient "%s" because appointments exist.' % rec.name
    #             )


class PatientHistory(models.Model):
    _name = 'hospital.patient.history'
    _description = 'Patient History'

    patient_id = fields.Many2one(
        'hospital.patient',
        string='Patient',
        required=True,
        help="The patient this history record belongs to."
    )
