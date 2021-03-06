# -*- coding: utf-8 -*-
##############################################################################
# Account move lines view
# Copyright (C) 2015 Moldeo (http://www.moldeo.coop)
# @author Gustavo Orrillo <gustavo.orrillo@moldeo.coop>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'acct_move_line_view',
    'version': '1.0.0',
    'category': 'Accounting',
    'sequence': 1,
    'author': "Moldeo",
    'summary': 'Account move lines view',
    'depends': [
        "account",
    ],
    'data': [
	'acct_move_line_view.xml'
    ],
    'demo': [
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
