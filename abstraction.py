
"""
hiding away info and having acess to only what the user requires
e.g. list.count() is accessible to the user. but he doesnt have to know how ist implemeted underneathe

in python, to make class attributes private, put an _ in front of their name
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


# from the definition of abstraction, it looks like we can just do...
Player = PlayerClass('teddy', 90)
Player.name = 'vince'
player.age = 19

# this is bad. because it means without knowing the underlying code , anotther person can just come and chnge what I've worked on
"""
to avoid this, we use private and public vars
publis vars --> all the ways we've initialised vars so far
private vars __> initialising vars with _ in front of names
_name
_age
this lets other programmers know not to chnage these variables because they are private
other programming languages have better ways of managing this with the private and public keywords
"""
list1 = [1, 2]
list1.append(3)
