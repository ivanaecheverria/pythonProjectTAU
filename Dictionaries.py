"""Dictionaries are a type of Python data collection that stores the data in key/value pairs.
# The keys are generally made of Strings, integers, or tuples, and need to be both unique and immutable.
# You can make an empty dictionary by assigning a dictionary name with nothing in the curly braces
or can contain a million of entries
# Dictionaries are mutable and can be changed using the Python dictionary methods
"""
# Methods
# dictionary.get : we can return the value of one of the keys in the dictionary

stuff = {"food": 18, "energy": 100, "enemies": 3}
print(stuff.get("food"))

# dictionary.items(): Takes the name of the dictionary and outputs a view of the key/value pairs

print(stuff.items())

# dictionary.keys() : Returns a view of all the keys in the dictionary

print(stuff.keys())

# dictionary.popitem : Allows us to remove the last item in a dictionary

print(stuff.popitem())
print(stuff)

# dictionary.setdefault : Allows us to see what the value is of a key that is in the dictionary
# But more importantly allows us to set a default value when a key is not in the dict and to add value to the dict

print(stuff.setdefault("food"))
print(stuff)
print(stuff.setdefault("friends", 123))
print(stuff)

# dictionary.update : One way to use the update method is to update the first dictionary with another dictionary

new_items = {"rocks": 4, "arrows": 18}
stuff.update(new_items)
print(stuff)

# We can also update existing items in the dictionary through the same process

new_items = {"rocks": 2, "arrows": 5}
stuff.update(new_items)
print(stuff)

# We can update and add new items at the same time

up_new = {"food": 3, "webs": 2}
stuff.update(up_new)
print(stuff)

#Finally we can add items directly to the update method in order to use it

stuff.update(food = 450, cookies = 6)
print(stuff)