weight = 1.5

if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight > 2 and weight <= 6:
  cost_ground = weight * 3.0 + 20
elif weight > 6 and  weight <= 10:
  cost_ground = weight * 4.0 + 20
else:
  cost_ground = weight * 4.75 + 20 

cost_ground_premium = 125

#Drone shipping
if weight <= 2:
  drone_shipping = weight * 4.5
elif weight > 2 and weight <= 6:
  drone_shipping = weight * 9.0
elif weight > 6 and  weight <= 10:
  drone_shipping = weight * 12.0
else:
  drone_shipping = weight * 14.25 

print("The ground shipping price is: ", cost_ground)
print("The premium ground shipping price is: ", cost_ground_premium)
print("The price for drone shipping is: ", drone_shipping)