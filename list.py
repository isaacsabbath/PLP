mangoes = [] # initialising an empty list

# creating the length of the list
num = int(input("Enter a length of list: "))

#sum variable
sum = 0 
for i in range(0, num):
	ele = int(input(" Enter you numbers: ")) #user inputs elements of the list
	sum += ele # adds the elements in the list

	mangoes.append(ele) # method to add the elements in the list

print(sum) # prints the total sum of his elements in the list
