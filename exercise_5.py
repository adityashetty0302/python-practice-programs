# Task 5
#
# Use the BeautifulSoup and requests Python packages to print out a list of all the news titles on the https://news.ycombinator.com/.


import requests
from bs4 import BeautifulSoup

url = 'https://news.ycombinator.com/'
page = requests.get(url)
data = page.text
soup = BeautifulSoup(data, 'html.parser')
td_tags = soup.find_all('td', attrs={'class': 'title'})

for td in td_tags:
    a_tag = td.find('a')
    if 'a' in str(a_tag):
        print('---', a_tag.text)
