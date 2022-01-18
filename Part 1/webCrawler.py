import requests
import pandas as pd
import htmlParser
from ratelimit import limits, sleep_and_retry

#limits rate to 1 request every 2 seconds. 
@sleep_and_retry
@limits(1,2)
def get(url):
    print ("Requested: " + url)
    return requests.get(url).text    

#the list of urls for all the presidents and vice presidents
#you can think of these urls as a folder that contains the urls for individual presidents
startingURLs = [
    "https://en.wikipedia.org/wiki/Category:21st-century_presidents_of_the_United_States",
    "https://en.wikipedia.org/wiki/Category:21st-century_vice_presidents_of_the_United_States",
    "https://en.wikipedia.org/wiki/Category:20th-century_presidents_of_the_United_States",
    "https://en.wikipedia.org/wiki/Category:20th-century_vice_presidents_of_the_United_States",
    "https://en.wikipedia.org/wiki/Category:19th-century_presidents_of_the_United_States",
    "https://en.wikipedia.org/wiki/Category:19th-century_vice_presidents_of_the_United_States", 
    "https://en.wikipedia.org/wiki/Category:18th-century_presidents_of_the_United_States",
    "https://en.wikipedia.org/wiki/Category:18th-century_vice_presidents_of_the_United_States"
]


#extract all the urls from the starting lists
categoryURLs = []

for url in startingURLs:
    categoryhtml = get(url)
    categoryURLs.append(htmlParser.extractLinks(categoryhtml))

#get rid of any duplicates as many presidents were vice presidents at some point
filteredURLs = []

for category in categoryURLs:
    for url in category:
        if url not in filteredURLs:
            filteredURLs.append(url)

#create dataframe
df = pd.DataFrame()

#for each president url extract the biodata and append it to the dataframe
for url in filteredURLs:
    html = get(url)
    df = df.append(htmlParser.getBioData(html))

#convert dataframe to csv file
df.to_csv("U.S. President Biodata.csv")
