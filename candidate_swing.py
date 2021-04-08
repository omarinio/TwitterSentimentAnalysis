from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
from states import *
import json

analyzer = SentimentIntensityAnalyzer()
total_tweets = 0
tweets_from_loc = 0
no_loc_tweets = 0
usable_tweets = 0

with open("tweets/tweets0.json") as json_file:
    data = json.load(json_file)
    for state_abbr, state_name in states.items():
        tweets_from_loc = 0
        vader_positive = 0
        vader_negative = 0 
        vader_neutral = 0
        for user in data:
            for tweet in data[user]:
                total_tweets += 1
                if (state_abbr in tweet['user_location'] or state_name in tweet['user_location']):
                    tweets_from_loc += 1
                    vs = analyzer.polarity_scores(tweet['text'])
                    if (vs['compound'] > 0):
                        vader_positive += 1
                    elif (vs['compound'] < 0):
                        vader_negative += 1
                    else:
                        vader_neutral += 1
        usable_tweets += tweets_from_loc
        if not (tweets_from_loc == 0):
            vader_swing = (vader_positive - vader_negative) / (tweets_from_loc / 100)                
            print(state_abbr + " " + state_name)
            print(f"Total tweets from state: {tweets_from_loc}")
            print(f"Vader swing: {vader_swing}")

total_tweets /= 50
print(f"Total tweets: {total_tweets}")
print(f"Usable tweets: {usable_tweets}")
