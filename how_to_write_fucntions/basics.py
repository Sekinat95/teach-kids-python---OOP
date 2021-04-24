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

        sumElem += i

    return sumElem


print(addListElements(mylist))


# find the area of a rectangle
# l * b


def areaofRectangle(l, b):
    return multiplyTwoNums(l, b)


def nameOfFunction():
    # do something
    return result


def nameOfFunction(parsedInValue):
    # do something with the parsedInValue
    # get result of the action performed
    return result
