import csv
import json
import tweepy
from keys import *
from states import *
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def read_csv(lines):
    data = {}

    with open('uselection_tweets_1jul_11nov.csv') as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        for tweet in reader:
            if line_count == 0:
                print(f'Column names are {", ".join(tweet)}')
                line_count += 1
            elif line_count <= lines:
                user_id = tweet[1:2]
                if data.get(user_id[0]) != None:
                    data[user_id[0]].append({
                        "created_at": tweet[0:1],
                        "from_user_id": tweet[1:2],
                        "to_user_id": tweet[2:3],
                        "language": tweet[3:4],
                        "retweet_count": tweet[4:5],
                        "party_name": tweet[5:6],
                        "tweet_id": tweet[6:7],
                        "sentiment_score": tweet[7:8],
                        "words": tweet[8:9],
                        "negative_sum": tweet[9:10],
                        "positive_sum": tweet[10:11]
                    })
                else:
                    data[user_id[0]] = [{
                        "created_at": tweet[0:1],
                        "from_user_id": tweet[1:2],
                        "to_user_id": tweet[2:3],
                        "language": tweet[3:4],
                        "retweet_count": tweet[4:5],
                        "party_name": tweet[5:6],
                        "tweet_id": tweet[6:7],
                        "sentiment_score": tweet[7:8],
                        "words": tweet[8:9],
                        "negative_sum": tweet[9:10],
                        "positive_sum": tweet[10:11]
                    }]
                line_count += 1
            elif line_count > lines:
                break

        print(f'Processed {lines} lines.')

        return data

def get_user_loc(user):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

    try:
        user_info = api.get_user(user_id=user)
        if (user_info.location != ""):
            user_loc = user_info.location
        else:
            user_loc = None
    except:
        user_loc = None
            
    
    return user_loc

def remove_null_locations(data):
    cleaned_data = {}
    i = 0
    for user in data:
        i += 1
        print(f"User {i}")
        user_loc = get_user_loc(user)
        if (user_loc != None):
            print(user_loc)
            for state_abbr, state_name in states.items():
                if (state_abbr in user_loc or state_name in user_loc):
                    for tweet in data[user]:
                        tweet['location'] = user_loc
                        if cleaned_data.get(user) != None:
                            print(">1 tweet from same user")
                            cleaned_data[user].append(tweet)
                        else:
                            cleaned_data[user] = [tweet]
       
    return cleaned_data

def write_json(cleaned_data):
    with open(f'tweets/cleaned_tweets.json', 'w') as json_file:
            json.dump(cleaned_data, json_file)

def read_json():
    try:
        with open("tweets/cleaned_tweets.json") as json_file:
            data = json.load(json_file)
    except:
        print("Could not read JSON file")
    
    return data

def get_sentiment_val(state_abbr, state_name, data):
    dem_tweets = 0
    dem_positive = 0
    dem_negative = 0 
    dem_neutral = 0
    dem_swing = None
    rep_tweets = 0
    rep_positive = 0
    rep_negative = 0 
    rep_neutral = 0
    rep_swing = None
    for user in data:
        for tweet in data[user]:
            if (state_abbr in tweet['location'] or state_name in tweet['location']):
                if (tweet['party_name'][0] == "Democrats"):
                    dem_tweets += 1
                    if (float(tweet['sentiment_score'][0]) > 0):
                        dem_positive += 1
                    elif (float(tweet['sentiment_score'][0]) < 0):
                        dem_negative += 1
                    else:
                        dem_neutral += 1
                elif (tweet['party_name'][0] == "Republicans"):
                    rep_tweets += 1
                    if (float(tweet['sentiment_score'][0]) > 0):
                        rep_positive += 1
                    elif (float(tweet['sentiment_score'][0]) < 0):
                        rep_negative += 1
                    else:
                        rep_neutral += 1
    if not (dem_tweets == 0 or rep_tweets == 0):
        dem_swing = (dem_positive - dem_negative) / (dem_tweets / 100)
        rep_swing = (rep_positive - rep_negative) / (rep_tweets / 100)
        tweets_from_loc = dem_tweets + rep_tweets                   
        print(f"{state_name}: {tweets_from_loc} tweets")
    else:
        print(f"{state_name}: No tweets")
    return dem_swing, rep_swing

if __name__ == "__main__":
    #This set of functions gets a certain number of tweets and cleans them based on user locations then writes to JSON
    """
    num_tweets = 10000
    data = read_csv(num_tweets)
    cleaned_data = remove_null_locations(data)
    write_json(cleaned_data)
    """
    #This set of functions reads the earlier produced JSON and produces a sentiment score for each party within each state
    data = read_json()

    for state_abbr, state_name in states.items():
        dem_swing, rep_swing = get_sentiment_val(state_abbr, state_name, data)
        print(f"Democrat swing: {dem_swing}")
        print(f"Republican swing: {rep_swing}")
    


            
