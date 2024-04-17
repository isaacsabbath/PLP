# A function program to calculate final price after is either applied or not
def calculate_discount(price,discount_percent):
	finalP = price * (discount_percent/100)

	# defining the condition
	if discount_percent >= 20:
		return finalP

	else:
		return price

price = int(input("Enter the price: "))
discount_percent = int(input("Enter the discount: "))
print("The price is? ", calculate_discount(price,discount_percent))