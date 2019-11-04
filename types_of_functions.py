"""

Created by ADITYA.SHETTY on 7/26/2018
 
"""

'''
# Default Argument Values
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in 'yes':
            return True
        if ok in 'nope':
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


ask_ok('Your Choice: ', 1, 'try it again')

-------------------------------------------------------------------------------

i = 5


def f(arg=i):
    print(arg)


i = 6

f()

------------------------------------------------------------------------------

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


print(f(1))
print(f(2))
-------------------------------------------------------------------------------

# yield vs return

# yield
def createGenerator(n):
    for i in range(n):
        yield i * i


a = createGenerator(3)
for i in a:
    print(i)

# return
def func(n):
    for i in range(n):
        return i * i


a = func(3)
print(a)
-------------------------------------------------------------------------------

# sort method
a = ['one','two', 'three','four']
a.sort()
print(a)
-------------------------------------------------------------------------------

# lambda expressions
def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
print(f(2))

string = 'abc'
string_reversal_func = lambda a:a[::-1]
print(string_reversal_func(string))
------------------------------------------------------------------------------
'''
