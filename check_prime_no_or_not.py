"""

Created by aditya on 2/11/18 at 1:18 AM

"""

n = int(input())

for x in range(2, int(n / 2) + 1):
    if n % x == 0:
        print(str(n) + ' is not a prime no.')
        break
else:
    # loop fell through without finding a factor
    print(n, 'is a prime number')
