import csv
import tweepy
from keys import *

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

def get_user_loc(data):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)

    api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

    i = 0

    for user in data:
        i += 1
        try:
            user_info = api.get_user(user_id=user)
            #print(f"User {i}")
            if (user_info.location != ""):
                print(user_info.location)
            else:
                print("Empty location")
        except:
            print(f"User {i} suspended")


if __name__ == "__main__":
    num_tweets = 10
    data = read_csv(num_tweets)
    get_user_loc(data)