# This is a function that returns a boolean expression
def large_power(base, exponent): # declaration a function with parameters
	result = base ** exponent # function defination

	if exponent > 5000:
		return True
	else:
		return False

#user input of the parameters
base = int(input("Enter your base: "))  
exponent = int(input("Your exponent is?: "))

#calling the function
result = large_power(base, exponent)
print(result)