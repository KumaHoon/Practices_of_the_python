# receipt.py

from sales_tax import add_sales_tax

def print_receipt():
    total = ...
    state = ...
    print(f'TOTAL : {total}')
    print(f'AFTER TAX : {add_sales_tax(total,state)}')


