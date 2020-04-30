#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 13:41:09 2020

@author: luluxiao
"""


from gtts import gTTS
import speech_recognition as sr
import os
import webbrowser
import playsound
#import smtplib
from datetime import date
from datetime import datetime
import datetime
import requests
from pprint import pprint
from bs4 import BeautifulSoup
from mutagen.mp3 import MP3
import time 
from pygame import mixer
import sentencetype
import linguist
import funcList
import weatherman 
import linguist2
import nltk
from nltk import word_tokenize
import webbrowser
import data_allDialogs
"""
class Lucy:
    
    def __init__(self,name):
        self.name = name 
    
    do.talkToMe("Hi, I‘m lucy! What can I do for you?")
    do.helpMe()
"""

#do.talkToMe("Hi, I‘m lucy! What can I do for you?")
#do.assist(do.helpMe())

otherwords = ["can","help","find","me","you"]

def beenRejected():
     #talkToMe('Okay, let me know when you need that.')
     print('Okay, let me know when you need that.')

def shouldI(question):
        prob=weatherman.possibility(question)
        if prob >0.75:
            print("I thhink you should wear "+ question)
        elif prob > 0.5:
            print("I will suggest wear " + question)
        elif prob >0.25:
            print("I think both way is okay. It's up to you.")
        else:
            print("I don't think you need to bring "+question)
            
def findGoalandBehavior(statement):
    wordlist=[]
    wordtypelist=[]
    tags = nltk.pos_tag(word_tokenize(statement))

    for i in range(0,len(tags)):
        wordlist.append(tags[i][0])
        wordtypelist.append(tags[i][1])

    behavior = 'x'
    goal = 'x'

    if 'VB' in wordtypelist:
        behavior = wordlist[wordtypelist.index('VB')]
    if 'NN' in wordtypelist:
        goal = wordlist[wordtypelist.index('NN')]
        if wordtypelist.index('JJ') < wordtypelist.index('NN') and behavior == 'x':
            behavior = wordlist[wordtypelist.index('JJ')]

    #print(behavior,goal)

    return behavior,goal 

def doIKnow(do,go):
    
    try:
        data_allDialogs.operation[do][go]
        return True
    except KeyError:
        return False
    
#====================================      

print("Hi, I‘m lucy! What can I do for you?")
command = input("-->")
funcName = linguist2.whereBelong(command)


#print(funcName[0:8])
if  funcName== "XXXXXX":
    print("sorry, i am not able to do that.")
elif funcName == "morning" :
    funcName = "funcList.funcgreeting1()"
    try:
        eval(funcName)
        print(weatherman.basicWeather())
    except: 
        print("sorry, i am not able to do that.")
        
    answer = input("-->")
    word_tokens = linguist2.word_tokenize(answer)
   
    if "hat" in word_tokens:
        shouldI("hat")
    elif "sunglasses" in word_tokens:
        shouldI("sunglasses")
    else: 
        print("Sorry, I haven't learned that. ")
    
elif funcName == "weather" :
    funcName = "funcList.func"+funcName +"understand()"
    answer = input("-->")
    word_tokens = linguist2.word_tokenize(answer)
   
    if "hat" in word_tokens:
        shouldI("hat")
    elif "sunglasses" in word_tokens:
        shouldI("sunglasses")
    else: 
        print("Sorry, I haven't learned that. ")
elif funcName == "operationList":
    b,g = findGoalandBehavior(command)
    try:
        funcName = "funcList.func"+data_allDialogs.operation[b][g] + "()"
        eval(funcName)
    except:
        print("Sorry, I haven't learned that. ")

else:
    print("Sorry, I haven't learned that. ")
    