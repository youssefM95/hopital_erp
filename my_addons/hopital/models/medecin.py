# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HopitalMedecin(models.Model):
    _name = 'hopital.medecin'
    _rec_name = "f_name"
    f_name = fields.Char('first name')
    l_name = fields.Char('last name')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')])
    date_entre = fields.Date('start date')
    prix_heure_operation = fields.Float()
    phone = fields.Char()
    operation_ids = fields.Many2many(comodel_name='hopital.operationchirurgicale', relation='med_op_rel',
                                     column1='f_name',
                                     column2='o_name')
    specialite_id = fields.Many2one(comodel_name='hopital.specialite')
    sejours_ids = fields.One2many(comodel_name='hopital.sejourmaladie', inverse_name='medecin_id')

    prix_op = fields.Integer(String='Price Of Operations', compute='prix_operation')

    def prix_operation(self):
        for operation in self.operation_ids:
            self.prix_op += operation.nombre_heures * self.prix_heure_operation
