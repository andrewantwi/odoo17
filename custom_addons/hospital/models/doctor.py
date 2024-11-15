from odoo import api, fields, models

class Doctor(models.Model):
    _name = 'hospital.doctor'
    _inherit = ['mail.thread']
    _description = 'Doctor Model'

    name = fields.Char(string="Name", required=True, tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], tracking=True)
    specialty_id = fields.Many2one('hospital.specialty', string='Specialties', required=True, tracking=True,unique=True)
    contact_info = fields.Char(string='Contact Information')
    availability_ids = fields.One2many('hospital.doctor.availability', 'doctor_id', string='Availability')
    consultation_ids = fields.One2many('hospital.consultation', 'doctor_id', string='Consultations')
    appointment_ids = fields.One2many('hospital.appointment', 'doctor_id', string="Appointments")

class Specialty(models.Model):
    _name = 'hospital.specialty'
    _description = 'Medical Specialty'

    name = fields.Char(string='Specialty Name', required=True)
    description = fields.Text(string='Description')
    doctor_ids = fields.One2many('hospital.doctor', 'specialty_id',string='Doctors')

class DoctorAvailability(models.Model):
    _name = 'hospital.doctor.availability'
    _description = 'Doctor Availability'

    doctor_id = fields.Many2one('hospital.doctor', string='Doctor', required=True)
    shift_type = fields.Selection([
        ('morning', 'Morning'),
        ('afternoon', 'Afternoon'),
        ('evening', 'Evening')
    ], string='Shift Type', required=True)
    date = fields.Date(string='Date', required=True)
    start_time = fields.Float(string='Start Time', required=True, help="Starting time of the shift in 24-hour format (e.g., 8.5 for 08:30 AM)")
    end_time = fields.Float(string='End Time', required=True, help="Ending time of the shift in 24-hour format (e.g., 17.5 for 5:30 PM)")
    is_available = fields.Boolean(string='Available', default=True)

class Consultation(models.Model):
    _name = 'hospital.consultation'
    _description = 'Consultation Record'

    doctor_id = fields.Many2one('hospital.doctor', string='Doctor', required=True)
    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    consultation_date = fields.Datetime(string='Consultation Date', required=True)
    notes = fields.Text(string='Consultation Notes')
    diagnosis = fields.Text(string='Diagnosis')
    treatment = fields.Text(string='Prescribed Treatment')
    follow_up_date = fields.Date(string='Follow-up Date')

