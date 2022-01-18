from math import nan
import pandas as pd
import htmlParser
from tools import *
from vars import *
import random

presidentScores = []
for president in presidentNames:
    dictURLs = htmlParser.getArticleURLs(president)
    dictScores = {
        siteNames[0]: 0,
        siteNames[1]: 0,
        siteNames[2]: 0,
        siteNames[3]: 0,
        siteNames[4]: 0,
        siteNames[5]: 0
    }
    for siteName, urls in dictURLs.items():
        if len(urls) != 0:
            for u in urls:
                score = htmlParser.analyze(u)["compound"]
                dictScores[siteName] += score
                print (score)
            dictScores[siteName] = round(dictScores[siteName] / len(urls), 2)
        else:
            dictScores[siteName] = nan

    presidentScores.append(dictScores)

df = pd.DataFrame(presidentScores, index=presidentNames)
df.to_csv("media sentiment by president.csv")
