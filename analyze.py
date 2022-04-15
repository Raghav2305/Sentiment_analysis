import joblib
import streamlit as st;
import pyaudio as pd 
import json
import moviepy.editor as mp
import speech_recognition as sr
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class Solution:

    my_clip = mp.VideoFileClip(r"C:/Users/ASUS/Documents/Bandicam/michael.mp4")
    print(my_clip)
    my_clip.audio.write_audiofile(r"result.wav")

    r = sr.Recognizer()
    with sr.AudioFile('result.wav') as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data)
    
    obj = SentimentIntensityAnalyzer()
 
    sentiment_dict = obj.polarity_scores(text)

    negative = sentiment_dict['neg']   
    neutral = sentiment_dict['neu']    
    positive = sentiment_dict['pos']
    compound = sentiment_dict['compound']
    
    if sentiment_dict['compound'] >= 0.05 :
        overall_sentiment = "Positive"

    elif sentiment_dict['compound'] <= - 0.05 :
        overall_sentiment = "Negative"

    else :
        overall_sentiment = "Neutral"
    
    for i in sorted(sentiment_dict):
        print('{0}: {1}, '.format(i, sentiment_dict[i]), end='')
        
    print("\n")
    print("Overall Sentiment: ", overall_sentiment)

    print(f"Text = {text}")
    print("\n")
    print("Sentiment Analysis:-")
    print("\n")
    print(text)

    
    
        
        



