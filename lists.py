"""a LIST is a collection of items
# The items can be of any datatype in a single list
# Can contain other collections (lists, dictionaries, tuples) as items
# Lists are MUTABLE (items can be added, removed, changed)
# Maintain the order (can use index to find an item)"""

fruits = ["peaches", "pears", "apples"]
years = [3, "1998", 2.5, 987, "1994"]
print(fruits, years)
"""LIST METHODS:
 Append: Using this method i can add a single item to the list"""

fruits.append("oranges")
print(fruits)

"""Extend: Allows us to extend the list with another list"""

fruits.extend(years)
print(fruits)

"""Remove: Removes an exact item match in the list"""

fruits.remove("oranges")
print(fruits)

""" Pop: Removes an item from the list using exact index number
If I want to remove an item but i'm not sure about the length of a list
i can use the concept of negative indexing which starts at the end of a list"""

fruits.pop(0)
print(fruits)
fruits.pop(-1)

"""Sort: This method can only be used with lists of like types"""

numbers = [5, 1928, 4, 17, 68, 73.76, 20.458]
numbers.sort()

print(numbers)

"""In: checking membership in a list. """

fruits = ["peaches", "apples", "pears", "apples", "apples"]
years = [3, "1998", 2.5, 987, "1994"]

print("apple" in fruits)
#false
print("apples" in fruits)
#true

"""Count: You can also check membership and the number of items with the count function"""

print(fruits.count("apples"))

"""Index: You can also check membership as well as the index position using the index function"""

print(fruits.index("apples"))