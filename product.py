class Product:
	'''
	
	'''
	def __init__(self, p_number:int, p_name:str, p_price:int) -> None:
		self.__p_number = p_number
		self.__p_name = p_name
		self.__p_price = p_price

	def get_p_number(self) -> int:
		return self.__p_number

	def get_p_name(self) -> str:
		return self.__p_name

	def get_p_price(self) -> int:
		return self.__p_price

	def __str__(self) -> str:
		# --> Produktnummer, produktnamn, produktpris
		return f'Produktnummer: {self.__p_number} \nProduktnamn: {self.__p_name} \nProduktpris: {self.__p_price}'