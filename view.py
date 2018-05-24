# TRIGGERING USER INTERFACE FUNCTIONALITY
from data import stores, print_stores
from model import Cart

cart = Cart()
while True:
    item = ""
    print_stores()
    store_name = input("Pick a store by typing its name.\n")
    picked_store = None
    for store in stores:
        if store.name.lower() == store_name.lower():
            picked_store = store

    for product in picked_store.products:
        print(product)
        print()

    while item != "go back" and item != "checkout":
        for product in picked_store.products:
            if item.lower() == product.name.lower():
                cart.add_to_cart(product)
        item = input()

    if item == "checkout":
        break

cart.checkout()
