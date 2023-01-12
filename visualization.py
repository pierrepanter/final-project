from wordcloud import WordCloud,STOPWORDS, ImageColorGenerator
#import matplotlib.pyplot as plt #to display our wordcloud
from PIL import Image #to load our image
import numpy as np #to get the color of our image
from collections import Counter
from os import path
import nltk

#Content-related
text = open('batman.txt', 'r').read()
stop_words = STOPWORDS
english_punctuations = [',', '.', ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%']

word_tokens = nltk.tokenize.word_tokenize(text.strip())
word_tokens = [w for w in word_tokens if not w in stop_words and english_punctuations]
data = []
for word in word_tokens:
    data.append(word)
    dataDict = Counter(data)
    #Counter(data).common(10)
    with open('counting.txt', 'w') as fw:
        for k, v in dataDict.items():
            fw.write("%s,%d\n" % (k, v))
        #  fw.write("%s"%dataDict)
#Appearance-related
custom_mask = np.array(Image.open('batman.png'))
wc = WordCloud(background_color = 'white',
               stopwords = stop_words,
               mask = custom_mask,
               contour_width = 3,
               contour_color = 'black')

wc.generate(text)
image_colors = ImageColorGenerator(custom_mask)
wc.recolor(color_func = image_colors)


wc.to_file('Batman_wordcloud.png')
#