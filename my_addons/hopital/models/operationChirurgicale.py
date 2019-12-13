from odoo import models, fields, api


class HopitalOperationChirurgicale(models.Model):
    _name = 'hopital.operationchirurgicale'
    o_name = fields.Char(String='o_name')
    nombre_heures = fields.Integer('nombre heures')
    date_operation = fields.Date('date operation')

    med_ids = fields.Many2many(comodel_name='hopital.medecin', relation='op_med_rel', column1='o_name',
                                     column2='f_name')
    patient_ids = fields.Many2many(comodel_name='hopital.patient', relation='op_pat_rel', column1='o_name',
                               column2='f_name')
    sale_operation_id = fields.Many2one(comodel_name='hopital.saleoperatoire')