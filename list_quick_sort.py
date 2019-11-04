"""

Created by aditya on 29/10/18 at 8:51 PM

"""


def quickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)


def quickSortHelper(alist, low, high):
    if low < high:
        splitpoint = partition(alist, low, high)
        quickSortHelper(alist, low, splitpoint - 1)
        quickSortHelper(alist, splitpoint + 1, high)


def partition(alist, low, high):
    pivot_value = alist[low]
    leftmark = low + 1
    rightmark = high

    done = False

    while done == False:

        while leftmark <= rightmark and alist[leftmark] <= pivot_value:
            leftmark += 1

        while rightmark >= leftmark and alist[rightmark] >= pivot_value:
            rightmark -= 1

        if rightmark < leftmark:

            done = True

        else:

            alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]

    alist[rightmark], alist[low] = alist[low], alist[rightmark]
    return rightmark


a = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quickSort(a)
print(a)
