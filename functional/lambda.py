"""
used when we only need to use a fucntion once
they are anonymous fucntions

lambda functions are used with higher functuons
"""
# lambda data: return action on data
from functools import reduce

# parse


def multiplyBy2_(item):
    return item*2


print(list(map(multiplyBy2_, [1, 3])))

# doing the same thing with a lambda fucn

print(list(map(lambda item: item*2, [1, 3])))


# filter
def checkOdd(item):
    return item % 2 == 1


print(list(filter(checkOdd, [1, 3, 4, 6])))

print(list(filter(lambda item: item % 2 == 1, [1, 3, 4, 6])))


# REDUCE
mylist = [1, 2, 3]


def accumulator(acc, item):
    return acc + item


print(reduce(accumulator, mylist, 0))
print(reduce(lambda acc, item: acc+item, mylist, 0))
