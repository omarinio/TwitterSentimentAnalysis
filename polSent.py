import pandas as pd
import numpy as np

lex = pd.read_csv("politics.tsv",sep='\t')

#removes all but latin leters
def filterNonLatin(myStr):
    whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    answer = ''.join(filter(whitelist.__contains__, myStr))
    return answer

#returns dataframe cotaining lexicon
def getLexicon():
    return pd.read_csv("politics.tsv",sep='\t')

def createHash(lex):
    h = {}
    for i in range(0, lex.shape[0]):
        h[lex["word"][i]] = lex["score"][i]
    return h

h = createHash(lex)

def findSumScore(tweet, h):
    tokenList = tweet.split()
    sum = 0
    for tok in tokenList:
        if tok in h:
            sum += h[tok]
    
    return sum

def findAverageScore(tweet, h):
    #cheeky line of cleaning the string here
    tokenList = tweet.lower().split()
    sum = 0
    for tok in tokenList:
        if tok in h:
            sum += h[tok]
        else:
            tokenList.remove
    
    return sum/len(tokenList)

def analyse(tweets):
    # lex = getLexicon()
    # h = createHash(lex)
    scores = [findAverageScore(tweet, h) for tweet in tweets]
    scoreFrame = pd.DataFrame()
    scoreFrame["tweet"] = tweets
    scoreFrame["score"] = scores
    return scoreFrame

def wordcloud_ting(word):
    score = 0
    if word in h:
        score = h[word]
    
    return score


def test():
    print(analyse(["Lib"]))

if __name__ == '__main__':
    test()