"""

Created by aditya on 28/10/18 at 6:20 PM

"""

'''
a = [1, 2, 3, 4, 5]
a=a[::-1]
print(a)
'''

'''
a = [1, 2, 3, 4, 5]
b=[]
for i in range(len(a)-1, -1, -1):
    b.append(a[i])
print(b)
'''

'''
a = [1, 2, 3, 4, 5,6]
n = len(a)
m = int(n / 2)
for i in range(0, m):
    a[i], a[n - 1 - i] = a[n - 1 - i], a[i]

print(a)
'''

a = [1, 2, 3]
a.reverse()
print(a)
