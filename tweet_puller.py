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

def clean_tweet(tweet):
    return " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", tweet).split())
 
def get_tweets():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    
    api = tweepy.API(auth,wait_on_rate_limit=True)
    
    csvFile = open('falo.csv', 'a')
    csvWriter = csv.writer(csvFile)
    
    search_words = "Election Trump -filter:retweets"      # enter your words
    
    for tweet in tweepy.Cursor(api.search,q=search_words,
                            lang="en",
                            since_id=0,
                            tweet_mode="extended").items(1):
        tweet_info = {
            "username": tweet.user.screen_name,
            "tweet": {
                        "user_name": tweet.user.name,
                        "created_at": str(tweet.created_at),
                        "text": tweet.full_text,
                        "user_location": tweet.user.location,
                        "user_followers_count": tweet.user.followers_count,
                        "user_created_at": str(tweet.user.created_at),
                        "favourite_count": tweet.favorite_count,
                        "retweet_count": tweet.retweet_count
            }
        }
        y = json.dumps(tweet_info)
        print(y)
        # new_tweet = clean_tweet(tweet.full_text)
        # #csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'),tweet.user.screen_name.encode('utf-8'), tweet.user.location.encode('utf-8')])
        # csvWriter.writerow([new_tweet])

if __name__ == '__main__':
	get_tweets()
    

