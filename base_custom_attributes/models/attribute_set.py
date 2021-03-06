# -*- encoding: utf-8 -*-
###############################################################################
#                                                                             #
#   base_attribute.attributes for OpenERP                                     #
#   Copyright (C) 2015 Odoo Community Association (OCA)                       #
#                                                                             #
#   This program is free software: you can redistribute it and/or modify      #
#   it under the terms of the GNU Affero General Public License as            #
#   published by the Free Software Foundation, either version 3 of the        #
#   License, or (at your option) any later version.                           #
#                                                                             #
#   This program is distributed in the hope that it will be useful,           #
#   but WITHOUT ANY WARRANTY; without even the implied warranty of            #
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             #
#   GNU Affero General Public License for more details.                       #
#                                                                             #
#   You should have received a copy of the GNU Affero General Public License  #
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.     #
#                                                                             #
###############################################################################

from openerp import models, fields, api


class AttributeSet(models.Model):
    _name = "attribute.set"
    _description = "Attribute Set"

    @api.multi
    def _get_default_model(self):
        if 'force_model' in self.env.context and \
                self.env.context.get('force_model'):
            models = self.env['ir.model'].search([
                ('model', '=', self.env.context.get('force_model'))])
            if models:
                return models[0]
        return False

    name = fields.Char(
        'Name',
        required=True,
        translate=True,
    )

    attribute_group_ids = fields.One2many(
        'attribute.group',
        'attribute_set_id',
        'Attribute Groups',
    )

    model_id = fields.Many2one(
        'ir.model',
        'Model',
        required=True,
        default=_get_default_model,
    )
