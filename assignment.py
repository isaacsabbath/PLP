# Week two assignment:
#Create an empty list called my_list.
#Append the following elements to my_list: 10, 20, 30, 40.
#Insert the value 15 at the second position in the list.
#Extend my_list with another list: [50, 60, 70].
#Remove the last element from my_list.
#Sort my_list in ascending order.
#Find and print the index of the value 30 in my_list.
#
my_list = []


for i in range(0, 4):
	lst = int(input("Enter intergers: "))

	my_list.append(lst)

my_list.insert(2, 15)
another = [50,60,70]
my_list.extend(another)
del my_list[-1]

print(my_list)


