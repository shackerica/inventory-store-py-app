# Empty dictionary to store product details
inventory = {}

# Variables for product details
Product1 = "Mobile Phone"
Product1_quantity = 5
Product1_price = 20000
Product1_releaseYear = 2020

# Add details in the inventory
inventory["Product1"] = Product1
inventory["Product1_quantity"] = Product1_quantity
inventory["Product1_price"] = Product1_price
inventory["Product1_releaseYear"] = Product1_releaseYear

# Variables for the 2nd product details
Product2 = "Laptop"
Product2_quantity = 10
Product2_price = 50_0000
Product2_releaseYear = 2020

# Add 2nd product details in the inventory
inventory["Product2"] = Product2
inventory["Product2_quantity"] = Product2_quantity
inventory["Product2_price"] = Product2_price
inventory["Product2_releaseYear"] = Product2_releaseYear

# Displays the products in inventory
print(inventory)

# Checking if Product1_releaseYear & Product2_releaseYear is in the inventory

print("Product1_releaseYear" in inventory)
print("Product2_releaseYear" in inventory)

# Checking if Product3_releaseYear is in the inventory this will return False
print("Product3_releaseYear" in inventory)