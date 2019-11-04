"""

Created by aditya on 2/11/18 at 1:27 AM

"""

n = int(input())

count = 0
i = 1

while count != n:

    i += 1
    for x in range(2, int(i / 2) + 1):

        if i % x == 0:
            break

    else:
        print(i, end=' ')
        count += 1
