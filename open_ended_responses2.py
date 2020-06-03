# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 17:16:51 2020

@author: ajeanbaptiste
"""

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download("stopwords")
stop_words = set(stopwords.words('english'))
import string


from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import pandas as pd
import numpy as np
import seaborn as sns  # for plots
import matplotlib.pyplot as plt  # for plots
sns.palplot(sns.color_palette("Blues"))
sns.set(style="darkgrid")

# -----------------------------------------------------------------------------
# ------------------ NO NOT RUN THIS LINE OF CODES! ---------------------------
df = pd.read_csv("sel_academy_series_feedback_survey_04_10_2020.csv", low_memory=False)
# -----------------------------------------------------------------------------

# Q13	Please provide an example of a self-awareness practice and/or tool you have used in your personal life or at work.
text = df[['Q13']]
text.dropna

# transforming to list
text = text.values.tolist()    

# Transforming the list of lists to just one list
empty_list = []
for i in range(len(text)):
    empty_list = empty_list + text[i]

print(empty_list)
type(empty_list)


# Tranform list to a string
text = str(empty_list).strip('[]')

# Generating the wordCloud
wordcloud = WordCloud().generate(text)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

# lower max_font_size, change the maximum number of word and lighten the background:
wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white", stopwords=STOPWORDS).generate(text)

plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

# -----------------------------------------------------------------------------
# Q15 Please provide an example of how you have encouraged coworkers and youth to practice resilience and self-care.

text = df[['Q15']]
text.dropna

# transforming to list
text = text.values.tolist()    

# Transforming the list of lists to just one list
empty_list = []
for i in range(len(text)):
    empty_list = empty_list + text[i]

print(empty_list)
type(empty_list)


# Tranform list to a string
text = str(empty_list).strip('[]')

# Generating the wordCloud
wordcloud = WordCloud().generate(text)


# lower max_font_size, change the maximum number of word and lighten the background:
wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white", stopwords=STOPWORDS).generate(text)

plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

# -----------------------------------------------------------------------------
# Q17 How would you describe your social awareness in your personal and work relationships?
text = df[['Q17']]
text.dropna

# transforming to list
text = text.values.tolist()    

# Transforming the list of lists to just one list
empty_list = []
for i in range(len(text)):
    empty_list = empty_list + text[i]

print(empty_list)
type(empty_list)


# Tranform list to a string
text = str(empty_list).strip('[]')

# Generating the wordCloud
wordcloud = WordCloud().generate(text)


# lower max_font_size, change the maximum number of word and lighten the background:
wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white", stopwords=STOPWORDS).generate(text)

plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()


# -----------------------------------------------------------------------------
# Q18 	Please provide an example of how you have implemented Res...
text = df[['Q18']]
text.dropna

# transforming to list
text = text.values.tolist()    

# Transforming the list of lists to just one list
empty_list = []
for i in range(len(text)):
    empty_list = empty_list + text[i]

print(empty_list)
type(empty_list)


# Tranform list to a string
text = str(empty_list).strip('[]')

# Generating the wordCloud
wordcloud = WordCloud().generate(text)


# lower max_font_size, change the maximum number of word and lighten the background:
wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white", stopwords=STOPWORDS).generate(text)

plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()


# -----------------------------------------------------------------------------
# Q26	 What strategies do you use to create a more inclusive Aft...
text = df[['Q26']]
text.dropna

# transforming to list
text = text.values.tolist()    

# Transforming the list of lists to just one list
empty_list = []
for i in range(len(text)):
    empty_list = empty_list + text[i]

print(empty_list)
type(empty_list)


# Tranform list to a string
text = str(empty_list).strip('[]')

# Generating the wordCloud
wordcloud = WordCloud().generate(text)


# lower max_font_size, change the maximum number of word and lighten the background:
wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white", stopwords=STOPWORDS).generate(text)

plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

# -----------------------------------------------------------------------------
# Q28 	Please provide an example of how you have encouraged co-w...
text = df[['Q28']]
text.dropna

# transforming to list
text = text.values.tolist()    

# Transforming the list of lists to just one list
empty_list = []
for i in range(len(text)):
    empty_list = empty_list + text[i]

print(empty_list)
type(empty_list)


# Tranform list to a string
text = str(empty_list).strip('[]')

# Generating the wordCloud
wordcloud = WordCloud().generate(text)


# lower max_font_size, change the maximum number of word and lighten the background:
wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white", stopwords=STOPWORDS).generate(text)

plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()


# -----------------------------------------------------------------------------
# What practices do you use to build self-care and resilience ...
# Preprocessing the text
text = df[['Q31']] # This is a pandas dataframe
text.dropna

# transforming to list
text = text.values.tolist()     

# Transforming the list of lists to just one list
empty_list = []
for i in range(len(text)):
    empty_list = empty_list + text[i]

print(empty_list)
type(empty_list)


# Tranform list to a string
text = str(empty_list).strip('[]')

# Generating the wordCloud
wordcloud = WordCloud().generate(text)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

# lower max_font_size, change the maximum number of word and lighten the background:
wordcloud = WordCloud(max_font_size=50, max_words=170, background_color="white", stopwords=STOPWORDS).generate(text)

plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

# 

# -----------------------------------------------------------------------------
# Q35 	Please provide an example of a relationship building prac...

# Preprocessing the text
text = df[['Q35']] # This is a pandas dataframe
text.dropna

# transforming to list
text = text.values.tolist()     

# Transforming the list of lists to just one list
empty_list = []
for i in range(len(text)):
    empty_list = empty_list + text[i]

print(empty_list)
type(empty_list)


# Tranform list to a string
text = str(empty_list).strip('[]')

# Generating the wordCloud
wordcloud = WordCloud().generate(text)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

# lower max_font_size, change the maximum number of word and lighten the background:
wordcloud = WordCloud(max_font_size=50, max_words=170, background_color="white", stopwords=STOPWORDS).generate(text)

plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()


# -----------------------------------------------------------------------------
# 

# -----------------------------------------------------------------------------
# Q37 	Please provide an example of how you have been able to pr...

# Preprocessing the text
text = df[['Q37']] # This is a pandas dataframe
text.dropna

# transforming to list
text = text.values.tolist()     

# Transforming the list of lists to just one list
empty_list = []
for i in range(len(text)):
    empty_list = empty_list + text[i]

print(empty_list)
type(empty_list)


# Tranform list to a string
text = str(empty_list).strip('[]')

# Generating the wordCloud
wordcloud = WordCloud().generate(text)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

# lower max_font_size, change the maximum number of word and lighten the background:
wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white", stopwords=STOPWORDS).generate(text)

plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()


# -----------------------------------------------------------------------------
# Q39 	Give an example of how you have integrated SEL into other...

text = df[['Q39']]
# transforming to list
text = text.values.tolist()     

# Transforming the list of lists to just one list
empty_list = []
for i in range(len(text)):
    empty_list = empty_list + text[i]

print(empty_list)
type(empty_list)


# Tranform list to a string
text = str(empty_list).strip('[]')

# Generating the wordCloud
wordcloud = WordCloud().generate(text)

# lower max_font_size, change the maximum number of word and lighten the background:
wordcloud = WordCloud(max_font_size=60, 
                      max_words=100, 
                      background_color="white",
                      stopwords=STOPWORDS).generate(text)

plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()


# -----------------------------------------------------------------------------
# Q41 	Give an example of how you incorporated diversity, equity…

equity_text = df[['Q41']]
#equity_text = equity_text.dropna

equity_text = equity_text.values.tolist()

# tranforming this list to an list of list
new_equity_list = []
for i in range(len(equity_text)):
    new_equity_list = new_equity_list + equity_text[i]


# Tranform list to a string
equity_text = str(new_equity_list).strip('[]')

# Generating the word could for the equity question
wordcloud = WordCloud(max_font_size=60, 
                      max_words=150, 
                      background_color="white",
                      stopwords=STOPWORDS).generate(equity_text)

# Display the figure
plt.figure()
plt.imshow(wordcloud, interpolation = 'bilinear')
plt.axis('off')
plt.show()


# -----------------------------------------------------------------------------
# Q42 	Is there anything else you would like to share with us?


text = df[['Q42']]
#equity_text = equity_text.dropna

text = text.values.tolist()

# tranforming this list to an list of list
new_list = []
for i in range(len(text)):
    new_list = new_list + text[i]


# Tranform list to a string
text = str(new_list).strip('[]')


# Generating the word could
wordcloud = WordCloud(max_font_size=100, 
                      max_words= 450, 
                      background_color="white",
                      stopwords=STOPWORDS).generate(text)

# Display the figure
plt.figure()
plt.imshow(wordcloud, interpolation = 'bilinear')
plt.axis('off')
plt.show()


# -----------------------------------------------------------------------------


# ---- NLP 
useless_words = nltk.corpus.stopwords.words("english") + list(string.punctuation)

# Defining a function that will clean the texts and remove all the useless words
def build_bag_of_words_features_filtered(words):
    return {
        word:1 for word in words \
        if not word in useless_words}

build_bag_of_words_features_filtered(text)

words = word_tokenize(text)
build_bag_of_words_features_filtered(words)
words = str(words).strip('[]')
# ----  It works but it's not that good ----
# This word could has the tokenized words
# lower max_font_size, change the maximum number of word and lighten the background:
wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(words)

plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()











