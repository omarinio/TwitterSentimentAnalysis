from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
import json

analyzer = SentimentIntensityAnalyzer()

with open("tweets.json") as json_file:
    data = json.load(json_file)
    for user in data:
        print(data[user][0]['text'])    
        vs = analyzer.polarity_scores(data[user][0]['text']) 
        print(vs)
        testimonial = TextBlob(data[user][0]['text'])
        print(testimonial.sentiment)