"""
definition: the binding of data and fucntions that manipulate that data
"""

"""
encapsulation example
"""


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
