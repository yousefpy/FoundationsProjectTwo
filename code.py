stores = []     # this outside variable is what I wanted to avoid when I created the Store class. Icebox.
class Store():
    products = []

    def __init__(self, name):
        self.name = name

class Product():
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def __repr__(self):
        return " Product: %s \n Description: %s \n Price: %s KWD" %(self.name, self.description, self.price)

class Cart():
    products = []
    def add_to_cart(self, product):
        self.products.append(product)

    def get_total_price(self):
        price = 0
        for product in self.products:
            price += product.price

        return price

    def checkout(self):
        print("Here's your receipt: ")
        for product in self.products:
            print(product)

        confirm = input("Confirm?")
        if confirm.lower() == "yes":
            total_price = self.get_total_price()
            product = []
            print("Your total price is: KD%s" % total_price)
        else:
            print("Then why checkout?? God...")


zara = Store("Zara")
nike = Store("Nike")
apple = Store("Apple")
stores = [zara, nike, apple]

top = Product("Nice Yellow Top", "A nice yellow top.", 30)
pants = Product("Pants", "100 percent cotton", 25)
running_shoes = Product("Running Shoes", "Shoes for running.", 15)
style_shoes = Product("Style Shoes", "Stylish shoes.", 20)
iphonex = Product("iPhone X", "256GB Space Gray", 310)
iphone5s = Product("iPhone 5s", "128GB Silver", 250)

zara.products = [top, pants]
nike.products = [running_shoes, style_shoes]
apple.products = [iphonex, iphone5s]

# for store in stores:
#     print("%s: " % store.name)
#     for product in store.products:
#         print(product)
#         print("---------------------------")

def print_stores():
    for store in stores:
        print("- %s" % store.name)

print_stores()
store_name = input("Pick a store by typing its name.\n")
picked_store = None
for store in stores:
    if store.name.lower() == store_name.lower():
        picked_store = store
for product in picked_store.products:
    print(product)
    print()

cart = Cart()
item = ""
item = input()
while item.lower() != "checkout":
    for product in picked_store.products:
        # print("checking \"%s\" vs \"%s\"" % (item.lower(), product.name))
        if item.lower() == product.name.lower():
            # print("MATCH")
            cart.add_to_cart(product)
    item = input()

cart.checkout()
