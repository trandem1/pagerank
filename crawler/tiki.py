from bs4 import BeautifulSoup
import requests

def getContent (link):
    req = requests.get(link)
    soup = BeautifulSoup(req.text, "lxml")
    raw = soup.findAll('div',attrs = {"class":"shopee-product-rating__content"})
    print(raw)


getContent('https://tiki.vn/')