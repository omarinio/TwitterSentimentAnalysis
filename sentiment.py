import sys
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
import json
import re
from collections import Counter
import wordcloud
import matplotlib.pyplot as plt
import polSent as ps

# C:\Users\Omar\AppData\Local\Programs\Python\Python38\Lib\site-packages\vaderSentiment

def generate_word_cloud(word_list, filename, candidate):
    wc = wordcloud.WordCloud(width=1600, height=800, collocations = False)
    wc=wc.generate(" ".join(word_list).lower())
    plt.figure(figsize=(20,10), facecolor='k')
    plt.imshow(wc)
    plt.axis("off")
    # save the wordcloud
    plt.savefig(f'wordclouds/{filename}_{candidate}_selflexicon.png', facecolor='k', bbox_inches='tight')
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
    if len(sys.argv) == 1:
        print("Please type in 'biden' or 'trump' after sentiment.py")
    elif (len(sys.argv) == 2):
        if (sys.argv[1].lower() != 'biden' and sys.argv[1].lower() != 'trump'):
            print("Please enter 'biden' or 'trump' as the argument")
        else:
            analyzer = SentimentIntensityAnalyzer()
            pos = []
            neg = []
            overall = []
            with open(f"tweets/{sys.argv[1].lower()}_cleaned_tweets.json") as json_file:
                data = json.load(json_file)
                for user in data:
                    cleaned_tweet = clean_tweet(data[user][0]['tweet'][0])
                    #print(cleaned_tweet)    
                    vs = analyzer.polarity_scores(cleaned_tweet) 
                    #print(vs)
                    for word in cleaned_tweet.split(' '):
                        word = word.replace('\n', ' ').replace('\xa0',' ').replace('.',' ').replace('·', ' ').replace('•',' ').replace('\t', ' ').replace(',',' ').replace('-', ' ').replace(':', ' ').replace('/',' ').replace('*',' ')
                        for w in word.split(' '):
                            # if analyzer.polarity_scores(w)['compound'] > 0.05:
                            #     pos.append(w)
                            # elif analyzer.polarity_scores(w)['compound'] < -0.05:
                            #     neg.append(w)
                            if (len(w) > 0):
                                vss = ps.wordcloud_ting(w)
                                
                                if (vss > 0.5):
                                    pos.append(w)
                                    overall.append(w)
                                elif (vss < 0.5):
                                    neg.append(w)
                                    overall.append(w)

            # counter_pos = Counter(pos)
            # counter_neg = Counter(neg) 

            # json_pos = json.dumps(counter_pos)
            # json_neg = json.dumps(counter_neg)
            # f = open("pos.json", "w")
            # f.write(json_pos)
            # f.close()
            # f2 = open("neg.json", "w")
            # f2.write(json_neg)
            # f2.close()

            generate_word_cloud(pos, 'positive', sys.argv[1].lower())
            generate_word_cloud(neg, 'negative', sys.argv[1].lower())
            generate_word_cloud(overall, 'overall', sys.argv[1].lower())

            # with open("tweets/trump_cleaned_tweets.json") as json_file:
            #     data = json.load(json_file)
            #     listoftexts = [data[user][0]['tweet'] for user in data]
            #     vss = ps.analyse(listoftexts)
            #     i=0

            #     for i in range(0, vss.shape[0]):
            #         print(vss['tweet'][i])
            #         print(vss['score'][i])
            #         print("\n")
            #         print("\n")
    else:
        print('please only enter one argument')
    

    