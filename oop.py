print(type(int(3)))


class BigObject:
    pass


obj1 = BigObject()  # instantiating the class and creating a new object

print(type(obj1))


class Player:
    # class object attribiute (static)
    membership = True

    def __init__(self, name, age):
        # class attributes (dynamic)
        if (Player.membership):
            self.name = name
            self.age = age

    def run(self):
        print('run')

    def shoutout(self):
        print(f"my name is {self.name}")

    # class methods and static methods
    @classmethod
    def adding_things(cls, num1, num2):
        return cls('teddy', num1+num2)

    @staticmethod
    def adding_things(num1, num2):
        return num1+num2

    def speak(self):
        print(f"hi! nice to meet you. I'm {self.name}")


player1 = Player('cydni', 23)
player2 = Player('ope', 45)

print(player1.name)  # how to access your attributes
print(player2.name)
player1.shoutout()

print(Player.adding_things(3, 7))

# the above illustrate encapsulation

"""
four pillars of oop:
1. encapsulation
2. abstraction
3. inheritance
4. polymorphism
"""
# abstraction
"""
hiding away info and having acess to only what the user requires
in python, to make class attributes private, put an _ in front of their name
"""

# inheritance
"""
allows new objects to asume the props of existing objects
"""


class User:
    def signin(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"attacking the enemy with {self.power} powers")


class Archar(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def attack(self):
        print(f"attacking the enemies with {self.arrows} arrows")


wiz = Wizard("ted", 69)
arch = Archar('jon', 33)
# isinstance(instamce, class)
print(isinstance(wiz, object))  # True
wiz.signin()

# Polymorphism
"""
many forms --> poly morphism
e.g having the same method name for diff classes
"""
for i in [wiz, arch]:
    i.attack()


# EXERCISE
# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats


# 2 Create a function that finds the oldest cat


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2

class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# Instantiate the Cat object with 3 cats
peanut = Cat("Peanut", 3)
garfield = Cat("Garfield", 5)
snickers = Cat("Snickers", 1)


# Find the oldest cat
def get_oldest_cat(*args):
    return max(args)


# Output
print(
    f"The oldest cat is {get_oldest_cat(peanut.age, garfield.age, snickers.age)} years old.")


# OBJECT INTROSPECTION
# ability to determine the type of an object at runtime(when the code is running)
print(dir(wiz))  # prints all the methods and attributes available to an object


# DUNDER METHODS
