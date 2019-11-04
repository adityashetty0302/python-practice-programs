"""

Created by aditya on 28/10/18 at 6:45 PM

"""

a = [1, 2, 2, 5, 9, 9, 4, 7, 9, 2, 4, 6, 8, 10, 56, 42, 11, 3, 2, 9, 1]
f_list = []
for i in a:
    if i not in f_list:
        f_list.append(i)

print(f_list)

