# TRIGGERING USER INTERFACE FUNCTIONALITY
from data import stores, print_stores
from model import Cart

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


welcome()
shop()
cart.checkout()
thank_you()


# welcome()
# shop()  # repeats until "checkout"
# checkout()
# thank_you()
