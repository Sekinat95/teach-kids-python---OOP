from functools import reduce

# 1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

# name = "geeks FOR geeks"
# print(name.capitalize())

print(list(map(lambda x: x.capitalize(), my_pets)))

# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]

print(list(zip(my_strings, my_numbers)))
new_list = list(zip(my_strings, my_numbers))

new_list.sort(key=lambda x: x[1])
# remember sort takes two arguments: reverse(a true or false value), key(a fucntion). How do I know this? google ofcourse

print(new_list)


# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
