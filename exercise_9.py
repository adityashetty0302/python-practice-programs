# Task 9

# Please write a binary search function which searches an item in a sorted list.
# The function should return the index of element to be searched in the list.


def binary_search(i_list, elem):
    first = 0
    last = len(i_list) - 1
    found = False

    while first <= last and not found:

        midpoint = (first + last) // 2

        if i_list[midpoint] == elem:
            found = True
            index = midpoint

        else:
            if elem < i_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    if found:
        return 'Item found at index %d' % index
    else:
        return 'Item not found'


ip_list = [10, 12, 18, 23, 56, 62]
op = binary_search(ip_list, 12)
print(op)
