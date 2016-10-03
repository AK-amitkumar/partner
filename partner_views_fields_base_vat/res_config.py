# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in module root
# directory
##############################################################################
from openerp import fields, models
from openerp.tools.translate import _

class partner_configuration(models.TransientModel):
    _inherit = 'base.config.settings'


    group_vat = fields.Boolean("Show VAT On Partners Tree View"
            implied_group='partner_views_fields_base_vat.group_vat',),


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
