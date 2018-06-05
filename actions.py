# UTILS AND FUNCTIONALITY
from data import stores
from components import Cart

site_name = ""  # Give your site a name

def welcome():
    print("Welcome to %s\nFeel free to shop throughout the stores we have, and only checkout once!" % site_name)

def print_stores():
    """
    prints the list of stores in a nice readable format.
    """
    # your code goes here!

def get_store(store_name):
    """
    receives a name for a store, and returns the store object with that name.
    """
    # your code goes here!

def pick_store():
    """
    prints list of stores and prompts user to pick a store.
    """
    # your code goes here!

def pick_products(cart, picked_store):
    """
    prints list of products and prompts user to add products to card.
    """
    # your code goes here!

def shop():
    """
    The main shopping functionality
    """
    # your code goes here!

def thank_you():
    print("Thank you for shopping with us at %s" % site_name)



# pick_store():
# print("No store with that name. Please try again.")
# store_name = input("Pick a store by typing its name. Or type \"checkout\" to pay your bills and say your goodbyes.\n")

# shop():
# print("Pick the items you'd like to add in your cart by typing the product name exactly as it was spelled above.")
# print("Type \"back\" to go back to the main menu where you can checkout.")
