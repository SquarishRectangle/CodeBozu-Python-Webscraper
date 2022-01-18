import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

#read the raw csv
df = pd.read_csv("raw politico.csv", index_col=0)
#get the impact column since that's all we're analyzing 
impact = list(df["The Impact"])

#get the evaluation for each row
evals = []
for i in impact:
    evl = sia.polarity_scores(i)
    evals.append(evl)

#seperate the positive and negative evals
pos = []
neg = []
for e in evals:
    pos.append(round(e["pos"] * 100, 2))
    neg.append(round(e["neg"] * 100, 2))

#make csv about how positive it is
df["Positive Sentiment"] = pos
df.to_csv("Politico Positive Sentiment.csv")

#make csv with both positives and negatives
df["Negative Sentiment"] = neg
df.to_csv("Politico Both Sentiment.csv")

#make csv with only negatives
del df["Positive Sentiment"]
df.to_csv("Politico Negative Sentiment.csv")