# many forms:
# ways in which object class can share the same methid name which can behave differenlty based on the class that calls them
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

for i in [wiz, arch]:
    i.attack()
