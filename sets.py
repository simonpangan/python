# A Set is a collection which is unordered and unindexed. No duplicate members.

#Create a set
fruits_set = {'Apples', 'Oranges', 'Mango'}

#Check if in set
print('Apples' in fruits_set)

#Add set
fruits_set.add('Grape')

print(fruits_set)

#Remove from set
fruits_set.remove('Grape')

print(fruits_set)

#In set there should be no duplicate. It is not going to throw an error but it will not add it twice
fruits_set.add('Apples')

print(fruits_set)

#Clear set

fruits_set.clear()

print(fruits_set)


#Delete a set

del fruits_set

print(fruits_set)