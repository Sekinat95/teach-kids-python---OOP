print(type(int(3)))
myint = 4


class BigObject:
    pass


class Wheel:
    pass


class Engine:
    pass


class Body:
    pass


class Electronics:
    pass


vase = [1, 3, 5]
print(type(vase))

obj1 = BigObject()  # instantiating the class and creating a new object
obj2 = BigObject()

print(type(obj1))


class PlayerClass:
    # class object attributes(static)
    # constructor
    membership = True

    def __init__(self, name, age):
        # class attributes(dynamic)
        self.age = age
        self.name = name

    def getName(self):
        print(self.name)

    def sayHello(self):
        print(f'hello {self.name}')


playerclass1 = PlayerClass("dami", 3)
playerclass1.getName()
playerclass1.sayHello()
print(playerclass1.membership)
pl2 = PlayerClass('robot1', 0.7)

print("************************************")


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
    def adding_things_c(cls, num1, num2):
        """
        we can use it without even instantiating the class
        it can create an instance of the class
        they are not used as often
        """
        return cls('teddy', num1+num2)

    @staticmethod
    def adding_things(num1, num2):
        """
        cannot create instance of the class
        can be used withoht instantiating the class
        """
        return num1+num2

    def speak(self):
        print(f"hi! nice to meet you. I'm {self.name}")


player1 = Player('cydni', 23)
player2 = Player('ope', 45)

print(player1.name)  # how to access your attributes
print(player2.name)
player1.shoutout()

# calling classmethod without instantiting the class
print(Player.adding_things_c(3, 7))
# so...
player3 = Player.adding_things_c(3, 7)
print(player3.name)
print(player3.age)
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
cat1 = Cat("zuri", 0.25)
cat2 = Cat('lucky', 2)
cat3 = Cat('cat', 3)

# 2 Create a function that finds the oldest cat


def getOldestCat(*args):
    oldest = max(args)
    return oldest


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
var1 = 3
var2 = "pencils"
var3 = "quam"
bigVar = var3 + " has" + str(var1) + var2
bigVar1 = f'quam has {str(var1)} {var2}'
print(bigVar)
print(bigVar1)

print(
    f'The oldest cat is {getOldestCat(cat1.age,cat2.age,cat3.age)} years old')


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
class Toy():
    def __init__(self, color, age):
        self.age = age
        self.color = color

    def __str__(self):
        return f"{self.color}"

    def __len__(self):
        return 100


toy = Toy('blue', 1)
print(str(toy))  # same as below
print(toy.__str__())  # same as above
print(toy.__len__())
print(len(toy))


class Super_list(list):
    def __len__(self):
        return 1000


splist1 = Super_list()
print(splist1.__len__())
splist1.append(0)
print(splist1.__len__())
print(splist1[0])


# most programming langiages dont allow multiple inheritance

# method resolution order
print(Toy.mro())
