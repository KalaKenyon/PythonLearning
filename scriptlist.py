first_names = ["Ainsley", "Ben", "Chani", "Depak"]
preferred_size = ["Small", "Large", "Medium"]
preferred_size.append("Medium")

print(preferred_size)

customer_data = [["Ainsley", "Small", True ], ["Ben", "Large", False ], ["Chani", "Medium", True ], ["Depak", "Medium", False ]]

#Changes Chani's to regular shipping
customer_data[2][2]= False

#Removes Ben's shipping option
customer_data[1].remove(False)

#adding 2 new customers
customer_data_final = customer_data + [["Amit", "Large", True],["Karim", "X-Large", False]]

print(customer_data_final)

