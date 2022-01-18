This is my project for the first CodeBozu Fellowship.

# report 
For Deliverable 0, before the project fully began, we did a writeup about the Ethics of Webscraping which taught us the rules and guidelines of responsible scraping before we actually started so we wouldn’t do anything stupid. 

# Part 1: Presidential Biodata
For Deliverable 1 of this project, we were tasked with collecting data from all the presidents and vice-presidents given several index pages where all the presidents and vice-presidents of a specific century are listed. Hereafter, whenever I say presidents, all politicians who have only served as vice-president are included as well. 
To achieve this, I first located and extracted all the Hypertext Reference links, hereafter referred to as href or hrefs, from the given index pages. Foreach page in the list of hrefs, I located the biography card and extracted all data about their presidency and personal details. Data pertaining to non-presidential offices were discarded because I did not feel that was relevant to this project. After extracting the data from all the presidents, I converted it into a Pandas DataFrame and exported it into a .csv (Comma Separated Values) file. 

For Deliverable 2 of this project, we were tasked to generate insights from the data. For my first insight, I tried to find how many politicians have served as both president and vice-president. To do this, I scanned the presidency column to find blanks or NaN’s (not a number) in order to identify the people who did not serve as president and rule them out. I then repeated that for the vice-presidency column. I found that only 15 politicians were both president and vice-president. For my second piece of insight, I tried to find how many presidents does not have spouses and or children. Using the same line of reasoning from above, I scanned the Spouse and Children column, only this time I included instead of excluded rows that returned NaN. I found that only 2 presidents did not have children and only 6 did not have spouses. 

# Part 2: Media Favorability 
For Deliverable 3 of this project, we were tasked with scraping one article from Politico summarizing 30 things that Donald Trump did during his Presidency and analyzing the sentiment of each of those 30 things to determine what this particular media outlet liked about trump and what they didn’t like. 
I achieved this by first splitting up the article into chunks, then grouping those chunks together into the 30 different things. Then I used Vader Sentiment’s Sentiment Intensity Analyzer to evaluate the text for each thing Donald Trump did. Then I created a DataFrame which includes the list of things, the text for each of the things, and the sentiment values for those text.  
For Deliverable 4 and 5 of this project, we were tasked with scraping and analyzing articles for at least 2 presidents, from at least 2 news sources and creating a heat map from it and then analyzing the produced heatmap for insights on media bias. 
My plan was to start with all 22 major news networks in the US according to Wikipedia, and all 79 presidents and from there, I would narrow down the list of networks and presidents depending on which of them yields the most amount of data, since generally speaking more data = greater accuracy. 
The first thing I did was to create a properly rate-limited request function, so I don’t get my IP address banned in the middle of doing this. Next I first manually found and recorded the base search URLs for all the news sites. (e.g., https://www.usatoday.com/search/?q=). Then foreach website I searched for all the presidents taking note to convert to all lowercase and change spaces to +’s to comply with standard URL practices (e.g., https://www.usatoday.com/search/?q=joe+biden). Then for each of those searches, I would find the list of all hrefs that contain the politician’s first and last names (e.g., https://www.usatoday.com/story/entertainment/tv/2022/01/16/snl-joe-biden-blames-everything-wrong-america-spider-man/6546983001/) and filter out those that merely take you to the second page of the search (e.g., https://www.usatoday.com/search/?q=joe+biden&page=2). After that, I took the number of good articles found for each president from each source and saved it into a benchmark csv file. From that, I took the top 6 websites and the top 15 presidents that gave me the greatest number of articles. Foreach link that those sites and presidents yielded, I put all of the visible text through the Sentiment Intensity Analyzer and took the compound score instead of only the positive or negative score. My reason for that is an article could be very emotionally loaded and be both very positive and very negative at the same time which would mean its not very biased overall but if I took only the positive or negative it will show up as very biased. Then I averaged the scores for each president-website combination to get the overall bias from each source for each president. Lastly I used Seaborn and Matplotlib to create a heatmap image. I tweaked some settings, including rotating the bottom labels by 45 degrees so they will fit, and changing the overall aspect ratio of the image so that the graph part (excluding the labels and legend) will be square. 
After examining the resulting heatmap, I discovered that although there are many extreme opinions of Trump and Pence, and that they have been called radicalizing forces many times, most of the news sites I analyzed seem to give them average to ok ratings. I also discovered that most news sites give out average to good ratings, with only TMZ and New Yorker having extreme negative views on some presidents. The two George Bushes seems to be well liked by everyone except the New Yorker who for some reason absolutely hates them. 

