# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HopitalSejourMaladie(models.Model):
    _name = 'hopital.sejourmaladie'
    nombre_jour = fields.Integer('nombre jour')
    date_debut = fields.Date('date debut')
    chambre_id = fields.Many2one(comodel_name='hopital.chambre')
    patient_id = fields.Many2one(comodel_name='hopital.patient')
    medecin_id = fields.Many2one(comodel_name='hopital.medecin')