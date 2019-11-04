"""

Created by ADITYA.SHETTY on 8/1/2018

"""

# Fancier Output Formatting
'''
year = 2016 ; event = 'Referendum'
a = f'Results of the {year} {event}'
print(a)

b = 'Some string'
print(str(b))

# Manual String Formatting
for i in range(0, 11):
    print(i, i * i, i * i * i)

for x in range(1, 11):
    print(str(x).ljust(2), str(x * x).ljust(3), str(x * x * x).ljust(4))
    
print('123'.zfill(5))

value = ('the answer', 42)
print(str(value))
'''

# Saving structured data with json
import json

with open(r'D:\Aditya\Aditya\source\Practice\json_test.txt', 'a') as f:
    j = json.dumps([1, 'simple', 'list'])
    f.write(j)
