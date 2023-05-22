class FoodItem:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price
class Menu:
    def __init__(self):
        self.items = []
    def add_item(self, item):
        self.items.append(item)
    def remove_item(self, item):
        self.items.remove(item)
    def display_menu(self):
        print("Menu:")
        for item in self.items:
            print(f"{item.name}: {item.description} - ${item.price}")
class Order:
    def __init__(self):
        self.items = []
    def add_item(self, item):
        self.items.append(item)
    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.price
        return total
class Restaurant:
    def __init__(self):
        self.menu = Menu()
        self.orders = []
    def add_item_to_menu(self, item):
        self.menu.add_item(item)
    def remove_item_from_menu(self, item):
        self.menu.remove_item(item)
    def display_menu(self):
        self.menu.display_menu()
    def place_order(self, order):
        self.orders.append(order)
    def remove_order(self, order):
        self.orders.remove(order)
    def generate_bill(self, order):
        total = order.calculate_total()
        print("Bill:")
        for item in order.items:
            print(f"{item.name}: {item.price}")
        print(f"Total: ${total}")
food_item1 = FoodItem("Pizza", "Delicious pizza with cheese and toppings", 10)
food_item2 = FoodItem("Burger", "Juicy burger with a side of fries", 8)
food_item3 = FoodItem("Salad", "Fresh garden salad with dressing", 6)
menu = Menu()
menu.add_item(food_item1)
menu.add_item(food_item2)
menu.add_item(food_item3)
menu.display_menu()
order = Order()
order.add_item(food_item1)
order.add_item(food_item2)
restaurant = Restaurant()
restaurant.place_order(order)
restaurant.generate_bill(order)
with open("orders.txt", "w") as file:
    file.write("Order:\n")
    for item in order.items:
        file.write(f"{item.name}: {item.price}\n")
    file.write(f"Total: ${order.calculate_total()}")
