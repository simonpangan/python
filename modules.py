# A module is basically a file containing a set of functions to include in your application. 
# There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# Core modules
import datetime 
from datetime import date
from time import time 	

# Pip modules
from camelcase import CamelCase

# Custom modules
import validator
from validator import validate_email

today = datetime.date.today()
print(date.today())

print(today)

# timestamp = time.time()
# print(timestamp)

timestamp = time()
print(timestamp)

c = CamelCase()
print(c.hump('hello there world'))

if validate_email('simon_pangan@yahoo.com'):
	print('email is valid')
else :
	print('email is bad')

print(validator.validate_email('simon_pangan@yahoo.com'))