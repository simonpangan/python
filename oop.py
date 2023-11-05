# In python, unlike java and any other language it is more free. Our approach is 
# IF WE DON'T NEED IT DON'T DO IT
# This is why in python our classes are sometimes very thin. Example is encaptulation
# In python we have the option to do it or not do it. The person using your classses
# you can trust them that they are well educated and are going to use your classes in
# an appropriate way. WHere as in other language such as java, you have to restrict it

#Encapsulation
# In python encapsulation is more like an optional thing. We can use it or not use it. 
# Unlike in java, c# and other languages where it is a must.
# We don't really need to create those unless we need to. 
# That how python and its developers approach it and is considered as a best practice

class User:
	
	def log(self):
		print(self)

class Customer(User):
	def __init__(self, name, membership_type):
		self.name = name
		self.membership_type = membership_type
	
	# _ prefix is a convention that this is a private variable
	@property
	def name(self):
		#do something here
		return self._name

	@name.setter
	def name(self, name):
		#do something here
		self._name = name
	
	@name.deleter
	def name(self):
		del self._name

	def update_membership(self, new_membership):
		self.membership_type = new_membership
  
	def read_customer():
		print('Hi Customer')
  
	def print_all_customers(customers):
		for customer in customers: 
			print(customer)
	
	def __str__(self): 
		return self.name + " " + self.membership_type

	def __eq__(self, other): 
		if (self.name == other.name and 
			self.membership_type == other.membership_type
      	): 
			return True

		return False

	__repr__ = __str__

customers = [
	Customer("Simon Pangan", "Gold"),
	Customer("Caleb Curry", "Gold"),
]

print(customers[1].name)
# del customers[1].name
print(customers)

customers[1].log()