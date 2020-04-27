from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import datetime
from firebase import firebase

# website with the data
my_url = "https://www.stateofthenation.gov.za/"

# opens a connection, gets the html and closes it
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parser
page_soup = soup(page_html, "html.parser")

# scrape the 'tests conducted' value from the website
test_attr = page_soup.h3.text



