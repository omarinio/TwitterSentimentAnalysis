import csv
import json
import tweepy
from keys import *
from states import *
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def read_csv(lines):
    data = {}
    file_path = 'hashtag_donaldtrump.csv'
    with open(file_path, encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        print(csv_file)
        line_count = 0
        for tweet in reader:
            if line_count == 0:
                print(f'Column names are {", ".join(tweet)}')
                line_count += 1
            elif line_count <= lines:
                user_id = tweet[6:7]
                if user_id:
                    if data.get(user_id[0]) != None:
                        data[user_id[0]].append({
                            "created_at": tweet[0:1],
                            "tweet_id": tweet[1:2],
                            "tweet": tweet[2:3],
                            "likes": tweet[3:4],
                            "retweet_count": tweet[4:5],
                            "source": tweet[5:6],
                            "user_id": tweet[6:7],
                            "user_name": tweet[7:8],
                            "user_screen_name": tweet[8:9],
                            "user_description": tweet[9:10],
                            "user_join_date": tweet[10:11],
                            "user_followers_count": tweet[11:12],
                            "user_location": tweet[12:13],
                            "lat": tweet[13:14],
                            "long": tweet[14:15],
                            "city": tweet[15:16],
                            "country": tweet[16:17],
                            "continent": tweet[17:18],
                            "state": tweet[18:19],
                            "state_code": tweet[19:20],
                            "collected_at": tweet[20:21]
                        })
                    else:
                        data[user_id[0]] = [{
                            "created_at": tweet[0:1],
                            "tweet_id": tweet[1:2],
                            "tweet": tweet[2:3],
                            "likes": tweet[3:4],
                            "retweet_count": tweet[4:5],
                            "source": tweet[5:6],
                            "user_id": tweet[6:7],
                            "user_name": tweet[7:8],
                            "user_screen_name": tweet[8:9],
                            "user_description": tweet[9:10],
                            "user_join_date": tweet[10:11],
                            "user_followers_count": tweet[11:12],
                            "user_location": tweet[12:13],
                            "lat": tweet[13:14],
                            "long": tweet[14:15],
                            "city": tweet[15:16],
                            "country": tweet[16:17],
                            "continent": tweet[17:18],
                            "state": tweet[18:19],
                            "state_code": tweet[19:20],
                            "collected_at": tweet[20:21]
                        }]
                line_count += 1
            elif line_count > lines:
                break

        print(f'Processed {lines} lines.')

        return data

def remove_null_locations(data):
    cleaned_data = {}
    for user in data:
        for tweet in data[user]:
            user_state_code = tweet['state_code']
            user_state_name = tweet['state']
            if (user_state_name != None or user_state_code != None):
                for state_abbr, state_name in states.items():
                    if (state_abbr in user_state_code and state_name in user_state_name):
                        if cleaned_data.get(user) != None:
                            print(">1 tweet from same user")
                            cleaned_data[user].append(tweet)
                        else:
                            cleaned_data[user] = [tweet]

    return cleaned_data

def write_json(cleaned_data):
    try:
        with open('sentiment/avg_trump_swing_values.json', 'w') as json_file:
            json.dump(cleaned_data, json_file)
        print("Successfully wrote to JSON file")
    except Exception as e:
        print(e)

def read_json():
    try:
        with open("tweets/trump_cleaned_tweets.json") as json_file:
            data = json.load(json_file)
        print("Successfully read JSON file")
    except Exception as e:
        print(e)
    
    return data

def get_sentiment_val(state_abbr, state_name, data):
    tweets_from_loc = 0
    total_sentiment = 0
    positive = 0
    negative = 0
    neutral = 0
    swing = None

    analyzer = SentimentIntensityAnalyzer()

    for user in data:
        for tweet in data[user]:
            if (state_abbr in tweet['state_code'] or state_name in tweet['state']):
                vs = analyzer.polarity_scores(tweet['tweet'])
                tweets_from_loc += 1
                total_sentiment += vs['compound']
                """
                if (vs['compound'] > 0):
                    positive += 1
                elif (vs['compound'] < 0):
                    negative += 1
                else:
                    neutral += 1
                """
    if not (tweets_from_loc == 0):
        swing = total_sentiment / (tweets_from_loc)
        #swing = (positive - negative) / (tweets_from_loc)                  
        print(f"{state_name}: {tweets_from_loc} tweets")
    else:
        print(f"{state_name}: No tweets")
    return swing

if __name__ == "__main__":
    #This set of functions gets a certain number of tweets and cleans them based on user locations then writes to JSON
    trump_tweets = 971158
    biden_tweets = 777079
    test_tweets = 100
    
    """
    data = read_csv(trump_tweets)
    cleaned_data = remove_null_locations(data)
    write_json(data)
    """

    #This set of functions reads the earlier produced JSON and produces a sentiment score for each party within each state
    
    data = read_json()
    state_swing = {}

    for state_abbr, state_name in states.items():
        swing = get_sentiment_val(state_abbr, state_name, data)
        state_swing[state_abbr] = swing

    write_json(state_swing)

    
    


            
