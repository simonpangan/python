# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.


#Create tuple


#Parenthesis for tuples, square brackets for array 
fruits = ('Apples', 'Oranges', 'Grapes')

#Or using the constructor

fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

print(fruits, fruits2)

#Get a value

print(fruits[1])

#Can't change a value will throw an error

#fruits[0] = 'Simon'

# Delete a tuple
del fruits2

# print(fruits2)

#Get a length
print(len(fruits))

#For tuple always leave a comma if you only have 1 value. 
# Because if not it is going to be treat as string

fruits3 = ('Apples')

print(fruits3, type(fruits3)) 

fruits3 = ('Apples',)

print(fruits3, type(fruits3)) 
