"""
Sukurkite keletą savo pavyzdžių, kuriuose parodytumėte ir panaudotumėt keletą OOP paradigmų praktikoje.
Parašykite klasę CoffeeShop, kuri turi tris inicializuotos klasės kintamuosius:
name: str (iš esmės parduotuvės pavadinimas)
meniu : elementų sąrašas (list) (dict tipo), kuriame kiekvienas elementas turi elementą (elemento pavadinimą), tipą (ar tai maistas, ar gėrimas) ir kainą.
orders: tuščias list
ir septyni metodai:
add_order: į užsakymų sąrašo pabaigą įtraukia prekės pavadinimą, jei jis yra meniu, priešingu atveju grąžina "Šiuo metu šios prekės nėra!".
fulfill_order: jei užsakymų sąrašas nėra tuščias, grąžinama "{prekė} yra paruošta!". Jei užsakymų sąrašas tuščias, grąžinkite "Visi užsakymai įvykdyti!".
list_orders: grąžina priimtų užsakymų prekių pavadinimus, priešingu atveju - tuščią sąrašą.
due_amount: grąžina bendrą mokėtiną sumą už priimtus užsakymus.
cheapest_item: grąžina pigiausio meniu elemento pavadinimą.
drinks_only: grąžina tik meniu gėrimų tipo elementų pavadinimus.
food_only: grąžina tik meniu maisto tipo elementų pavadinimus.
"""


class CoffeeShop:
    def __init__(self, menu_list_var=None):
        if menu_list_var is None:
            menu_list_var = []
        self.name = "Pardoshke"
        self.menu = menu_list_var
        self.orders = []

    def add_order(self, order: str):
        for argument in self.menu:
            if order in argument.get("name"):
                self.orders.append(order)
                print("Your order added!")
                return
        print("Šiuo metu šios prekės nėra!")
        # if order in menu_index:
        #     self.orders.append(order)
        # else:
        #     print("Šiuo metu šios prekės nėra!")

    def fulfill_order(self):
        if len(self.orders) > 0:
            for order in self.orders:
                print(f"{order} yra paruošta!")
        else:
            print("Visi užsakymai įvykdyti!")

    def list_orders(self):
        # result = []
        # if orders
        pass

    def due_amount(self):
        pass

    def cheapest_item(self):
        pass

    def drinks_only(self):
        pass

    def food_only(self):
        pass


menu = [
    {"name": "Cheeseburger", "type": "food", "price": 9.99},
    {"name": "Caesar Salad", "type": "food", "price": 8.49},
    {"name": "Margherita Pizza", "type": "food", "price": 11.99},
    {"name": "Spaghetti Carbonara", "type": "food", "price": 12.99},
    {"name": "Grilled Chicken Sandwich", "type": "food", "price": 10.99},
    {"name": "Mojito", "type": "drink", "price": 7.99},
    {"name": "Iced Latte", "type": "drink", "price": 4.49},
    {"name": "Red Wine (glass)", "type": "drink", "price": 8.99},
    {"name": "Margarita", "type": "drink", "price": 9.99},
    {"name": "Lemonade", "type": "drink", "price": 3.99},
    {"name": "BBQ Ribs", "type": "food", "price": 15.99},
    {"name": "Vegetable Stir Fry", "type": "food", "price": 11.49},
    {"name": "Fish and Chips", "type": "food", "price": 13.99},
    {"name": "Chocolate Cake", "type": "food", "price": 6.99},
    {"name": "Cappuccino", "type": "drink", "price": 4.99},
    {"name": "Green Tea", "type": "drink", "price": 3.49},
    {"name": "Chicken Caesar Wrap", "type": "food", "price": 9.49},
    {"name": "Soda (can)", "type": "drink", "price": 2.49},
    {"name": "Beef Tacos", "type": "food", "price": 10.99},
    {"name": "Mai Tai", "type": "drink", "price": 8.49},
]


tcs = CoffeeShop(menu_list_var=menu)

tcs.add_order("hot cocoa")  # ➞ "This item is currently unavailable!"
# Tesha's coffee shop does not sell hot cocoa
tcs.add_order("iced tea")  # ➞ "This item is currently unavailable!"
# specifying the variant of "iced tea" will help the process

tcs.add_order("Margherita Pizza")  # ➞  "Order added!"
tcs.add_order("Vegetable Stir Fry")  # ➞ "Order added!"
print(tcs.orders)
print(tcs.list_orders())  # ➞ ["cinnamon roll", "iced coffee"]
# all items of the current order

tcs.due_amount()  # ➞ 2.17
tcs.fulfill_order()  # ➞ "The cinnamon roll is ready!"
tcs.fulfill_order()  # ➞ "The iced coffee is ready!"
tcs.fulfill_order()  # ➞ "All orders have been fulfilled!"
# all orders have been presumably served

tcs.list_orders()  # ➞ []
# an empty list is returned if all orders have been exhausted

tcs.due_amount()  # ➞ 0.0
# no new orders taken, expect a zero payable

tcs.cheapest_item()  # ➞ "lemonade"
tcs.drinks_only()  # ➞ ["orange juice", "lemonade", "cranberry juice", "pineapple juice", "lemon iced tea", "vanilla chai latte", "hot chocolate",
# "iced coffee"]
tcs.food_only()  # ➞ ["tuna sandwich", "ham and cheese sandwich", "bacon and egg", "steak", "hamburger", "cinnamon roll"]
