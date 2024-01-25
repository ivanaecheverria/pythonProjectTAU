#comment
#variables are case sensitive
#variables must be descriptive

_cars = 23
cars = 24
CARS = 25
CARS = 32324

number_of_cars = 35
type_of_cars = "Ferrari"

print(_cars)
print(cars)
print(CARS)
print(number_of_cars)
print(type_of_cars)

## Data Types ##
# Strings: Are enclosed in single or double quotes / The are INMUTABLE (operations cannot be performed)

name_of_bitch = "ivana"
number_of_the_beast = "666"

print(name_of_bitch)
print(number_of_the_beast)

# Integers are whole numbers, Mathematical operations can be performed
# Floating point no need to specificate decimal numbers

#String Formatting#

"""
This is a multi-line comment. 
You can use this kind of comment to make longer 
notes as you are learning.
In Python, these are often used as docstrings.
We will do formatting now
"""

name = "Janelle Jones"
type_of_car = "Rolls Royce"
school = "Foundation Elementary School"

print(name + school)
print(name + " " + school)
print(name + " works at " + school+ ". ")

#python string.format()

print("{} works at {}.".format(name,school))




