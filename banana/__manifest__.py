{
    "name": "Banana",
    "version": "13.0.1.0.0",
    "category": "General",
    "summary": "This module shows different security strategies in Odoo.",
    "author": "Sunflower IT",
    "website": "https://sunflowerweb.nl",
    "depends": ["base","mail"],
    "data": [
        "security/res_groups.xml",
        "security/ir.model.access.csv",
        "security/ir_rule_banana.xml",
        "security/ir_rule_tribe.xml",
        "views/banana.xml",
        "views/monkey_tribe.xml",
        "views/other_menus.xml",
    ],
    "installable": True,
}
