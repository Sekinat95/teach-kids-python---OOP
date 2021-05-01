"""
Here we're addressing how to write functions in python.
"""


# find the max of three numbers
def maxofThreeNums(num1, num2, num3):
    maxNum = max(num1, num2, num3)
    return maxNum


mylist = [8, 2, 3, 0, 7]
# find the sum of the elements in the list


def addListElements(list1):
    sumElem = 0
    for i in list1:
        #sumElem += i
        sumElem = i + sumElem

    return sumElem


print(addListElements(mylist))

# Qts 3
# Write a Python function to multiply all the numbers in a list. Sample List : (8, 2, 3, -1, 7)
mylist2 = [8, 2, 3, -1, 7]


def multiplyListElements(list1):
    total = 1
    for i in list1:

        #total *= i
        total = i * total

    return total


print(multiplyListElements(mylist2))

# Qts 3c&d
# c. Write a Python function to subtract all the numbers in a list. Sample List : (8, 2, 3, -1, 7)
# d. Write a Python function to divide all the numbers in a list. Sample List : (8, 2, 3, -1, 7)


def areaofRectangle(l, b):
    return multiplyTwoNums(l, b)


def nameOfFunction():
    # do something
    return result


def nameOfFunction(parsedInValue):
    # do something with the parsedInValue
    # get result of the action performed
    return result
