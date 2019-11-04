# Task 6

# Write the Task 5 titles to the text file.

# Extras:
# Ask the user to specify the name of the output file that will be saved.

import requests
from bs4 import BeautifulSoup

f_name = str(input('Enter name of the output file \n'))
url = 'https://news.ycombinator.com/'
page = requests.get(url)
data = page.text
soup = BeautifulSoup(data, 'html.parser')
td_tags = soup.find_all('td', attrs={'class': 'title'})

with open(r'exercise_6_output/%s.txt' % f_name, 'a+') as f1:
    for td in td_tags:
        a_tag = td.find('a')
        if 'a' in str(a_tag):
            # print('---', a_tag.text)
            f1.write('\n--- ' + str(a_tag.text))
