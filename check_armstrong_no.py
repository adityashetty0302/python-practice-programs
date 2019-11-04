"""

Created by aditya on 3/11/18 at 1:05 AM

"""

num = int(input())
o = len(str(num))

sum = 0
temp = num

while temp > 0:

    digit = temp % 10
    sum += digit ** o
    temp //= 10

if num == sum:
    print('Armstrong no.')
else:
    print('Not a Armstrong no.')
