import tweepy
from tweepy import *
import pandas as pd
import csv
import re
import string
import preprocessor as p
import json
import jsonpickle
from keys import *

# https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/object-model/tweet
# created_at (str)
# full_text (str)
# user.location
# user.followers_count
# user.created_at
# user.name
# user.screen_name
# favorite_count
# retweet_count

# def clean_tweet(tweet):
#     return " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", tweet).split())

def clean_tweet(tweet):
    # retweet cleaning
    tweet = re.sub("RT @[\w]*:", '', tweet)
    # twitter handle removal
    tweet = re.sub("@[\w]*", '', tweet)
    # URL removal
    tweet = re.sub("https?://[A-Za-z0-9./]*", '', tweet)

    return tweet

def get_tweets():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)

    api = tweepy.API(auth,wait_on_rate_limit=True)

    # csvFile = open('falo.csv', 'a')
    # csvWriter = csv.writer(csvFile)

    search_words = "Election Biden -filter:retweets"      # enter your words

    total_tweets = 10000
    tweets_per_request = 1000

    for i in range (int(total_tweets / tweets_per_request)):
        tweets_pulled = {}
        j = 0
        for tweet in tweepy.Cursor(api.search,q=search_words,
                                lang="en",
                                since_id=0,
                                tweet_mode="extended").items(tweets_per_request):

            j += 1
            print(f"Tweet number: {j}/{tweets_per_request}")

            if tweets_pulled.get(tweet.user.screen_name) != None:
                tweets_pulled[tweet.user.screen_name].append({
                    "user_name": tweet.user.name,
                    "created_at": str(tweet.created_at),
                    "text": clean_tweet(tweet.full_text),
                    "user_location": tweet.user.location,
                    "user_followers_count": tweet.user.followers_count,
                    "user_created_at": str(tweet.user.created_at),
                    "favourite_count": tweet.favorite_count,
                    "retweet_count": tweet.retweet_count
                })
            else:
                tweets_pulled[tweet.user.screen_name] = [{
                    "user_name": tweet.user.name,
                    "created_at": str(tweet.created_at),
                    "text": clean_tweet(tweet.full_text),
                    "user_location": tweet.user.location,
                    "user_followers_count": tweet.user.followers_count,
                    "user_created_at": str(tweet.user.created_at),
                    "favourite_count": tweet.favorite_count,
                    "retweet_count": tweet.retweet_count
                }]

        with open(f'tweets/tweets{i}.json', 'w') as json_file:
            json.dump(tweets_pulled, json_file)
            print(f"File {i} saved")

if __name__ == '__main__':
	get_tweets()
