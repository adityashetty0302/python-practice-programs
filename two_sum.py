"""

Created by aditya on 24/12/18 at 9:57 PM

"""


class TwoSum:

    @staticmethod
    def find_two_sum(numbers, target_sum):
        """
        :param numbers: (list of ints) The list of numbers.
        :param target_sum: (int) The required target sum.
        :returns: (a tuple of 2 ints) The indices of the two elements whose sum is equal to target_sum
        """
        n = len(numbers)

        for i in range(0, n-1):

            for j in range(i + 1, n):

                result = numbers[i] + numbers[j]
                if result == target_sum:
                    return (i, j)
                    break

            if result == target_sum:
                break


print(TwoSum.find_two_sum([3, 1, 5, 7, 5, 9], 6))
