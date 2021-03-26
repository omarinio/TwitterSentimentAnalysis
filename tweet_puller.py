import tweepy
from tweepy import *
import pandas as pd
import csv
import re 
import string
import preprocessor as p
from keys import *

def clean_tweet(tweet):
    tweet = re.sub(b"https?://", b"", tweet)   #links
    tweet = re.sub(b"#\S+", b"", tweet)           #hashtags
    tweet = re.sub(b".?@", b"", tweet)           #at mentions
    tweet = re.sub(b"RT.+", b"", tweet)           #Retweets
    tweet = re.sub(b"Video:", b"", tweet)        #Videos
    tweet = re.sub(b"\n", b"", tweet)             #new lines
    tweet = re.sub(b"&", b"and", tweet)       #encoded ampersands
    return tweet
 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
 
api = tweepy.API(auth,wait_on_rate_limit=True)
 
csvFile = open('US-Election-Data', 'a')
csvWriter = csv.writer(csvFile)
 
search_words = "US Election"      # enter your words
new_search = search_words + " -filter:retweets"
 
for tweet in tweepy.Cursor(api.search,q=new_search,count=100,
                           lang="en",
                           since_id=0).items(100):
    new_tweet = clean_tweet(tweet.text.encode('utf-8'))
    #csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'),tweet.user.screen_name.encode('utf-8'), tweet.user.location.encode('utf-8')])
    csvWriter.writerow([new_tweet])

