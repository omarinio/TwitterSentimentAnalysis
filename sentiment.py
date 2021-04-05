from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

vs = analyzer.polarity_scores("The election fraud that was the 2020 election should be fully investigated and exposed and then Trump should be granted an extra term.")

print(vs)