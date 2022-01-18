from bs4 import BeautifulSoup as bs
import pandas as pd
import requests

#read from website
html = requests.get("https://www.politico.com/news/magazine/2021/01/18/trump-presidency-administration-biggest-impact-policy-analysis-451479").text

#convert to soup
soup = bs(html, "html.parser")

#get list of labels
rLabels = soup.find_all(class_="story-text__heading-medium")
labels = []
for l in rLabels:
    labels.append(l.text)

#get paragraphs
rData = soup.find_all(text=["The move:", "The impact:", "The upshot:", "The upshot: "])
data = []
for d in rData:
    data.append(d.parent.parent.text)

#sort paragraphs into move impact and upshot
move = []
impact = []
upshot = []
for j in range(len(data) // 3):
    i = 3 * j
    move.append(data[i])
    impact.append(data[i + 1])
    upshot.append(data[i + 2])

#make dictionary with the three columns
dct = {
    "The Move": move,
    "The Impact": impact,
    "The Upshot": upshot
}

#create dataframe with the data, indexing with labels
df = pd.DataFrame(dct, index=labels)
#convert to csv
df.to_csv("raw politico.csv")