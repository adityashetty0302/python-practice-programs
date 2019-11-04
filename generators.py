"""

Created by aditya on 12/11/18 at 7:48 AM

"""

'''
mygenerator = (x*x for x in range(3))
for i in mygenerator:
    print(i)
'''

def create_generator():

    for i in range(0, 10):
        yield i*i


mygenerator = create_generator()

for i in mygenerator:
    print(i)