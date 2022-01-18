from bs4 import BeautifulSoup as bs
from bs4.element import Comment
from tools import *
from vars import *
import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
sAnalyzer = SentimentIntensityAnalyzer()

def getArticleURLs(name):
    lastName = name.split()[-1]
    firstName = name.split()[0]
    uName = re.sub(' ', '+', name)

    benchmark = []

    sortedLinks = {
        siteNames[0]: [],
        siteNames[1]: [],
        siteNames[2]: [],
        siteNames[3]: [],
        siteNames[4]: [],
        siteNames[5]: []
    }
    links = []
    for sI in range(len(siteURLs)):
        url = siteURLs[sI]
        baseURL = "https://" + url.split('/')[2]
        html = get(url + uName)
        soup = bs(html, "html.parser")
        hrefs = soup.find_all(href=True)
        i = 0
        for h in hrefs:
            u = h["href"]
            if (firstName.lower() in u.lower() and lastName.lower() in u.lower()) and not "search" in u.lower():
                if "https://" not in u:
                    u = baseURL + u
                if u not in links:
                    links.append(u)
                    i += 1
        sortedLinks[siteNames[sI]] = links
        links = []
        print (i)
        benchmark.append(i)
    return sortedLinks 

def tagVisible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def textFromHtml(body):
    soup = bs(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tagVisible, texts)  
    return u" ".join(t.strip() for t in visible_texts)

def analyze(url):
    html = get(url)
    text = textFromHtml(html)
    return sAnalyzer.polarity_scores(text)

def benchmark(name):
    lastName = name.split()[-1]
    firstName = name.split()[0]
    uName = re.sub(' ', '+', name)

    benchmark = []

    sortedLinks = {
        siteNames[0]: [],
        siteNames[1]: [],
        siteNames[2]: [],
        siteNames[3]: [],
        siteNames[4]: [],
        siteNames[5]: []
    }
    links = []
    for sI in range(len(siteURLs)):
        url = siteURLs[sI]
        baseURL = "https://" + url.split('/')[2]
        html = get(url + uName)
        soup = bs(html, "html.parser")
        hrefs = soup.find_all(href=True)
        i = 0
        for h in hrefs:
            u = h["href"]
            if (firstName.lower() in u.lower() and lastName.lower() in u.lower()) and not "search" in u.lower():
                if "https://" not in u:
                    u = baseURL + u
                if u not in links:
                    links.append(u)
                    i += 1
        print (i)
        benchmark.append(i)
    return benchmark 