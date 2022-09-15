from inventory import inventory

class Shop:
	'''
	Beskriv klassen
	'''
	def __init__(self) -> None:
		self.inventory = inventory
		
	def print_shop_menu(self) -> str:
		print("-"*20)
		print("Hej och välkommen till en affär!")
		print("1) Visa inventarie")
		print("2) Produktmeny")
		print("3) Avsluta")
		user_choice = input("Vänligen välj ett alternativ: ")

		if user_choice == 1:
			pass

Shop.print_shop_menu()
