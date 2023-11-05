class Customer:

	#self is required for every methods that is based on an object
	def __init__(self, name, membership_type):
		self.name = name
		self.membership_type = membership_type
	
	def update_membership(self, new_membership):
		#do anything else

		self.membership_type = new_membership
  
	def read_customer():
		print('Hi Customer')
  
	def print_all_customers(customers):
		for customer in customers: 
			print(customer)
	
	#by default if we did not overrider the string method, 
 	# it will display the memory address of the object
	def __str__(self): 
		return self.name + " " + self.membership_type

	#by default if we did not override the equal method, 
 	#it will compare by object memory location
	def __eq__(self, other): 
		if (self.name == other.name and 
			self.membership_type == other.membership_type
      	): 
			return True

		return False

	#to display customer list via print
	__repr__ = __str__
	#Or 
	#def __repr__(self): 
	#	return self.__str__()
	
	
# there is no "new" keyword in python
c = Customer("Simon Pangan", "Gold")

print(c.name)
print(c.membership_type)


customers = [
	Customer("Simon Pangan", "Gold"),
	Customer("Caleb Curry", "Gold"),
]

print(customers[1].name)

#python is dynamic 
# such that you can add attributes after you construct the object
# but it is best practice to put every initialization in the constructor
customers[1].verified = False

print(customers[1].verified)

customers[1].update_membership('Bronze')

print(customers[1].membership_type)

# not going to work since there is no self in method
# self is required if the method is based on an customer object, 
# it is passed by default by python 
# customers[1].read_customer()

# This is static methods. Basically methods that are not tied in every individual object
Customer.read_customer()


#object __str__
print(customers[0])


print("----")
Customer.print_all_customers(customers)


#object __eq__
print("----")

customer1 = Customer('Simon', "Gold")
customer2 = Customer('Simon', "Gold")
customer3 = Customer('Pangan', "Gold")
customer4 = customer1

print(customer1 == customer2)
print(customer1 == customer3)

#by default if we did not override the equal method, 
#it will compare by object memory location as shown below
print(id(customer1),  id(customer3))
print(id(customer1),  id(customer4))


#to display customer list via print: __repr__ = __str__
print("---------")
print(customers)
