"""

Created by ADITYA.SHETTY on 7/27/2018

"""
from collections import deque

'''
# List methods
a = [1, 2, 3, 4, 5]
a.append(6)
print(a)
b = [6, 7]
a.extend(b)
a = a + b
a.insert(0, 1)
a.remove(0)
a.pop(0)
a.clear()
index = a.index(3)
count = a.count(1)
a.reverse()
a.sort()
c = a.copy()
a.insert(0, 0)
print(c, a)
-------------------------------------------------------------------------------

queue = deque([1, 2, 3])
# queue.append(4)
# queue.appendleft(0)
first_element = queue.popleft()
print(first_element)
print(queue)
-------------------------------------------------------------------------------
# List Comprehensions

number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)

squares = list(map(lambda x: x ** 2, range(10)))
print(squares)

squares = [x ** 2 for x in range(10)]
print(squares)

num_greater_than_zero = [x for x in range(-5, 5) if x > 0]
print(num_greater_than_zero)

print(abs(-5))

vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
single_list = [x for elem in vec for x in elem]
print(single_list)

from math import pi

print(round(pi, 2))
-------------------------------------------------------------------------------
# Nested List Comprehensions

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

new_matrix = [[row[i] for row in matrix] for i in range(4)]
print(new_matrix)

new_matrix_with_func = list(zip(*matrix))
print(new_matrix_with_func)
-------------------------------------------------------------------------------
# Tuples

a = (1, 2, 3)
print(a)
x, y, z = a
print(y)
-------------------------------------------------------------------------------
# Set

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
print(type(basket))
a = set('abracadabra')
b = set('alacazam')
print(a & b)
c=set()
print(type(c))
-------------------------------------------------------------------------------
# Dictionary

color = {'red': 456, 'blue': 123}
color['green'] = 78798
del color['green']
print(color)
print(list(color))
print(dict([('apple', 100), ('banana', 200)]))
print(dict(apple=100, banana=200))
-------------------------------------------------------------------------------
# Looping Techniques

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

for i in reversed(range(0, 10)):
    print(i)
'''
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for fruit in sorted(set(basket)):
    print(fruit)
