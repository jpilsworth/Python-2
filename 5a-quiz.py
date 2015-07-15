'''
Q1.
 What is the type of the parameter for a mouseclick handler?
'''

''' 
A1.
Tuple
'''

'''
Q2.
Which of the following expressions mutate, i.e., change, list my_list?
'''

'''
A2.
my_list.append(10) 	Yes
my_list.extend([10, 20])	Yes	
another_list.extend(my_list)	No - This mutates another_list, not my_list.
my_list + [10, 20]	No	
my_list.reverse()	Yes
'''

'''
Q3.
We want to remove the element at the front of a list. For example, we want the following code to print "apple" and ["pear", "blueberry"], respectively. What function or method call should replace the question marks?
''' 

fruits = ["apple", "pear", "blueberry"]
fruit = fruits.pop(0)
print fruit, fruits 

'''
Q4.
Which of the following uses of range() will generate the list [2, 5, 8, 11, 14]?
'''

range(2, 17, 3)

'''
Q5.
To correctly compute the product of a list numbers of numbers, what statement should replace the question marks?

numbers = …
???
for n in numbers:
    product *= n
'''

numbers = [1, 7, 8, 19, 21]
product = 1
for n in numbers:
    product *= n
    print product

'''
Q6.
We can loop over strings, too!

The following incomplete function is a simple, but inefficient, way to reverse a string. What line of code needs to replace the questions marks for the code to work correctly?

def reverse_string(s):
    """Returns the reversal of the given string."""
    ???
    for char in s:
        result = char + result
    return result

print reverse_string("hello")
'''

def reverse_string(s):
    """Returns the reversal of the given string."""
    result = ""
    for char in s:
        result = char + result
    return result

print reverse_string("hello")

'''
Q7.
Imagine a game on a map. At the beginning, we might want to randomly assign each player a starting point. Which of the following expressions may we use in place of the question marks to correctly implement this functionality?

import random

def random_point():
    """Returns a random point on a 100x100 grid."""
    return (random.randrange(100), random.randrange(100))

def starting_points(players):
    """Returns a list of random points, one for each player."""
    points = []
    for player in players:
        point = random_point()
        ???
    return points
'''

import random

def random_point():
    """Returns a random point on a 100x100 grid."""
    return (random.randrange(100), random.randrange(100))

def starting_points(players):
    """Returns a list of random points, one for each player."""
    points = []
    for player in players:
        point = random_point()
        points.append(point)
    return points

'''
Q8.
The following function is supposed to check whether the given list of numbers is in ascending order. For example, we want is_ascending([2, 6, 9, 12, 400]) to return True, while is_ascending([4, 8, 2, 13]) should return False.

def is_ascending(numbers):
    """Returns whether the given list of numbers is in ascending order."""
    for i in range(len(numbers)):
        if numbers[i+1] < numbers[i]:
            return False
    return True
However, the function doesn't quite work. Try it on the suggested tests to verify this for yourself. The easiest fix is to make a small change to the highlighted code. What should it be replaced with?
'''

def is_ascending(numbers):
    """Returns whether the given list of numbers is in ascending order."""
    for i in range(len(numbers) - 1):
        if numbers[i+1] < numbers[i]:
            return False
    return True

'''
Question Explanation

Note that here we loop not over numbers, but over a new list, a range of indices. This function uses that approach because it looks at two elements of numbers on each iteration.
'''

'''
Q9.
Turn the following English description into code:

Create a list with two numbers, 0 and 1, respectively.
For 40 times, add to the end of the list the sum of the last two numbers.
What is the last number in the list?

To test your code, if you repeat 10 times, rather than 40, your answer should be 89.
'''

l = [0, 1]
for i in range(2, 42):
    l.append(l[i-2] + l[i-1])
    print i

print l

