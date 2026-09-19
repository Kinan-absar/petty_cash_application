{
    'name': 'Petty Cash Management - Employee Portal Bridge',
    'version': '18.0.1.1.0',
    'summary': 'Connects Petty Cash Management with Employee Portal Suite.',
    'description': """
Technical integration bridge between Petty Cash Management and Employee Portal Suite.

The two main applications remain independent. When both are available, this bridge
installs automatically and lets authorized employees submit and view petty cash reports
from the Employee Portal.
    """,
    'category': 'Accounting',
    'author': 'Kinan',
    'license': 'OPL-1',
    'application': False,
    'installable': True,
    'auto_install': True,
    'depends': [
        'petty_cash_management',
        'employee_portal_suite',
        'portal',
        'website',
    ],
    'data': [
        'views/layout_extension.xml',
        'views/portal_petty_cash_templates.xml',
    ],
}
