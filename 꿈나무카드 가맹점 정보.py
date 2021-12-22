#!/usr/bin/env python
# coding: utf-8

# In[28]:


import pandas as pd
import numpy as np
from bs4 import BeautifulSoup

df_seoul = pd.read_csv("서울시 꿈나무카드 가맹점 현황 2020.csv", sep=",")

manu_seoul = df_seoul["Unnamed: 2"][2:]
num_manu = manu_seoul.size
list_manu_seoul =[ ]
for i in range(2, num_manu):
    list_manu_seoul.append(manu_seoul[i])
len_list_manu_seoul = len(list_manu_seoul)
store_manu_seoul = ""
for i in range(0,len_list_manu_seoul):
    store_manu_seoul += (" " +list_manu_seoul[i])

f = open("store_manu_seoul.txt", "w", encoding = 'utf-8')
f.write(store_manu_seoul)
f.close()

import matplotlib.pyplot as plt
from wordcloud import WordCloud

text = open('store_manu_seoul.txt', encoding = 'utf-8').read()
wordcloud = WordCloud(font_path = "KoPubWorld Batang Bold.ttf", background_color = 'white').generate(text)
plt.figure(figsize=(10.,10))
plt.imshow(wordcloud, interpolation = 'bilinear')
plt.axis("off")
plt.show()


df_seoul = pd.read_csv("서울시 꿈나무카드 가맹점 현황 2020.csv", sep=",")

manu_seoul = df_seoul["Unnamed: 2"][2:]
num_manu = manu_seoul.size
list_manu_seoul =[ ]
for i in range(2, num_manu):
    list_manu_seoul.append(manu_seoul[i])
len_list_manu_seoul = len(list_manu_seoul)
store_manu_seoul = ""
for i in range(0,len_list_manu_seoul):
    store_manu_seoul += (" " +list_manu_seoul[i])

f = open("store_manu_seoul.txt", "w", encoding = 'utf-8')
f.write(store_manu_seoul)
f.close()


text = open('store_manu_seoul.txt', encoding = 'utf-8').read()
wordcloud = WordCloud(font_path = "KoPubWorld Batang Bold.ttf", background_color = 'white').generate(text)
plt.figure(figsize=(10.,10))
plt.imshow(wordcloud, interpolation = 'bilinear')
plt.axis("off")
plt.show()


# In[45]:


df_ydp = pd.read_csv("19.영등포구.csv", sep=",")

manu_ydp = df_ydp["Unnamed: 2"][2:]
num_ydp = manu_ydp.size
list_manu_ydp =[ ]
for i in range(2, num_ydp):
    list_manu_ydp.append(manu_ydp[i])
len_list_manu_ydp = len(list_manu_ydp)
store_manu_ydp = ""
for i in range(0,len_list_manu_ydp):
    store_manu_ydp += (" " +list_manu_ydp[i])

f = open("store_manu_ydp.txt", "w", encoding = 'utf-8')
f.write(store_manu_ydp)
f.close()

text_ydp = open('store_manu_ydp.txt', encoding = 'utf-8').read()
wordcloud = WordCloud(font_path = "KoPubWorld Batang Bold.ttf", background_color = 'white').generate(text_ydp)
plt.figure(figsize=(10.,10))
plt.imshow(wordcloud, interpolation = 'bilinear')
plt.axis("off")
plt.show()


# In[ ]:




