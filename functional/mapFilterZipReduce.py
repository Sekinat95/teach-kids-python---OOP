#map, filter, zip, reduce

# MAP


from functools import reduce


def multiplyBy2(list1):
    new_list = []
    for i in list1:
        i = i*2
        new_list.append(i)
    return new_list


def multiplyBy2_(item):
    return item*2


print(multiplyBy2([1, 3]))
# returns the same thing as when we use the first func
print(list(map(multiplyBy2_, [1, 3])))

# FILTER


def checkOdd(item):
    return item % 2 == 1


print(list(filter(checkOdd, [1, 3, 4, 6])))

# ZIP
mylist = [1, 2, 4]
yourlist = [10, 20, 40]
theirlist = [-1, -2, -4]
# you can put any number of iterable you want
print(list(zip(mylist, yourlist, theirlist)))


# REDUCE
#from functools import reduce

def accumulator(acc, item):
    return acc + item


# func, iterable, init val
print(reduce(accumulator, mylist, 0))  # ADDS up the items in [1,2,4] --> 7
