# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object
# Python can be used using different programming paradigms such as procedural, object-oriented, and functional programming. Python supports object-oriented programming (OOP).

#Create class

class User:
    
    #Constructor
	def __init__(self, name, email, age):
		self.name = name
		self.email = email
		self.age = age
		# print('Constructor called')
	
	def greeting(self):
		return f'My name is {self.name} and I am {self.age}'
	
	def has_birthday(self):
		self.age += 1
  
  
#Extend class

class Customer(User):
    
	def __init__(self, name, email, age):
		self.name = name
		self.email = email
		self.age = age
		self.balance = 0
		# print('Constructor called')
  
	def set_balance(self, balance):
		self.balance = balance

 
	def greeting(self):
		return super().greeting() + f' and my balance is {self.balance}'

#Init user object

simon = User('Simon Pangan', 'simon_pangan@yahoo.com', 23)

print(simon.name)
simon.has_birthday()
print(simon.greeting())

#Init customer object

janet = Customer('Janet Pangan', 'simon_pangan@yahoo.com', 23)

janet.set_balance(500)

print(janet.greeting())