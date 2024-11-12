from odoo import api, fields, models


class Doctor(models.Model):
    _name = 'hospital.doctor'
    _inherit = ['mail.thread']
    _description = 'Doctor Model'

    name = fields.Char(string="Name", required=True, tracking=True)
    date_of_birth = fields.Date(string='DOB', tracking=True)
    gender = fields.Selection([('Male', 'male'), ('Female', 'female')], tracking=True)
    specialty = fields.Char(string="Specialty", required=True, tracking=True)
    patient_ids = fields.One2many('hospital.patient', 'doctor_id', string="Patients", tracking=True)
    appointment_ids = fields.One2many('hospital.appointment', 'doctor_id', string="Appointments", tracking=True)
    shift = fields.Selection([('Morning', 'morning'), ('Afternoon', 'afternoon'), ('Evening', 'evening')])
