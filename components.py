# CLASSES AND METHODS
class Store():
    def __init__(self, name):
        """
        Initializes a new store with a name.
        """
        # your code goes here!

    def add_product(self, product):
        """
        Adds a product to the list of products in this store.
        """
        # your code goes here!

    def print_products(self):
        """
        Prints all the products of this store in a nice readable format.
        """
        # your code goes here!


class Product():
    def __init__(self, name, description, price):
        """
        Initializes a new product with a name, a description, and a price.
        """
        # your code goes here!

    def __str__(self):
        # your code goes here!


class Cart():
    def __init__(self):
        """
        Initializes a new cart with an empty list of products.
        """
        # your code goes here!

    def add_to_cart(self, product):
        """
        Adds a product to this cart.
        """
        # your code goes here!

    def get_total_price(self):
        """
        Returns the total price of all the products in this cart.
        """
        # your code goes here!

    def print_receipt(self):
        """
        Prints the receipt in a nice readable format.
        """
        # your code goes here!

    def checkout(self):
        """
        Does the checkout.
        """
        # your code goes here!
