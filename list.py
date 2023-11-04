# A List is a collection which is ordered and changeable. Allows duplicate members.
# just like an array in other languages 

#Create a list
numbers = [1, 2, 3, 4, 5, 7, 6]
fruits = ['Apples', 'Oranges', 'Grapes', "Pears"]

#Use a constructor
numbers2 = list((1, 2, 3, 4, 5))

print(numbers, numbers2)

#Get a value
print(fruits[1])

#Get length
print(len(fruits))

#Append to list
fruits.append('Mangos')

print(fruits)

#Remove from list
fruits.remove('Grapes')

print(fruits)

#Insert into position
fruits.insert(2, "Strawberries");

print(fruits);

#Change Value
fruits[0] = 'Simon'

print(fruits);

#Remove with pop
fruits.pop(2);

print(fruits);

#Reverse the list
fruits.reverse();

print(fruits);

#Sort
fruits.sort()

print(fruits)

fruits.sort(reverse=True)

print(fruits)