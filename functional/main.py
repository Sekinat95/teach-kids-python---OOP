"""
functional programmin: separationm of concerns
each part concerms itself with one thing its good at
contrast to oop, here we separate methods and attributes --> pure functions"""

# PURE FUNCTIONS
"""
1. whenever we give an input to this function, an operation is perfromed such that 
a defined behaviour happens each time the ficntion is called e.g inputting [1,3] to 
a doubling functon wil always result in [2, 6]

2. a function should not produce any side effects --> no unintended behaviours wrt to the outside world
"""
# examples

# parse

# yes, a pure func


def multiplyBy2_(list1):
    new_list = []
    for i in list1:
        i = i*2
        new_list.append(i)
    return new_list


print(multiplyBy2_([1, 2]))


def multiplyBy2(list1):
    new_list = []
    for i in list1:
        i = i*2
        new_list.append(i)
    # becasue the print intercats with the outside world
    return print(new_list)


multiplyBy2([1, 3])
# is this a pure function?? no

new_list_ = []

# no


def multiplyBy2__(list1):

    for i in list1:
        i = i*2
        # becasue the print intercats with the outside world
        new_list_.append(i)

    return new_list
