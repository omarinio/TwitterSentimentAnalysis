from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

vs = analyzer.polarity_scores("Joe Biden is to stupid to be the President His illiteracy and incompetence will set America back decades This rigged election will hurt us all a long time GOP seeks to pull back curtain on Biden tax shelter hypocrisy FoxNews")

print(vs)