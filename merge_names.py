"""

Created by aditya on 25/12/18 at 1:58 PM

"""


class MergeNames:

    @staticmethod
    def unique_names(names1, names2):
        f_list = names1 + names2

        return list(set(f_list))


names1 = ["Ava", "Emma", "Olivia"]
names2 = ["Olivia", "Sophia", "Emma"]
print(MergeNames.unique_names(names1, names2))  # should print Ava, Emma, Olivia, Sophia
