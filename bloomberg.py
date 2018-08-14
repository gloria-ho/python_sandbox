# Scrape and display data from IRL
# No longer works due to violation of bloomberg's term of service

# import libraries
import urllib2
from bs4 import BeautifulSoup

# url
quote_page = 'http://www.bloomberg.com/quote/SPX:IND'

# query the website and return the html to the variable
page = urllib2.urlopen(quote_page)

# parse the html using BS and store in variable
soup = BeautifulSoup(page, 'html.parser')
print soup
# take the value of the name
name_box = soup.find('h1', attrs={'class': 'companyName__99a4824b'})
print name_box

# grab the text data
name = name_box.text #.strip()
print name

# get index price
price_box = soup.find('span', attrs={'class': 'priceText__1853e8a5'})
price = price_box.text
print price