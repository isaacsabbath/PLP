
def divisible_by_ten(num):
	if num % 10 == 0:
		return True

	else:
		return False

num = int(input("Enter your number: "))

print("The number is: ", divisible_by_ten(num))