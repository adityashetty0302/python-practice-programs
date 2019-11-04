# Task 1
#
# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
# and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.


def first_last(ip_list):
    op_list = []
    op_list.append(ip_list[0])
    op_list.append(ip_list[-1])

    return op_list


input_list = [5, 10, 15, 20, 25]  # Any list can be taken
output_list = first_last(input_list)
print(output_list)
