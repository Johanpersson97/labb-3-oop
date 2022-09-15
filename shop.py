from inventory import Inventory

class Shop:
	'''
	Klassen shop fungerar som en affär som består av ett inventory som i sin tur innehåller produkter
	'''

	def __init__(self) -> None:
		'''
		Skapar ett inventory (klass) som kallas inventory
		'''
		self.inventory = Inventory()
		self.menu()

	def menu(self) -> None:
		'''
		sparar användarens menyval i user_choice
		'''
		user_choice = None
		while user_choice != "0":
			self.print_menu()
			user_choice = input("Ange val: ")
			if user_choice == "1":
				self.print_products()
			elif user_choice == "2":
				self.search_products()
			elif user_choice == "3":
				self.add_product()
			elif user_choice == "4":
				self.remove_product()
			elif user_choice == "0":
				print("Hejdå!")
			else:
				print("Age ett korrekt menyalternativ!")

	def print_menu(self) -> None:
		'''
		printar ut menyn för användaren
		'''
		print("\nMeny")
		print("-----")
		print("1) Lista produkter")
		print("2) Sök produkter")
		print("3) Lägg till en produkt")
		print("4) Ta bort en produkt")
		print("0) Avsluta")

	def add_product(self) -> None:
		'''
		låter användaren lägga till en produkt i affären
		'''
		print("\nLägg till en produkt")
		print("------------------")
		p_number = int(input("Produktnummer: "))
		p_name = input("Produktnamn: ")
		p_price = int(input("Pris: "))
		self.inventory.add_product(p_number, p_name, p_price)

	def print_products(self) -> None:
		'''
		Printar ut samtliga produkter som finns i affären för användaren, finns där inga får användaren ett felmeddelande
		'''
		products = self.inventory.get_products()

		if len(products) == 0:
			print("Det finns inga produkter i inventariet")
		else:
			print("\nProdukter")
			print("-------")
			for product in products:
				print(product)
				print("-"*15)


	def search_products(self) -> None:
		'''
		Låter användaren ange en söksträng för att hitta befintliga produkter i affären
		'''
		search_string = input("Ange söksträng: ")
		results = self.inventory.search_products(search_string)

		if len(results) == 0:
			print("Inga träffar")
		else:
			print("\nResultat")
			print("-"*20)
			for product in results:
				print(product)
				print("-"*20)

	def remove_product(self):
		remove_id = int(input("Välj ett id som du vill ta bort: "))
		
		if self.inventory.remove_product(remove_id):
			print(f"Produkten med {remove_id} har tagits bort!")
		
		else: 
			print("Felaktigt id, vänligen ange korrekt nummer")

my_shop = Shop()