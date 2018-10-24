from bs4 import BeautifulSoup
import requests

def getAllDestLink (link):
    destLinks = []
    try:
        req = requests.get(link)
        soup = BeautifulSoup(req.text, "lxml")
        prefix = "https://vi.wikipedia.org"
        for link in soup.find_all('a'):
            if(str(link.get('href')).startswith('/wiki')):
                destLink = prefix + link.get('href')
                destLinks.append(destLink)
    except:
        pass
    # destLinks.remove("")
    return  destLinks



# x =getAllDestLink('https://vi.wikipedia.org/wiki/Tổng_Bí_thư_Ban_Chấp_hành_Trung_ương_Đảng_Cộng_sản_Việt_Nam')
