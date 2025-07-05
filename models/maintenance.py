from odoo import models, fields

class AgroMaintenance(models.Model):
    _name = "agro.maintenance"
    _description = "Mantenimiento de Maquinaria"
    _order = "date desc"

    name = fields.Char(string="Referencia", required=True)
    date = fields.Date(string="Fecha", required=True, default=fields.Date.today)
    machinery_id = fields.Many2one(
        comodel_name="agro.machinery",
        string="Maquinaria",
        required=True,
        ondelete="cascade"
    )
    task_description = fields.Text(string="Tarea realizada")
    technician = fields.Char(string="Técnico responsable")
    cost = fields.Float(string="Costo", digits=(12, 2))
    parts_used = fields.Text(string="Repuestos utilizados")
    notes = fields.Text(string="Observaciones")
