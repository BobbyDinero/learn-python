print("Thank you for choosing Sal's Super Speedy Shipping!\nWe Ship Packages & Deliver Smiles :)\n")
print("Here is a cost breakdown for your shipment...\n")

weight = 3.2

flat_charge = 20

#Ground Shipping
if weight <= 2:
  ground_cost = (1.5 * weight) + flat_charge
elif weight > 2 and weight <= 6:
  ground_cost = (3 * weight) + flat_charge
elif weight > 6 and weight <= 10:
  ground_cost = (4 * weight) + flat_charge
else:
  ground_cost = (4.75 * weight) + flat_charge

#Drone Shipping
if weight <= 2:
  drone_cost = 4.5 * weight
elif weight > 2 and weight <= 6:
  drone_cost = 9 * weight
elif weight > 6 and weight <= 10:
  drone_cost = 12 * weight
else:
  drone_cost = 14.25 * weight

#Ground Shipping Premium
ground_ship_premium = 125

print(f"It will cost ${ground_cost:.2f} to ship this with Ground Shipping.")
print(f"It will cost ${ground_ship_premium:.2f} to ship this with Ground Shipping Premium")
print(f"It will cost ${drone_cost:.2f} to ship this with Drone Shipping.\n")

if ground_cost < ground_ship_premium and ground_cost < drone_cost:
  print("We recommend using Ground Shipping. That would be most cost effective.")
elif ground_cost > ground_ship_premium and ground_ship_premium < drone_cost:
  print("We recommend using Ground Shipping Premium. That would be most cost effective due to the flat rate pricing.")
elif ground_cost > drone_cost and ground_ship_premium > drone_cost:
  print("You should try out our new Drone Shipping option! That would be most cost effective!")
elif weight <= 6:
  cost_drone = weight * 9.00
elif weight <= 10:
  cost_drone = weight * 12.00
else:
  cost_drone = weight * 14.25

print("Drone Shipping: $", cost_drone)
