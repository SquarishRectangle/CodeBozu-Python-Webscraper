from bs4 import BeautifulSoup as bs
from tools import *
from vars import *
import re

def getArticleURLs(name):
    lastName = name.split()[-1]
    firstName = name.split()[0]
    uName = re.sub(' ', '+', name)

    benchmark = []

    links = []
    for url in siteURLs:
        baseURL = "https://" + url.split('/')[2]
        html = get(url + uName)
        soup = bs(html, "html.parser")
        hrefs = soup.find_all(href=True)
        i = 0
        for h in hrefs:
            u = h["href"]
            if ((firstName.lower() in u.lower() and lastName.lower() in u.lower()) or "president" in u.lower()) and not "search" in u.lower():
                if "https://" not in u:
                    u = baseURL + u
                if u not in links:
                    links.append(u)
                    i += 1
        print (i)
        benchmark.append(i)

    return benchmark 