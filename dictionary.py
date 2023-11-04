# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

#Create a dictionary
person = {
	'first_name' : 'John',
	'last_name' : 'Doe',
	'age' : 30
}

#Or use a constructor
person2 = dict(first_name='Sara', last_name='Williams')

print(person, type(person))
print(person2, type(person2))

#Get value
print(person['first_name'])
print(person.get('last_name'))

#Add key value
person['phone'] = '555-555-5555'

print(person)

#Get dictionary keys
print(person.keys())

#Get dictionary items
print(person.items())	

#Copy dictionary
person3 = person.copy()
person3['city'] = 'Boston'

print()
print()
print(person3)

#Remove item

del(person['age'])
#Or
person.pop('phone')

print(person)

#Clear
person.clear()

print(person)

#Get length
print(len(person3))

#List of dictonaries

people = [
	{'name': 'Martha', 'age': 30},
	{'name': 'Kevin', 'age': 25},
	{'name': 'Bob', 'age': 40}
]

print(people)
print(people[1]['name'])
