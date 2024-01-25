"""Python classes allow programmers to group data and information like variables and functions into a single organized unit.
Classes can be organized one to a file, or multiple classes that share similar types of functionality can be organized into the same file.
CLASSES FEATURES: Classes allow us to share information with other classes and with other parts of a Python program.
> Inheritance: allow us to borrow from one class and use elements of that class to create another class.
> Multiple inheritance: allows a class to inherit attributes from multiple classes
> Polymorphism: allows for inherited or derived classes to override the base or parent classes, and all classes in Python are Objects
The statements or information inside of a class are usually functions, but a class can also contain class
 variables that are specific to the class and usable throughout the entire class.
 Instance variables: are specific to any Objects that are created by the class"""
import random

"""
__init__ method: allows every instance of a class to be created or initialized with 
specific parameters pre-determined at the creation of that Object. (Constructor)
> sets the attributes for the Object, for example, the characteristics
> The __init__ method has parameters that accept arguments which determine the attributes of the Object when it is created.
> Once the parameters are given, those parameters are available to every class method."""
"""
Self variable: The self variable in Python represents an instance of a class, 
and specifically it references the instance of the class that has been created.
> We use self in order to make available all of the attributes to the methods throughout the class.
> However, if a method is running as a part of the class rather than as an instance of the class, 
then we do not need to use the self parameter in the method."""

class Person:

    def __init__(self, firstname, lastname, health, status):
        """initialize attributes to be used in/available for all
        class methods in this class, and for class Objects created by this class"""
        self.firstname = firstname
        self.lastname = lastname
        self.health = health
        self.status = status

    def introduce(self):
        """all people will introduce themselves"""
        print("Hi, I'm {} {}. ".format(self.firstname, self.lastname))

    def emote(self):
        emotion = random.randrange(1,3)

        if emotion == 1:
            print("{} is happy today".format(self.firstname))
        elif emotion == 2:
            print("{} is sad right now".format(self.firstname))

    def status_change(self):
        if self.health == 100:
            print("{} is totally healthy".format(self.firstname))
        elif self.health >= 76:
            print("{} is a little tired today".format(self.firstname))
        elif self.health >= 51:
            print("{} feels unwell".format(self.firstname))
        elif self.health >= 40:
            print("{} goes to the doctor".format(self.firstname))
        else:
            print("{} is unconscious".format(self.firstname))
#Instancing the class with their parameters
Maria = Person("Maria","Gutierrez", 95, True)
Rey = Person("Rey", "Jones", 88, False)
Lee = Person("Lee", "Williams", 10, True)

print("{} is my friend? {}".format(Maria.firstname, Maria.status))
print("{} is my friend? {}".format(Rey.firstname, Rey.status))

#Instancing the methods within the class
Maria.introduce()
Rey.introduce()
Lee.introduce()

Maria.status_change()
Rey.status_change()
Lee.status_change()

Maria.emote()

"""INHERITANCE: Inheritance happens when we use the attributes and methods from the parent class and make those attributes and methods available to the child's class."""
"""POLYMORPHISM: Polymorphism occurs when we want to allow the child class to have a method with the same name and a similar implementation as the parent class and we wish for that method you override the parent class method.
For example: Make an 'introduction' method for Enemy class that will have a different outcome"""

class Enemy(Person):
    def __init__(self, weapon, firstname, lastname, health, status):
        super().__init__(firstname, lastname, health, status)
        self.weapon = weapon

    def hurt(self,other):
        if self.weapon == 'rock':
            other.health -= 10
        elif self.weapon == 'stick':
            other.health -= 5
        print(other.health)

    def insult(self, other):
        if other.health <= 80:
            print("{}, you are tired and weak".format(other.firstname))

    def steal(self, other):
        print("ha ha ha, {}, I have your stuff!".format(other.firstname))
        if other.status == True:
            other.status = False

    def introduce(self):
        print("You are my mortal enemy!!")

#Create new Enemy character

Alex = Enemy('rock', 'Alex', 'Wayne', '75', False)
Alex.hurt(Maria)
Alex.insult(Rey)
Alex.insult(Lee)
Alex.steal(Lee)

#Polimorphism example
Maria.introduce()
Rey.introduce()
Alex.introduce()



