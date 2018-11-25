#!/usr/bin/env python
# coding: utf-8

# Libraries
import string
import folium
import string
import math
import heapq

import pandas as pd
import numpy as np

import folium.plugins as plugins

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from geopy.distance import geodesic
from folium.plugins import MeasureControl
from collections import Counter


# Variables
df = pd.read_csv("Airbnb_Texas_Rentals.csv")

# Create a dictionary that stores every word found in documents.
dictionary = dict()
dictionary2 = dict()

# Create a vocabulary list that stores every word found in documents with index.
vocabulary = list()


# Function text_formatting - Receive a string and remove the unwanted characters, punctuation, and stop words.
# This function also updates the dictionary, appending each stemmed word. 

# Create porter stemmer object.
ps = PorterStemmer()

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
    text_line = text_line.lower()
    text_line = text_line.split(" ")

    # Remove stop words.
    text_line = [word for word in text_line if not word in set(stopwords.words('english'))]

    # Perform the stemming process.
    text_line = [ps.stem(word) for word in text_line]

    # Rejoin line text  
    text_line = " ".join(text_line)
    
    return text_line


# Vocabulary Function

# Create and update the vocabulary when invoked
def add_voc(text_line):
    text_line = text_line.split(" ")
    
    # Update the vocabulary.
    for word in set(text_line):
        vocabulary.append(word)


# TFIDF Function


# Define tfidf function
def TFIDF(term_id, term, text):
    
    count = 0
    for word in text:
        if word == term:
            count += 1
    tf = (count/len(text))
    
    N = len(df)  
    n = len(dictionary[term_id])
    idf = math.log10(N/n)
    
    tfidf = tf*idf
    
    return tfidf