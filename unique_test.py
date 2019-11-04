"""

Created by aditya on 25/12/18 at 4:55 PM

"""


class UniqueNumbers:

    @staticmethod
    def find_unique_numbers(numbers):
        # u_list = []
        # nu_list = list(set(numbers))
        # n = len(numbers)
        # for i in range(0,n-1):
        #     for j in range(i+1, n):
        #         if numbers[i] == numbers[j]:
        #             break
        #
        #     else:
        #         u_list.append(numbers[i])
        #
        # print(set(u_list))

        nu_list = list(set(numbers))
        u_list = []
        gen = (x for x in nu_list)
        for i in gen:
            if numbers.count(i) == 1:
                u_list.append(i)

        return u_list


print(UniqueNumbers.find_unique_numbers([1, 2, 1, 3]))

'''
use one liner (set) (list comprehension - if/else)
'''
