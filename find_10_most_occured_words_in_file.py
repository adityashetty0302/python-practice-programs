'''Aditya'''

# Using Logic
'''
with open(r'D:\Aditya\asd.txt', 'r') as t:
    data = str(t.read())
    data = data.split()
    d = {k: [] for k in data}
    # print(d)
    for j in data:
        for i, x in d.items():
            if j == i:
                d[i].append(i)

    l2 = []
    flag = 0
    for k in range(20, 1, -1):
        for i, x in d.items():
            if len(d[i]) == k:
                l2.append(i)
                if len(l2) == 10:
                    flag = 1
                    break
        if flag == 1:
            break

    print(l2)
'''

# Using inbuilt functions
# Python program to find the k most frequent words
# from data set
from collections import Counter

data_set = "Welcome to the world of Geeks " \
           "This portal has been created to provide well written well" \
           "thought and well explained solutions for selected questions " \
           "If you like Geeks for Geeks and would like to contribute " \
           "here is your chance You can write article and mail your article " \
           " to contribute at geeksforgeeks org See your article appearing on " \
           "the Geeks for Geeks main page and help thousands of other Geeks. " \
 \
    # split() returns list of all the words in the string
split_it = data_set.split()

# Pass the split_it list to instance of Counter class.
Counter = Counter(split_it)

# most_common() produces k frequently encountered
# input values and their respective counts.
most_occur = Counter.most_common(4)

most_occur_list = [x[0] for x in most_occur]

print(most_occur, '\n', most_occur_list)
