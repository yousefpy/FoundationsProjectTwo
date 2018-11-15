# UTILS AND FUNCTIONALITY
from data import stores
from components import Cart

site_name = "www.iShop.com.kw"  # Give your site a name

def welcome():
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("Welcome to %sFeel free to shop throughout the stores we have, and only checkout once!" % site_name)
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

def print_stores():
    """
    prints the list of stores in a nice readable format.
    """
    for i in stores:
        print("- %s" % i.name)

    print("-----------------------------------------------------------------------------------------------------")

def get_store(store_name):
    """
    receives a name for a store, and returns the store object with that name.
    """
    for i in stores:
        if store_name == i.name:
            return i

    return False

def pick_store():
    """
    prints list of stores and prompts user to pick a store.
    """
    print_stores()
    print("Pick a store by typing its name. Or type \"checkout\" to pay your bills and say your goodbyes.")
    user_input = input()
    while user_input.lower() != "checkout":
        if get_store(user_input) != False:
            return get_store(user_input)
            break
        else:
            print("Please check your spell, Pick a store or type checkout:")
            user_input = input()

    if user_input.lower() == "checkout":
        return "checkout"


def pick_products(cart, picked_store):
    """
    prints list of products and prompts user to add products to card.
    """
    print("===================================================")
    print("type exactly the item you want to buy and press 'Enter'\nType 'back' to go back to the main menu where you can checkout:")
    user_input = input()
    while user_input.lower() != "back":
        for item in picked_store.store_list_of_product:
            if user_input == item.name:
                cart.add_to_cart(item)
            elif user_input.lower() == "checkout":
                return "checkout"

        user_input = input()
        if user_input.lower() == "checkout":
            return "checkout"

def shop():
    """
    The main shopping functionality
    """
    cart = Cart()
    user_input = ""
    while user_input != "checkout":
        picked_store = pick_store()
        if picked_store == "checkout":
            break

        picked_store.print_products()
        user_input = pick_products(cart, picked_store)

    cart.checkout()

def thank_you():
    print("Thank you for shopping with us at %s" % site_name)
