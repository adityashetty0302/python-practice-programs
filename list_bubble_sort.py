"""

Created by aditya on 28/10/18 at 12:42 PM

"""
'''
# Normal Bubble sort
import random
import datetime


def bubble_sort(arr):
    n = len(arr)

    for i in range(0, n - 1):

        for j in range(0, n - 1 - i):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


t1 = datetime.datetime.now()
arr = random.sample(range(0, 100), 10)
print(arr)
bubble_sort(arr)
print(arr)
t2 = datetime.datetime.now()
print(t2 - t1)
'''

# Fast Bubble sort
import random
import datetime


def bubble_sort(arr):
    n = len(arr)

    for i in range(0, n - 1):
        swapped = False

        for j in range(0, n - 1 - i):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if swapped == False:
            break

    return arr


t1 = datetime.datetime.now()
arr = random.sample(range(0, 100), 10)
print(arr)
bubble_sort(arr)
print(arr)
t2 = datetime.datetime.now()
print(t2 - t1)
