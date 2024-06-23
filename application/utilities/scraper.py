from bs4 import BeautifulSoup
import requests, re

def get_elements (url):
    try:
        html = requests.get(url).text
        exp = r'(\w+)-""'

        html = re.sub(exp, r'\1=""', html)
        return BeautifulSoup(html, "html.parser")
    except Exception as error:
        print (error)
        return False