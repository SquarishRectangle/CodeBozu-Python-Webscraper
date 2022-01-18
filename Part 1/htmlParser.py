from bs4 import BeautifulSoup as bs
import pandas as pd
import re

#base url as some hyperlinks only contain the directory part of the url
baseurl = "https://en.wikipedia.org"

#get the biodata from a html file
def getBioData(file):
    #convert the html file to a beautiful soup data structure
    html = bs(file, "html.parser")

    #get the name of the politician
    title = html.find("title").text
    politicianName = title[:-12]

    #find the infobox card
    card = html.find(class_="infobox-header").parent.parent

    #find the list of headers, labels, and data
    carddata = card.find_all(class_=["infobox-header", "infobox-label", "infobox-data"])

    #find the indexes of the headers
    headers = card.find_all(class_="infobox-header")
    headerindexes = []
    for h in headers:
        headerindexes.append(carddata.index(h))

    #use the indexes of the headers to sort them into boxes
    boxes = []
    for i in range(len(headerindexes) - 1):
        boxes.append(carddata[headerindexes[i]:headerindexes[i + 1]])
    boxes.append(carddata[headerindexes[-1]:])

    #initiate data and category lists
    politicianData = []
    categories = []
    #filter the boxes
    for box in boxes:
        #keep the personal details box
        if box[0].text == "Personal details":
            print ("Found " + box[0].text)
            #box zero is the header which we don't need anymore
            del box[0]
            #sort them into categories and data
            for i in range(len(box)):
                if i % 2 == 0:
                    categories.append(box[i].text)
                else:
                    politicianData.append(box[i].text)
        #keep any box that ends in president of the united states. and do the same thing to it
        elif box[0].text[-30:] == "President of the United States":
            print ("Found " + box[0].text)
            del box[0]
            for i in range(len(box)):
                if i % 2 == 0:
                    categories.append(box[i].text)
                else:
                    politicianData.append(box[i].text)

    #number duplicates in categories because pandas will throw a tantrum if we don't 
    cleanCategories = []
    for c in categories:
        if c not in cleanCategories:
            cleanCategories.append(c)
        else:
            i = 2
            while True:
                nc = c + str(i)
                if nc not in cleanCategories:
                    cleanCategories.append(nc)
                    break
                i += 1
            

    #make dataframe
    df = pd.DataFrame([politicianData], columns=cleanCategories, index=[politicianName])


    return df


#extracts links from the html pages that hold the list of presidents
def extractLinks(file):
    #convert html file to a beautiful soup file type
    html = bs(file, "html.parser")
    #find title
    title = html.find("title").text
    #delete the word "categories: " from the beginning and the word " - wikipedia" from the end
    title = title[9:-12]

    #find the list of presidents
    card = html.find(text="Pages in category \"" + title + "\"").parent.parent.find(class_="mw-content-ltr")
    #find the hyperlinks aka hrefs
    hrefs = card.find_all(href=True)

    #initiate list to append to later
    links = []

    #add the baseurl to the hrefs and return them
    for h in hrefs:
        links.append(baseurl + h["href"])
    
    return links
