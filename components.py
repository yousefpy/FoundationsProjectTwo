# CLASSES AND METHODS
class Store():
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def print_products(self):
        print("-----------------------------------")
        print("%s:" % self.name)
        for product in self.products:
            print(product)
            print()


class Product():
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
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
