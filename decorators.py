'''
# Simple Example
def decorate_greet(func):
    def inner():
        print('decorated')
        func()

    return inner


@decorate_greet
def greet():
    print("hello")


greet()
'''

'''
# Decorators with arguments
import sys


def smart_divide(func):
    def inner(a, b):

        if b == 0:
            print("Whoops! cannot divide")

        else:
            return func(a, b)

    return inner


@smart_divide
def divide(a, b):
    print(a / b)


divide(5, 2)
'''

'''
# Multiple decorators
def hash(func):
    def inner(msg):
        print("#####################")
        func(msg)
        print('#####################')

    return inner


def star(func):
    def inner(msg):
        print("*********************")
        func(msg)
        print('*********************')

    return inner


@hash
@star
def pr(msg):
    print(msg)


pr('hello')
'''
