#this is from the codecademy pro data science course. The project is called 'Carly's clippers.''

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0

total_revenue = 0

#calculates total price

for price in prices:
  total_price = (total_price + price)

#calculates average price

average_price = (total_price // len(prices))

print('Average Haircut Price: ' + str(average_price))

#list comprehension for new list, taking prices and - 5.

new_prices = [x - 5 for x in prices]

print(new_prices)

#calculates total revenue for last week. 

for i in range(len(hairstyles)):
  total_revenue += last_week[i] * prices[i] 
print('Total Revenue: ' + str(total_revenue))

average_daily_revenue = total_revenue // 7

print(average_daily_revenue)

#populates new list of haircuts with new_prices.

cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i] < 30]

print(cuts_under_30)