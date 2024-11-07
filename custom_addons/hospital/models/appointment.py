from odoo import api, fields, models
# from odoo.api import ondelete


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _inherit = ['mail.thread']
    _description = 'Patient Appointments'
    _rec_name = 'patient_id'
    _rec_names_search = ['patient_id', 'reference']

    reference = fields.Char(string='Reference', default='New')
    patient_id = fields.Many2one('hospital.patient', string='Patient',ondelete='restrict')
    date_appointment = fields.Date(string='Date')
    note = fields.Text(string='Note')
    state = fields.Selection([('draft', 'Draft'), ('confirmed', 'Confirmed'),
                              ('ongoing', 'Ongoing'), ('done', 'Done'), ('canceled', 'Canceled')
                              ], default='draft', tracking=True)
    appointment_line_ids = fields.One2many('hospital.appointment.line', 'appointment_id', string='Lines')
    total_qty = fields.Float(compute='_compute_total_qty', string='Total Quantity', store=True)
    date_of_birth = fields.Date(related='patient_id.date_of_birth')

    @api.depends('appointment_line_ids','appointment_line_ids.qty')
    def _compute_total_qty(self):
        for rec in self:
            rec.total_qty = sum(rec.appointment_line_ids.mapped('qty'))


    # Replacing the reference with a sequence generated number
    @api.model_create_multi
    def create(self, vals_list):
        print("odoo mates", vals_list)
        for vals in vals_list:
            if not vals.get('reference') or vals['reference'] == 'New':
                vals['reference'] = self.env['ir.sequence'].next_by_code('hospital.appointment')
        return super().create(vals_list)

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirmed'

    def action_ongoing(self):
        for rec in self:
            rec.state = 'ongoing'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def action_cancel(self):
        for rec in self:
            rec.state = 'canceled'

    def _compute_display_name(self):
        for rec in self:
            rec.display_name = f"[{rec.reference}]" f"[{rec.patient_id.name}]"


class HospitalAppointmentLine(models.Model):
    _name = 'hospital.appointment.line'
    _description = 'hospital appointment line'

    appointment_id = fields.Many2one('hospital.appointment', string='Appointment')
    product_id = fields.Many2one('product.product', string='Product', required=True)
    qty = fields.Float(string='Quantity')
