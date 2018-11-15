# CLASSES AND METHODS
class Store():
    def __init__(self, name):
        """
        Initializes a new store with a name.
        """
        self.name = name
        self.store_list_of_product = []

    def add_product(self, product):
        """
        Adds a product to the list of products in this store.
        """
        self.store_list_of_product.append(product)

    def print_products(self):
        """
        Prints all the products of this store in a nice readable format.
        """
        print("===================================================")
        for item in self.store_list_of_product:
            print(item)

class Product():
    def __init__(self, name, description, price):
        """
        Initializes a new product with a name, a description, and a price.
        """
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return "Product Name : %s\ndescription : %s\nPrice : %s KWD \n" %(self.name , self.description , self.price)


class Cart():
    def __init__(self):
        """
        Initializes a new cart with an empty list of products.
        """
        self.cart_list = []

    def add_to_cart(self, product):
        """
        Adds a product to this cart.
        """
        self.cart_list.append(product)

    def get_total_price(self):
        """
        Returns the total price of all the products in this cart.
        """
        self.total_price = 0
        for item in self.cart_list:
            self.total_price += item.price
        return self.total_price

    def print_receipt(self):
        """
        Prints the receipt in a nice readable format.
        """
        print("*********************************")
        print("Here is your receipt:")
        for item in self.cart_list:
            print(item)

        total_price = str(self.get_total_price())
        print("Your total price : %s KWD" %total_price)
        print("*********************************")

    def checkout(self):
        """
        Does the checkout.
        """
        self.print_receipt()
        confirmation = input("Confirm your oredr 'yes/no' :")
        if confirmation.lower() == "yes":
            print("Your order has been placed")
        else:
            print ("You've cancelled your order")

