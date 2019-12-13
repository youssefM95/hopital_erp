from odoo import models, fields, api


class HopitalSaleOperatoire(models.Model):
    _name = 'hopital.saleoperatoire'
    _rec_name = "name"
    name = fields.Char('name')
    prix_heure_operation = fields.Float()
    operation_chirurgicale_ids = fields.Many2many(comodel_name='hopital.operationchirurgicale',
                                     relation='sale_prof_rel',
                                     column1='name',
                                     column2='o_name')