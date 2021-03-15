print(type(int(3)))


class BigObject:
    pass


obj1 = BigObject()  # instantiating the class and creating a new object

print(type(obj1))


class Player:
    def __init__(self, name, age):
        self.name = name  # attributes
        self.age = age

    def run(self):
        print('run')


player1 = Player('cydni', 23)
player2 = Player('ope', 45)

print(player1.name)  # how to access your attributes
print(player2.name)
