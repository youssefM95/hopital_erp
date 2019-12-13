from odoo import models, api, fields


class HopitalChambre(models.Model):
    _name = 'hopital.chambre'
    _rec_name = "name"
    name = fields.Char('name')
    prix_jour = fields.Float()
