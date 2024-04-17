class Person:
	def __init__(self, name, age, gender):
		self.name = name
		self.age = age
		self.gender = gender

	def you(self):
		print(f'Hi my name is {self.name}, and I am {self.age} years, and i am a {self.gender}')

p1 = Person("Isaac", 22, "male")

p1.you()

