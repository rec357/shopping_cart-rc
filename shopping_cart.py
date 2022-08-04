from datetime import datetime


products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71


# TODO: write some Python code here to produce the desired output

#list inputs

id_list = []
valid_inputs = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']

while True:
    id = input("Please enter a product identifier: ")
    if id in valid_inputs:
        id_list.append(id)

    else: 
        print("Invalid input. Please enter valid id :)")

    if id == "DONE":
        break

print(id_list)

#source: https://cs.stanford.edu/people/nick/py/python-while.html


#current date and time

now = datetime.now()

DATE = now.strftime("%Y-%m-%d %I:%M %p")

# source: https://stackoverflow.com/questions/1759455/how-can-i-account-for-period-am-pm-using-strftime

# Name of Store and Top of Receipt

print("------------------------------------")
print("RITA'S FARM FRESH FOODS")
print("WWW.RITA'S-FARM-FRESH-FOODS.COM")
print("------------------------------------")
print("CHECKOUT AT: " + DATE)
print("------------------------------------")
print("SELECTED PRODUCTS:")

#list of products

product_name_list = []
product_price = []

for I in id_list:  
    for P in products:
        if P["id"] == int(I):
            product_name_list.append(P["name"])
            product_price.append(P["price"])

length = len(product_name_list)
   
for i in range(length):
    #print(i)
    print("... " + product_name_list[i] +  " ($" + str(product_price[i]) + ")")

#pricing of total products

SUBTOTAL = sum(product_price)
TAX = SUBTOTAL * .0875
TOTAL = SUBTOTAL + TAX

format_subtotal = "{:.2f}".format(SUBTOTAL)
format_tax = "{:.2f}".format(TAX)
format_total = "{:.2f}".format(TOTAL)

#source: https://pythonguides.com/python-print-2-decimal-places/


print("------------------------------------")
print("SUBTOTAL: $" + str(format_subtotal))
print("TAX: $" + str(format_tax))
print("TOTAL: $" + str(format_total))

# closing statement
print("------------------------------------")
print("THANK YOU! HAVE A FARM FRESH DAY :)")
print("------------------------------------")
