#!/usr/bin/env python
# coding: utf-8

# <H3>Text Formatting Function</H3>

# In[4]:


import pandas as pd
import nltk
import string


# In[5]:


from nltk.corpus import stopwords
from nltk.stem import PorterStemmer


# In[6]:


nltk.download('stopwords')


# In[7]:


# Function text_formatting - Receive a string and remove the unwanted characters, punctuation, and stop words.
# This function also updates the dictionary, appending each stemmed word. 

def text_formatting(text_line):

    # Remove newlines and convert backslashes into single space.
    text_line = text_line.replace("\\n", " ").replace("/", " ").replace("-", " ")

    # Define punctuation.
    # We want to keep the "$" symbol, so we remove it from the default list of unwanted symbols.
    custom_punctuation = string.punctuation.replace("$", "")
    custom_punctuation = custom_punctuation + '“' + '–'

    # Remove punctuation from the given string.
    for char in custom_punctuation:
        text_line = text_line.replace(char, '')

    # Split into list.
    text_line = text_line.split(" ")

    # Remove stop words.
    text_line = [word for word in text_line if not word in set(stopwords.words('english'))]

    # Perform the stemming process.
    text_line = [ps.stem(word) for word in text_line]
    
    # Update the vocabulary.
    for word in set(text_line):
        vocabulary.append(word)

    # Rejoin line text  
    text_line = " ".join(text_line)
    
    return text_line


# In[ ]:




