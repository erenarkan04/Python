from ecommerce.sales import calc_shipping, calc_tax
from ecommerce import sales

sales.calc_tax()
sales.calc_shipping()

calc_tax()
calc_shipping()


print(dir(sales))
print(sales.__name__)
print(sales.__package__)
print(sales.__file__)

