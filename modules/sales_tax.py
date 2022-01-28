# sales_tax.py

#global namespace of this module
TAX_RATES_BY_STATE = {
    'MI' : 1.06,
    # ...
}


def add_sales_tax(total, state):
    tax_rate = total * TAX_RATES_BY_STATE[state] # tax_rate : local var
    return total * tax_rate