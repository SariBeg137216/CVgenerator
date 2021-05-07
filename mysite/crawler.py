import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.google.com/')

text = page.text
# print(text)

soup = BeautifulSoup(text, 'html.parser')
# print(soup)
# print(soup.find_all('a'))
for link in soup.find_all('a'):
    link_address = link.get('href')
    link_name = link.string
    print("{}----->{}".format(link_name, link_address))
    # print(link)
