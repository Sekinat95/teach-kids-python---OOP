"""
HIGHER FUNCTIONS:
 they accept other functions as arguments
"""
#map, filter, zip, reduce

# MAP

# from functools import reduce
# # map() filter() zip() reduce()

"""
MAP: is a higher function that manipulates 
an itrable with a fucntion  and returns a new item at  each iteration 
"""


def shortFunct():
    return True


# def multiplyBy2(list1):
#     new_list = []
#     for i in list1:
#         i = i*2
#         new_list.append(i)
#     return new_list


def multiplyBy2(item):
    return item*2


"""
an example of where map might be useful:
1. when you are trying to generate an iterable from an exsiting one by altering the existing one in some way.
 e.g if the original iterable, in this case, a list is ==> [1,2,3]
 and I'm trying to generate a new list of all elements in the old list + 10
  
  simple algorithm for that is:
  1. get each item in the old list 
  2. add 10 to each of those items
  3. append to a new list the result of each of your addition

  ecpected result ==> [1+10, 2+10, 3+10] = [11, 12, 13]

"""
################


def sqrroot(item):
    import math
    return math.sqrt(item)


print(list(map(sqrroot, [25, 16, 9])))

"""
random locations  |  country

abuja                   ghana
cairo                   uae
london                  germany
khartoum                uk
accra                   nigeria
dubai                   sudan
berlin                  egypt
"""

"""
EX: map()

1. here you're given this iterable, a list ==> [4, 7, 11]
2. for each item in the list, subtract 5
3. return the new list. solve this question using the map() fucntion

#hint:
 create a small fucntion called subtractFive()
 then do this: map(subtractFive, [4, 7, 11])
"""

# #print(multiplyBy2([1, 3]))
# # returns the same thing as when we use the first func
# mylist = list()


# print(list(map(multiplyBy2, [2, 3, 5])))
# print(tuple(map(multiplyBy2, [2, 3, 5])))


# # FILTER


# def checkOdd(item):
#     return item % 2 == 1


# print(list(filter(checkOdd, [1, 3, 4, 6])))

# # ZIP
# mylist = [1, 2, 4]
# yourlist = [10, 20, 40]
# theirlist = [-1, -2, -4]
# # you can put any number of iterable you want
# print(list(zip(mylist, yourlist, theirlist)))


# # REDUCE
# #from functools import reduce

# def accumulator(acc, item):
#     return acc + item


# # func, iterable, init val
# print(reduce(accumulator, mylist, 0))  # ADDS up the items in [1,2,4] --> 7
