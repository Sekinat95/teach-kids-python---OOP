class User:
    def __init__(self, email):
        self.email = email

    def signin(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(f"attacking the enemy with {self.power} powers")


class Archar(User):
    def __init__(self, name, arrows, email):
        super().__init__(email)
        self.name = name
        self.arrows = arrows

    def attack(self):
        print(f"attacking the enemies with {self.arrows} arrows")


wiz = Wizard("ted", 69, "my email")
arch = Archar('jon', 33, "arch emial")
# isinstance(instamce, class)
print(isinstance(wiz, object))  # True
wiz.signin()
print(wiz.email)
