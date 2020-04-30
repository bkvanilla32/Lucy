#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 13:41:17 2020

@author: luluxiao
"""
import pyowm

dictList = {"hat":{"rain":0.32,"formal":0.12,"wind":0.26},"sunglasses":{"rain":0.23,"formal":0.44,"wind":0.29}}
proFormal = 0


def getMyWeather():

    owm = pyowm.OWM('6e0f0ffa4cb8f1558a41c2b5e0c1c3d2')
    #enter your city
    boston = owm.weather_at_place('Boston, US')
    weather = boston.get_weather()
    #print(weather.get_temperature('celsius')['temp'])
    return weather

"""
def condition(condition):
    boston = owm.three_hours_forecast('Boston, US')
    rain = boston.will_have_rain()
    sun = boston.will_have_sun()
   
    return rain,sun
"""  
   
def getChance(condition):
    if condition =="rain":
        return 0.6
    elif condition =="wind":
        return 0.2
    elif condition == "formal":
        return proFormal
    else:
        return 0
    
def getProb(item,condition):
    conditionProb = dictList[item][condition]
    prob = getChance(condition)*conditionProb
    return prob
        

def possibility(item):
    prob = getProb(item,"rain")+getProb(item,"wind")+getProb(item,"formal")
    return prob
 

  
def bringItem(item):
    chanceOfRain, chanceOfWind = getChance()
    formal =  input("is this a formal even?")
    
    if formal == "yes": 
        return 1
    else: 
        return 0 
    #make decision

def basicWeather():
    line1 = 'The temperature in your city is currently '+ str(getMyWeather().get_temperature('celsius')['temp']) +' celcius. '
    #line2 = 'Do you want any recommendation on clothing?'
    #talkToMe(line1+line2)
    return line1



#==================================== 

def understand(): 
    
    line1 = 'The temperature in your city is currently '+ str(getMyWeather().get_temperature('celsius')['temp']) +' celcius. '
    #line2 = 'Do you want any recommendation on clothing?'
    #talkToMe(line1+line2)
    print(line1)
    
    
        
    
"""
     #print('yescommand = myCommand()')
     yescommand = myCommand()

     if 'no' in yescommand:
          #print('beenRejected()')
          beenRejected()
     else:
          #print('speakOfClothes(yescommand)')
          speakOfClothes()
"""