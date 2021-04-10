mystring = "hello"
mylist = []
for i in mystring:
    mylist.append(i)
print(mylist)

# list comprehension
mylist2 = [param for param in mystring]
print(mylist2)

"""
formula for list comprehension

[expression-with-param for param in iterable]
"""
numlist = [num for num in range(0, 100)]
numlist2 = [num*2 for num in range(0, 100)]
print(numlist2)
