#Домашння робота
class Clothing:
    def __init__(self, material, name, price, size):
        self.material = material
        self.name = name
        self.price = price
        self.size = size
class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.inventory = []
    def add_item(self, item):
        self.inventory.append(item)
    def remove_item(self, item):
        self.inventory.remove(item)
    def get_items(self):
        return self.inventory
    def search_items(self, keyword):
        matching_items = []
        for item in self.inventory:
            if keyword.lower() in item.name.lower():
                matching_items.append(item)
        return matching_items
class Customer:
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
        self.cart = []
    def add_to_cart(self, item):
        if item.price <= self.budget:
            self.cart.append(item)
            self.budget -= item.price
            print(f"{item.name} додано в кошик..")
        else:
            print("Недостатньо бюджету, щоб додати товар у кошик.")
    def remove_from_cart(self, item):
        if item in self.cart:
            self.cart.remove(item)
            self.budget += item.price
            print(f"{item.name} видалено з кошика.")
        else:
            print("Товар не знайдено в кошику.")
    def view_cart(self):
        print(f"{self.name} кошик:")
        for item in self.cart:
            print(f"- {item.name} (${item.price})")
    def checkout(self):
        total_price = sum(item.price for item in self.cart)
        if total_price <= self.budget:
            self.budget -= total_price
            self.cart = []
            print("Оформлення завершено.")
        else:
            print("Недостатній бюджет для завершення покупки.")
shop = Store("Модний магазин", "123 Головна вул")
item1 = Clothing("Бавовна", "Футболка", 20, "M")
item2 = Clothing("Джинса", "Джинси", 50, "L")
item3 = Clothing("Шерсть", "светр", 40, "S")
shop.add_item(item1)
shop.add_item(item2)
shop.add_item(item3)
customer = Customer("Максіка", 100)
search_results = shop.search_items("джинси")
if search_results:
    customer.add_to_cart(search_results[0])
customer.view_cart()
customer.remove_from_cart(item1)
customer.view_cart()
customer.checkout()

