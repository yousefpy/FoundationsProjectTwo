# CREATION OF DATA
####################### DO NOT MODIFY THE CODE BELOW ########################
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
