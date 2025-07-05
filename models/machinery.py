from odoo import models, fields

class AgroMachinery(models.Model):
    _name = "agro.machinery"
    _description = "Maquinaria Agrícola"

    name = fields.Char(string="Nombre", required=True)
    machinery_type = fields.Selection([
        ('tractor', 'Tractor'),
        ('harvester', 'Cosechadora'),
        ('seeder', 'Sembradora'),
        ('sprayer', 'Fumigadora'),
        ('other', 'Otro')
    ], string="Tipo de maquinaria", required=True)
    purchase_date = fields.Date(string="Fecha de compra")
    value = fields.Float(string="Valor estimado")
    state = fields.Selection([
        ('active', 'En uso'),
        ('maintenance', 'En mantenimiento'),
        ('retired', 'Retirada')
    ], string="Estado", default='active')
    employee_id = fields.Many2one('hr.employee', string="Responsable")
    maintenance_ids = fields.One2many('agro.maintenance', 'machinery_id', string="Mantenimientos")
