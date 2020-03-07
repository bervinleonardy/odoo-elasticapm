# -*- coding: utf-8 -*-
#!/usr/bin/env python
# Copyright 2019 Akretion (http://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

try:
    from odoo.cli import main
except ImportError:
    # Odoo 8.0
    from odoo import main

if __name__ == "__main__":
    main()
