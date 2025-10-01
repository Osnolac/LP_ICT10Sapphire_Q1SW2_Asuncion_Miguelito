from pyscript import display
#Restaurant Order System (Python Data Types)

#String
restaurant_name = "Krusty Krab"
owner_name = "Eugene H. Krabs"

#Integer
year_since = 1999

#Float
tax_rate = 0.08

#Boolean
has_delivery = True
is_dine_in = True
is_takeaway = False

#List
product_name =["Krabby Patty", "Kelp Rings", "Coral Bits"]
beverages = ["Kelp Shake", "Seafoam Soda"]

#Tuple
business_hours = ("9:00 AM", "6:00 PM")

#Dictionary
menu = {
    "Krabby Patty" : 1.25,
    "Kelp Rings" : 1.50,
    "Coral Bits" : 1.25,
    "Kelp Shake" : 2.00,
    "Seafoam Soda" : 1.25
}

#Set
common_allergens = ("gluten","dairy", "nuts")

#Display restaurant information
display(restaurant_name, target="name1")
display(f"Owner : {owner_name}", target="owner")
display(f"Since {year_since}", target="since")
display(f"Menu Pricelist", target="heading1")

#Display menu items
display(product_name[0], target="prod1")
display(f"${menu['Krabby Patty']:.2f}", target="price1")
display(product_name[1], target="prod2")
display(f"${menu['Kelp Rings']:.2f}", target="price2")
display(product_name[2], target="prod3")
display(f"${menu['Coral Bits']:.2f}", target="price3")

display(beverages[0], target="prod4")
display(f"${menu['Kelp Shake']:.2f}", target="price4")
display(beverages[1], target="prod5")
display(f"${menu['Seafoam Soda']:.2f}", target="price5")

#Display additional information
display(f"Open: {business_hours[0]} - {business_hours[1]}", target="openingHours")

#Display order type
display(f"Dine-in Available", target="orderType")