from odoo import models, fields, api


class HopitalSpecialite(models.Model):
    _name = 'hopital.specialite'
    _rec_name = "name"
    name = fields.Char('name')
    medecin_ids = fields.Many2many(comodel_name='hopital.medecin',
                                     relation='sub_med_rel',
                                     column1='name',
                                     column2='f_name')
