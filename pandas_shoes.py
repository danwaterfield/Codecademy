#culmination of a pandas tutorial

import codecademylib
import pandas as pd


#opens csv and saves it to orders

orders = pd.read_csv('shoefly.csv')

#let's inspect the first five rows...
print(orders.head(5))

#saves all email addresses from email column to emails variable
emails = orders.email

#finds and displays Frances Palmer's order.

frances_palmer = orders[(orders.first_name == 'Frances') & (orders.last_name == 'Palmer')]

#finds and displays clogs, boots, ballet flats before saving them to comfy_shoes
comfy_shoes = orders[orders.shoe_type.isin(['clogs', 'boots','ballet flats'])]