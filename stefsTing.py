import tweepy
import sys
import re
# Twitter API credentials
# You need to go to https://apps.twitter.com/ to get your own keys for this script
# to function
consumer_key = "6pmQIyPl8zUDysbGcWtzvEumf"
consumer_secret = "LBL97jh7O0V7Hh3oOeogZ5t1DWUy1idnPbIKUt6isewcyfVeIi"
access_key= "1046797250301763586-J6O0EjmFY9nkIWGoDISMiM64FWNaEL"
access_secret = "qBEsWvFHJpLRgQ24oZ9EPVJ8eMFkEz7y3QopzQ6nnt07H"

def clean_tweet(tweet):
    tweet = re.sub("https?://", "", tweet)   #links
    tweet = re.sub("#\S+", "", tweet)           #hashtags
    tweet = re.sub(".?@", "", tweet)           #at mentions
    tweet = re.sub("RT.+", "", tweet)           #Retweets
    tweet = re.sub("Video:", "", tweet)        #Videos
    tweet = re.sub("\n", "", tweet)             #new lines
    tweet = re.sub("&", "and", tweet)       #encoded ampersands
    return tweet

def get_tweets(user_name):
	# Authorize twitter API and initialize tweepy
	authorization = tweepy.OAuthHandler(consumer_key, consumer_secret)
	authorization.set_access_token(access_key, access_secret)
	api_handle = tweepy.API(authorization)
	
	# Holds all the returned tweets for a user
	list_of_tweets = []
	
	# Gets the most 200 recent tweets; 200 is the max at one time
	try:
		list_of_tweets = api_handle.user_timeline(user_name,count=200,tweet_mode="extended")
	except tweepy.TweepError as error:
		print("An error has occurred: ", error)
		return

	# This file will store the user's tweets. It will be named with their username.
	filename = "textfiles/"+ user_name + ".csv"
	file = open(filename, 'w', encoding="utf-8")
	
	# These lines do several things: It first gets the next tweet from the list. 
	# It then replaces any new line characters in the string with spaces. This prevents our generator
	# from interpreting a new line in the same tweet as a its own tweet. It then removes any white
	# spaces at the start or end of the string. The line is then written to output file.
	# A new line is then added to the end of every tweet in the file.
	for x in range (0, len(list_of_tweets)):
		file.write(clean_tweet(list_of_tweets[x].full_text.replace('\n'," ").strip()))
		file.write(",\n")
		
	file.close()

if __name__ == '__main__':
	if len(consumer_key) == 0 or len(consumer_secret) == 0 or len(access_key) == 0 or len(access_secret) == 0:
		print("You must provide Twitter API keys for this script to work!")
		exit()
	
	if len(sys.argv) == 2 and len(str(sys.argv[1])) > 1:
		user_name = str(sys.argv[1])
		
		# Remove the leading '@' if it is present in the user name
		if sys.argv[1][0] == '@':
			get_tweets(user_name[1:])
		else:
			get_tweets(user_name)
			
		exit()
	else:
		print("Didn't receive user name as argument!")
		exit()