# Copyright 2019 Tecnativa - Sergio Teruel
# Copyright 2023 Tecnativa - Pedro M. Baeza
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import fields, models


class StockPickingType(models.Model):
    _inherit = "stock.picking.type"

    show_move_onhand = fields.Boolean(
        string="Show Move On hand stock",
        help="Show a button 'Move On Hand' in the Inventory Dashboard "
        "to initiate the process to move the products in stock "
        "at the origin location.",
    )

    def action_move_location(self):
        action = self.env["ir.actions.act_window"]._for_xml_id(
            "stock_move_location.wiz_stock_move_location_action"
        )
        action["context"] = {
            "default_origin_location_id": self.default_location_src_id.id,
            "default_destination_location_id": self.default_location_dest_id.id,
            "default_picking_type_id": self.id,
            "default_edit_locations": False,
        }
        return action
