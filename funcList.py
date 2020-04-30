#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 17:34:09 2020

@author: luluxiao
"""

"""
FORMAT: "func" + "category" + "code"

INDEX
======================
======================

I. greeting

1.1: say "good morning" and provide basic info(whether)

======================

II: os(operating system)

2.1: open browser
2.2: open google
2.3: pen quora, 
2.4: open youtube 
2.5: close browser
2.6: close google
2.7: close quora
2.8: close youtube
2.9: play music 

======================
======================

"""

import nltk
from nltk import word_tokenize
import webbrowser
import webbrowser
import playsound
#import smtplib
from datetime import date
from datetime import datetime
import datetime
import requests
from pprint import pprint
import pyowm
from bs4 import BeautifulSoup
from mutagen.mp3 import MP3
import time 
from pygame import mixer
import sentencetype
#import lucyfunctionlist as do


"""
def getAllNames():
    name_func_tuples = inspect.getmembers(funcList, inspect.isfunction)
    name_func_tuples = [t for t in name_func_tuples if inspect.getmodule(t[1]) == funcList]
   functions = [w[0] for w in name_func_tuples]
   return  functions


"""


#======================
#======================
# greeting

def today():
     now = datetime.datetime.now()
     year = now.strftime("%Y")
     month = now.strftime("%B")
     day = now.strftime("%d")
     line = year + month +" "+ day
     return line

def funcgreeting1():
     td = today()
     rp = 'Good morning! Today is '+td
     #talkToMe(rp)
     #speakOfWeather()
     print(rp)
     
#======================
#======================
# os
def funcos1():
    webbrowser.open('http://www.google.com', new=2)

def funcos2():
    webbrowser.open('http://www.google.com', new=2)

def funcos3():
    webbrowser.open('http://www.quora.com', new=2)
    
    
def funcos4():
    webbrowser.open('http://www.youtube.com',new=2)

def funcos5():
    webbrowser.close()