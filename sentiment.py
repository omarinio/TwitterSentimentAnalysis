from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
import json
import polSent as ps

with open("tweets.json") as json_file:
    data = json.load(json_file)
    listoftexts = [data[user][0]['text'] for user in data]
    vss = ps.analyse(listoftexts)
    i=0

    for i in range(0, vss.shape[0]):
        print(vss['tweet'][i])
        print(vss['score'][i])
        print("\n")
        print("\n")
    

    