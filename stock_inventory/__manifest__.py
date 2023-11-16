{
    "name": "Stock Inventory Adjustment",
    "version": "15.0.1.1.0",
    "license": "LGPL-3",
    "maintainer": ["DavidJForgeFlow"],
    "development_status": "Beta",
    "category": "Inventory/Inventory",
    "summary": "Allows to do an easier follow up of the Inventory Adjustments",
    "author": "ForgeFlow, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/stock-logistics-warehouse",
    "depends": ["stock"],
    "data": [
        "security/ir.model.access.csv",
        "views/stock_inventory.xml",
        "views/stock_quant.xml",
        "views/stock_move_line.xml",
    ],
    "installable": True,
    "application": False,
}
