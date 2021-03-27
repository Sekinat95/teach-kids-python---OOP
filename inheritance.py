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
