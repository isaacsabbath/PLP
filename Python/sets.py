# am original program to input integers in different sets and prints the common intergers in the sets

#initialization of a new set
A = set()
B = set()

#the range of integers in each set but the user inputs 10 digits since its two sets.
num = int(input("How many integers do you want?: "))

#using a for loop to input the integers in the sets
for i in range(num):
		a = int(input("Add your numbers: "))
		A.add(a) # this method adds the integers in set A
		b = int(input("Add your numbers: "))
		B.add(b) # this method adds the integers in set A

print("Elements in both sets are:", A & B) # prints the common integers in the two sets.