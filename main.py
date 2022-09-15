from itertools import product
from inventory import Inventory

inventory = Inventory()
inventory.add_product(1234, "telefon", 12999)
inventory.search_product()
inventory.remove_product()