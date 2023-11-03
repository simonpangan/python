# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Brad'
age = 37

# Concatenate
print('Hello, my name is ' + name + " . My age is " + str(age))

# String Formatting

# Arguments by position
print(
    'My name is {name} and I am {age}'.format(name=name, age=age) #inside the strings are placeholders
)
# F-Strings (3.6+)
print(f'Hello, my name is {name} and I am {age}')


# String Methods

s = 'hello world'

print(s.capitalize())

s = 'SIMON'
print(s.lower())