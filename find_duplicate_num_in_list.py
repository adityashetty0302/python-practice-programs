"""

Created by aditya on 28/10/18 at 3:32 PM

"""

a = [0, 1, 0, 2, 4, 5, 5, 4, 6, 2, 1, 4, 3, 77, 9, 77, 8, 5]
dup = []
n = len(a)
for i in range(0, n-1):
    for j in range(i + 1, n):
        if a[i] == a[j]:
            dup.append(a[i])

print(list(set(dup)))
