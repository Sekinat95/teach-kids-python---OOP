"""
allows new objects to asume the props of existing objects
"""


class User:
    def __init__(self, email):
        self.email = email

    def signin(self):
        print('logged in')

# parse


class Wizard(User):
    def __init__(self, name, power, email):
        User.__init__(self, email)
        self.name = name
        self.power = power

    def attack(self):
        print(f"attacking the enemy with {self.power} powers")

    def multiplyPower(self):
        return self.power * 10


class Archar(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def attack(self):
        print(f"attacking the enemies with {self.arrows} arrows")


wiz = Wizard("ted", 69, "wiz@gmail.com")
arch = Archar('jon', 33)
# isinstance(instamce, class)
print(isinstance(wiz, object))  # True
wiz.signin()
print(wiz.email)
