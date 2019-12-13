from odoo import models, fields


class HopitalPatient(models.Model):
    _name = 'hopital.patient'
    _rec_name = "f_name"
    f_name = fields.Char('first name')
    l_name = fields.Char('last name')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')])
    identity_card = fields.Char('Identity card')
    address = fields.Text('Address')
    birthday = fields.Date('Birthday')
    situation_familliale = fields.Selection([('célibataire','célibataire'),('mariée','Mariée'),('divorcé(e)','Divorcé(e)'),('veuf(ve)','Veuf(ve)')])
    email = fields.Char()
    phone = fields.Char()
    operation_ids = fields.Many2many(comodel_name='hopital.operationchirurgicale', relation='pat_op_rel',
                                     column1='f_name',
                                     column2='o_name')