from collections import Counter
import sys

file = open("wordclouds/wordcloud_frequency_biden_positive.json", "r")
falo = file.read()
sorted(falo.items(), key=lambda pair: pair[1], reverse=True)

print(count.most_common())