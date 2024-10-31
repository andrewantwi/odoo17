from odoo import api, fields, models


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _inherit = ['mail.thread']
    _description = 'Patient Appointments'
    _rec_name = 'patient_id'

    reference = fields.Char(string='Reference', default='New')
    patient_id = fields.Many2one('hospital.patient', string='Patient')
    date_appointment = fields.Date(string='Appointments')
    note = fields.Text(string='Note')
    state = fields.Selection([('draft', 'Draft'), ('confirmed', 'Confirmed'),
                              ('ongoing', 'Ongoing'), ('done', 'Done'), ('canceled', 'Canceled')
                              ], default='draft')

    # Replacing the reference with a sequence generated number
    @api.model_create_multi
    def create(self, vals_list):
        print("odoo mates", vals_list)
        for vals in vals_list:
            if not vals.get('reference') or vals['reference'] == 'New':
                vals['reference'] = self.env['ir.sequence'].next_by_code('hospital.appointment')
        return super().create(vals_list)
