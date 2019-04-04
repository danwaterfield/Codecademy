# this is a program to 

price = 0
premium_ground = 125.00

def ground_shipping(weight):
  f_charge = 20.00
  if weight <= 2.0:
    price = (f_charge + weight * 1.50)
    return price
  elif weight >= 2.0 and weight <= 6.0:
    price = (f_charge + weight * 3.00)
    return price
  elif weight > 6.0 and weight <= 10.0:
    price = (f_charge + weight * 4.0)
    return price
  elif weight > 10.0:
    price = (f_charge + weight * 4.75)
    return price
  


def drone_shipping(weight):
  if weight <= 2.0:
    price = (weight * 4.50)
    return price
  elif weight >= 2.0 and weight <= 6.0:
    price = (weight * 9.00)
    return price
  elif weight > 6.0 and weight <= 10.0:
    price = (weight * 12.0)
    return price
  elif weight > 10.0:
    price = ( weight * 14.25)
    return price

def cheapest_shipping(weight):
  ground = ground_shipping(weight)
  drone = drone_shipping(weight)
  prem = premium_ground
  if ground < drone and ground < prem:
    return print('Ground would be cheapest, and the cost is ' + str(ground))
  elif drone < ground and drone < prem:
    return print('Drone would be cheapest, and the cost is ' + str(drone))
  else:
    return print('Premium Ground would be cheapest, and the cost is ' + str(prem))

  
cheapest_shipping(4.8)