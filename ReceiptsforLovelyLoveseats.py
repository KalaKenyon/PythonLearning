#Created a variable for description and assigned a multi-line string to it
lovely_loveseat_description = """
Lovely Loveseat. Tufted
polyester blend on wood. 32
inches high x 40 inches wide
x 30 inches deep. Red or white.
"""
#Creating a price variable and setting price
lovely_loveseat_price = 254.00

#Add another variable and string for a different product
stylish_settee_description = """
Stylish Settee. Faux leather on
birch. 29.50 inches high
x 54.75 inches wide x 28 inches
deep. Black.
"""

#Created another variable to set the price, like before
stylish_settee_price = 180.50

#Add another variable/item
luxurious_lamp_description = """
Luxurious Lamp. Glass and iron.
36 inches tall. Brown with 
cream shade.
"""

#And again, add a price variable
luxurious_lamp_price = 52.15

#Since this is a store, calculate sales tax of 8.8%
sales_tax = .088

#Business is hot! We got a customer, keep a tally going
customer_one_total = 0
#0 because they haven't bought anything yet

#Also keep a list of the descriptions of the things they get
customer_one_itemization = ""
#which is set to empty string

#customer wants to buy the loveseat, add it to the total
customer_one_total += lovely_loveseat_price

#keep track of items
customer_one_itemization += lovely_loveseat_description

#Now the customer wants the lamp, add both price and description
customer_one_total += luxurious_lamp_price
customer_one_itemization += luxurious_lamp_description

#customer wants to check out with both items, 
#calculate sales tax first then add it to the customer's cost
customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax

#print the receipt!
print("Customer One Items: ")
print(customer_one_itemization)
print("Customer One Total:")
print(customer_one_total)
