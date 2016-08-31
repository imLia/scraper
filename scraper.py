import urllib2
import json
from bs4 import BeautifulSoup

def scrape(url):
  url = url
  soup = BeautifulSoup(urllib2.urlopen(url).read(), 'html.parser')
  movie_list = soup.find_all('div', class_='table-scrollable')

  for movie_container in movie_list:
      title = movie_container.find('table').find('tbody')

      print title

scrape('https://admindev.acommercedev.com/partner/')
