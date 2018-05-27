# CREATION OF DATA
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


stores = []

def create_product(store, name, description, price):
    product = Product(name, description, price)
    store.add_product(product)

zara = Store("Zara")
nike = Store("Nike")
apple = Store("Apple")
stores = [zara, nike, apple]

create_product(zara, "Nice Yellow Top", "A nice yellow top.", 30)
create_product(zara, "Pants", "100 percent cotton", 25)

create_product(nike, "Running Shoes", "Shoes for running.", 15)
create_product(nike, "Style Shoes", "Stylish shoes.", 20)

create_product(apple, "iPhone X", "256GB Space Gray", 310)
create_product(apple, "iPhone 5s", "128GB Silver", 250)
