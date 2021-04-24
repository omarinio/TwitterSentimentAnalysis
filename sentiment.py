from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
import json
import re
from collections import Counter
import wordcloud
import matplotlib.pyplot as plt

# C:\Users\Omar\AppData\Local\Programs\Python\Python38\Lib\site-packages\vaderSentiment

def generate_word_cloud(word_list, filename):
    wc = wordcloud.WordCloud(width=1600, height=800, collocations = False)
    wc=wc.generate(" ".join(word_list).lower())
    plt.figure(figsize=(20,10), facecolor='k')
    plt.imshow(wc)
    plt.axis("off")
    # save the wordcloud
    plt.savefig(f'wordclouds/{filename}_biden.png', facecolor='k', bbox_inches='tight')
    #wc.to_file(f'wordclouds/{filename}_biden.png')

def clean_tweet(tweet):
    # retweet cleaning
    tweet = re.sub("RT @[\w]*:", '', tweet)
    # twitter handle removal
    tweet = re.sub("@[\w]*", '', tweet)
    # URL removal
    tweet = re.sub("https?://[A-Za-z0-9./]*", '', tweet)
    tweet = re.sub("&", "and", tweet)

    return tweet

def remove_duplicates(x):
    return list(dict.fromkeys(x))

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
                for w in word.split(' '):
                    if analyzer.polarity_scores(w)['compound'] > 0.05:
                        pos.append(w)
                    elif analyzer.polarity_scores(w)['compound'] < -0.05:
                        neg.append(w)

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

    generate_word_cloud(pos, 'positive')
    generate_word_cloud(neg, 'negative')

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