# lambda expression ex

print(list(map(lambda num: num**2, [1, 2, 3])))

a = [(0, 2), (5, 2), (9, 9), (10, -1)]
a.sort(key=lambda x: x[1])

# explanation:
"""
list.sort() takes in an argument key , a fucntion that descrobes the sorting criteria
remember lambda functions are anonymous functions that you intend to use only once. this
makes them fit in here for usage. 
so, in the solution, the sorting criteria indicates that the list should be sorted with each item of the second index in each tuple, 
x represents each item in each tuple.
"""

print(a)
