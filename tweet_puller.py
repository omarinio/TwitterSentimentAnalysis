import tweepy
from tweepy import *
import pandas as pd
import csv
import re 
import string
import preprocessor as p
from keys import *

# def clean_tweet(tweet):
#     tweet = re.sub(b"https?://", b"", tweet)   #links
#     tweet = re.sub(b"#\S+", b"", tweet)           #hashtags
#     tweet = re.sub(b".?@", b"", tweet)           #at mentions
#     tweet = re.sub(b"RT.+", b"", tweet)           #Retweets
#     tweet = re.sub(b"Video:", b"", tweet)        #Videos
#     tweet = re.sub(b"\n", b"", tweet)             #new lines
#     tweet = re.sub(b"&", b"and", tweet)       #encoded ampersands
#     return tweet

def clean_tweet(tweet):
    return " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", tweet).split())
 
def get_tweets():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    
    api = tweepy.API(auth,wait_on_rate_limit=True)
    
    csvFile = open('falo.csv', 'a')
    csvWriter = csv.writer(csvFile)
    
    search_words = "US Election -filter:retweets"      # enter your words
    
    for tweet in tweepy.Cursor(api.search,q=search_words,
                            lang="en",
                            since_id=0,
                            tweet_mode="extended").items(1):
        new_tweet = clean_tweet(tweet.full_text)
        #csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'),tweet.user.screen_name.encode('utf-8'), tweet.user.location.encode('utf-8')])
        csvWriter.writerow([new_tweet])

if __name__ == '__main__':
	get_tweets()
    

