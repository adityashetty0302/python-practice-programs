"""

Created by ADITYA.SHETTY on 10/12/2018

"""

'''
class MyClass:
    """docstring"""

    i = 12

    def f(self):
        return 'hello world'


x = MyClass()
# print(x.__doc__)

xf = x.f
# print(xf())

x.i = 15
y = MyClass()
y.i = 18
# print(x.i, y.i)

# print(x.__class__)
# print(isinstance(x,MyClass))
# print(issubclass(bool,int))
# print(issubclass(int,int))
# print(issubclass(float,int))
'''

'''
class Number():

    def __init__(self, ip, rp):
        self.i = ip
        self.r = rp


x = Number(-4.5, 2)
print(x.i, x.r)
'''

'''
def f1(self, x, y):
    return min(x, x + y)


class C:
    f = f1


x = C()
print(x.f(1, 2))
'''

'''
# Inheritance
class Person:
    pass


class Student(Person):
    pass

print(issubclass(Student, Person))
'''

'''
# Single Inheritance
x = 0


class fruit:

    def __init__(self):
        global x
        x += 1
        print('fruit')


class citrus(fruit):

    def __init__(self):
        super().__init__()
        global x
        x += 2
        print('citrus')


print(x)
lime = citrus()
print(x)
'''

'''
# Multilevel Inheritance
class A():
    x = 1


class B(A):
    pass


class C(B):
    pass


c_obj = C()
print(c_obj.x)
'''

'''
# Hierarchical Inheritance
class A:
    pass


class B(A):
    pass


class C(A):
    pass


print(issubclass(B, A))
print(issubclass(C, A))
'''

'''
# Multiple Inheritance
class Color:
    pass


class Fruit:
    pass


class Orange(Color, Fruit):
    pass


print(issubclass(Orange, Color))
print(issubclass(Orange, Fruit))
'''

'''
# Hybrid Inheritance
class A:
    x = 1


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


d_obj = D()
print(d_obj.x)
'''

'''
# super() Function
class Vehicle:

    def start(self):
        print('start')

    def stop(self):
        print('stop')


class TwoWheeler(Vehicle):

    def say(self):
        super().start()
        print('2wheel')
        super().stop()


bike = TwoWheeler()
bike.say()
'''

'''
# Method Overriding
class A:

    def hi(self):
        print('In A')


class B(A):

    def hi(self):
        print('In B')


b_obj = B()
b_obj.hi()
'''

'''
# Method Overloading (Not supported in python)
def add(a, b):
    return a + b


def add(a, b, c):
    return a + b + c


add(2, 3)
'''

'''
# method overloading workaround --- 1
def add(*args):
    result = 0
    for i in args:
        result += i

    return result


print(add(1, 2, 1, 1))
'''

'''
# method overloading workaround --- 2
def add(a, b, c=0):
    if c is None:
        return a + b
    else:
        return a + b + c


print(add(1, 2, 3))
'''

'''
class Employee:
    pass


john = Employee()  # Create an empty employee record

# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000

print(john.name)
'''

# # print('line_1', end='')
# print('line_2')

# for i in range(5,1,-1):
#     print(i)

'''
# Generators
def rev(data):
    for i in range(len(data) - 1, -1, -1):
        yield data[i]


for char in rev('spam'):
    print(char)
'''

'''
# Generator Expressions
print(sum(i * i for i in range(10)))
print(list(i for i in range(10)))
'''
