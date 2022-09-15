from product import Product

class Inventory:
	'''
	Beskriv klassen
	'''
	def __init__(self) -> None:
		'''
		Sparar affärens produkter i en lista
		'''
		self.__products = []

	def get_products(self) -> list:
		'''
		returnerar listan av produkter
		'''
		return self.__products
		
	def add_product(self, p_number:int, p_name:str, p_price:int) -> None:
		'''
		Lägger till en produkt i inventariet
		'''
		new_product = Product(p_number, p_name, p_price)
		self.__products.append(new_product)

	def search_products(self, search_string:str) -> list:
		'''
		Låter användaren söka efter en produkt
		'''
		result = []
		for product in self.__products:
			if search_string in product.get_p_name():
				result.append(product)
		
		return result
	
	def remove_product(self, remove_id:int) -> bool:
		'''
		Låter användaren ta bort en produkt från affären
		'''
		for product in self.__products:
			if product.get_p_number() == remove_id:
				self.__products.remove(product)
				return True
		return False