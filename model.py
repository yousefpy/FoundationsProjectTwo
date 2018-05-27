# CLASSES AND METHODS
class Store():
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

class Product():
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def __repr__(self):
        return "\tProduct Name: %s\n\tDescription: %s\n\tPrice: %s KWD" %(self.name, self.description, self.price)


class Cart():
    def __init__(self):
        self.products = []

    def add_to_cart(self, product):
        self.products.append(product)

    def get_total_price(self):
        price = 0
        for product in self.products:
            price += product.price

        return price

    def print_receipt(self):
        print("Here's your receipt: ")
        for product in self.products:
            print(product)
            print()

        print("Your total price is: KD%s" % self.get_total_price())

    def checkout(self):
        print("-----------------------------------")
        self.print_receipt()
        confirm = input("Confirm?(yes/no)")
        if confirm.lower() == "yes":
            self.products = []
            print("Your order has been placed.")
        else:
            print("Your order has been cancelled.")


site_name = "www.achoo.com"
cart = Cart()

def welcome():
    print("Welcome to %s\nFeel free to shop throughout the stores we have, and only checkout once!" % site_name)

def shop():
    item = ""
    while item.lower() != "checkout":
        item = ""
        print_stores()
        store_name = input("Pick a store by typing its name. Or type \"checkout\" to pay your bills and say your goodbyes.\n")
        picked_store = None

        # make util function
        for store in stores:
            if store.name.lower() == store_name.lower():
                picked_store = store

        # make method
        print("-----------------------------------")
        print("%s:" % picked_store.name)
        for product in picked_store.products:
            print(product)
            print()

        print("Pick the items you'd like to add in your cart by typing the product name exactly as it was spelled above.")
        print("Type \"checkout\" to pay your bills and say your goodbyes.")
        print("Type \"back\" to go back and shop at another store.")

        while item.lower() != "back" and item.lower() != "checkout":
            for product in picked_store.products:
                if item.lower() == product.name.lower():
                    cart.add_to_cart(product)
            item = input()

def thank_you():
    print("Thank you for shopping with us at %s" % site_name)
