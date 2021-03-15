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
    def adding_things(cls, num1, num2):
        return cls('teddy', num1+num2)


player1 = Player('cydni', 23)
player2 = Player('ope', 45)

print(player1.name)  # how to access your attributes
print(player2.name)
player1.shoutout()

print(Player.adding_things(3, 7))
