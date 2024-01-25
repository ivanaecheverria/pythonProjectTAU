#A for loop is useful when you'd like to iterate over each item in a list.
# The for loop allows you to repeat your action for every item in the list or for a specified number of items in the list.

fruits = ["apple", "orange", "pears", "cherries", "grapes"]

for fruit in fruits:
    print("Would you like {} ?".format(fruit))

for i in fruits:
    print("Would you like {} ?".format(i))

#range is a built-in function in python

for number in range(1,11):
    print("Number {} ".format(number))

#A while loop will run any time a condition remains true
#An infinite loop is a loop that doesn't have any stopping point. It just keeps going.
# we need to make the variable change so the loop can stop appropiately

#decrement operator (-=), and all that does is decrease the variable by whatever number I choose.

temp_f = 40
while temp_f > 32:
    print("The water is {} degrees.".format(temp_f))
    temp_f -= 1
    if temp_f == 33:
        break

#Loop control
# Break: end the loop, go to the next statement in the program(outside the loop)
# Continue: skips current part of the loop. moves to the next part of the loop
# Pass: Skips any part of the loop where "pass" appears. best used for testing code.

for number in range(1,11):
    if number == 7:
        print("We're skipping number 7.")
        continue
    print("This is the number {}.".format(number))
#

for number in range(1,11):
    if number == 3:
        pass
    else:
        print("The number is {}.".format(number))
