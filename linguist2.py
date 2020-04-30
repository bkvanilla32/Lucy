#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 18:52:41 2020

@author: luluxiao
"""



from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
import function_retrieveLucyBasicOperations as retrieve
import data_allDialogs
from data_allDialogs import operation
from nltk.tokenize import word_tokenize as tknize
from nltk.tokenize.treebank import TreebankWordDetokenizer as Detok #
from spellchecker import SpellChecker
######################
from sentenceCorrector import SentenceCorrector
from sentencetype import getSentenceProperty

stop_words = set(stopwords.words('english'))
detokenizer = Detok()



def cleanSentence(sentence):
    word_tokens = word_tokenize(sentence)
    cleaned_sent = word_tokens
    cleaned_sent = [x for x in word_tokens if x not in stop_words]
    return cleaned_sent

def spellChecker(sentenceTokens):
    
    spell = SpellChecker()
    #print(cleaned_sentence)
    misspelled = list(spell.unknown(sentenceTokens))
    #wrongwordsindex = []
    #print(misspelled)
    
    for w in misspelled:
        originalindex = sentenceTokens.index(w)
        #print(originalindex)
        newword = spell.correction(w)
        sentenceTokens[originalindex]=newword
        #print(cleaned_sentence)
    
    sentence = detokenizer.detokenize(sentenceTokens)
    
    return sentence

def confirmChange(sentence,sentence2):
    
    if sentence2 == "":
        return sentence
    
    answer = input("Do you mean '" + sentence2 + "'?  \n")
   
    if answer == "yes": 
        return sentence2
    else: 
        return sentence
    
def cosineSimilarity(cleaned_sentence,sentence2):
    
    #sentence = cleanSentence(sentence)
    sentence2 = cleanSentence(sentence2)
    l1 =[];l2 =[] 
    # form a set containing keywords of both strings  
    rvector = set(cleaned_sentence).union(set(sentence2))
    for w in rvector: 
        if w in cleaned_sentence: l1.append(1) # create a vector 
        else: l1.append(0) 
        if w in sentence2: l2.append(1) 
        else: l2.append(0) 
      
    # cosine formula  
    c = 0
    try:
        for i in range(len(rvector)): 
            c+= l1[i]*l2[i] 
        cosine = c / float((sum(l1)*sum(l2))**0.5) 
        return cosine
    except:
        return 0

def theMax(sentence,group):
    if sentence in eval(group):
        return 1
    elif max([cosineSimilarity(sentence,i)  for i in group]) >0:
        return max([cosineSimilarity(sentence,i)  for i in group]) 
    else:
        return 0

#==================================== 

#plan 1: find the sentence similarity among all data without preprocessing the sentence
    
def whatCategory(sentence):
    simList = []
    list1 = ["morning","weather","operationList"]
    
    for i in list1:
        category = "data_allDialogs." + i
        simList.append(theMax(sentence,category))
    
    maxSim = max(simList)
    maxIndex = simList.index(maxSim)
    category = list1[maxIndex]
    
    return maxSim, category

#checking any misspelled words

def preprocessing(sentence):
    sentenceTokens = cleanSentence(sentence)
    sentence2 = spellChecker(sentenceTokens)
    
    if sentence2 != sentence:
        sentence = confirmChange(sentence,sentence2)    
        
    return sentence
    


#====================================
#====================================


def whereBelong(sentence):
    word_tokens = word_tokenize(sentence)
    if "can" in word_tokens and "find" in tokens:
        return "googlesearch"
    sentence2 = preprocessing(sentence)
    sim1, category1 = whatCategory(sentence)
    sim2, category2 = whatCategory(sentence2)
    
    if sim2 > sim1:
        return category2
    elif sim2<sim1: 
        return category1
    elif sim1 == 0 and sim2 ==0:
        return "XXXXXX"
    else: 
        return category1
    
  

def understand(sentence):
    
    #check all data 
    funcName = whereBelong(sentence)
    #check online 
    
    
    #return category(funcnName)