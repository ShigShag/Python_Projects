import requests
from bs4 import BeautifulSoup

def get_soup_object(url):
    try:
        source = requests.get(url).text
        source = BeautifulSoup(source, "lxml")
        return source
    except:
        return None
