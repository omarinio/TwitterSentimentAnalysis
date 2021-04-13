from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
import json
import re
from collections import Counter
import wordcloud

# C:\Users\Omar\AppData\Local\Programs\Python\Python38\Lib\site-packages\vaderSentiment

def generate_word_cloud(word_list):
    wc = wordcloud.WordCloud(background_color='white', max_words=300, collocations=False, max_font_size=40, random_state=42)
    wc=wc.generate(" ".join(word_list).lower())
    # save the wordcloud
    wc.to_file('wordcloud.png')

def clean_tweet(tweet):
    # retweet cleaning
    tweet = re.sub("RT @[\w]*:", '', tweet)
    # twitter handle removal
    tweet = re.sub("@[\w]*", '', tweet)
    # URL removal
    tweet = re.sub("https?://[A-Za-z0-9./]*", '', tweet)
    tweet = re.sub("&", "and", tweet)

    return tweet

if __name__ == "__main__":
    analyzer = SentimentIntensityAnalyzer()
    pos = []
    neg = []
    with open("tweets/biden_cleaned_tweets.json") as json_file:
        data = json.load(json_file)
        for user in data:
            cleaned_tweet = clean_tweet(data[user][0]['tweet'][0])
            #print(cleaned_tweet)    
            vs = analyzer.polarity_scores(cleaned_tweet) 
            #print(vs)
            for word in cleaned_tweet.split(' '):
                word = word.replace('\n', ' ').replace('\xa0',' ').replace('.',' ').replace('·', ' ').replace('•',' ').replace('\t', ' ').replace(',',' ').replace('-', ' ').replace(':', ' ').replace('/',' ').replace('*',' ')
                if analyzer.polarity_scores(word)['compound'] > 0.05:
                    pos.append(word)
                elif analyzer.polarity_scores(word)['compound'] < -0.05:
                    neg.append(word)

    counter_pos = Counter(pos)
    counter_neg = Counter(neg) 

    json_pos = json.dumps(counter_pos)
    json_neg = json.dumps(counter_neg)
    f = open("pos.json", "w")
    f.write(json_pos)
    f.close()
    f2 = open("neg.json", "w")
    f2.write(json_neg)
    f2.close()
    generate_word_cloud(pos)
    generate_word_cloud(neg)

# vs = analyzer.polarity_scores("i am a corrupt bastard")
# pos = []
# neg = []
# for word in "i am a corrupt bastard".split(' '):
#     if analyzer.polarity_scores(word)['compound'] > 0.05:
#         pos.append(word)
#     elif analyzer.polarity_scores(word)['compound'] < -0.05:
#         neg.append(word)

#     print(pos)
#     print(neg)