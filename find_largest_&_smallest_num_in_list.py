"""

Created by aditya on 28/10/18 at 4:40 PM

"""

import random

a = random.sample(range(0, 100), 10)
print(a)
g_num = a[0]
g2_num = a[0]
l_num = a[0]
l2_num = a[0]

for i in a:
    if i > g_num:
        g_num = i

    if (i > g2_num) and (i < g_num):
        g2_num = i

    if i < l_num:
        l_num = i

    if (i < l2_num) and (i > l_num):
        l2_num = i

print(g_num, g2_num, l_num, l2_num)
