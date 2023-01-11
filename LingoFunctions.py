from termcolor import *
from lingowords import *
from random import *
KLEURGOED = "red"
KLEURSLECHT = "white"
KLEURHALF = "yellow"
NUMMERGOED = 1
NUMMERHALF = 2
NUMMERSLECHT = 3
MAX_POGINGEN = 5

def GetWord():
    word = choice(words)
    return word

def GetWordLength(word):
    return len(word)

def wordcheck(lenword:int):
    repeat = True
    while repeat == True:
        wordinput = input("Geef een woord van " + str(lenword) + " letters:")
        if int(len(wordinput)) == lenword and wordinput.isalpha() == True:
            repeat = False
            return wordinput
        else:
            repeat = True

def wordtoguessinletters(wordtoguess:str):
    wordlist = []
    for letter in wordtoguess:
        wordlist.append(letter)
    return wordlist

def wordinletters(wordinput:str):
    wordlist = []
    for letter in wordinput:
        wordlist.append(letter)
    return wordlist

def checkwords(word:str,wordinput:str,wordlist:list,wordtoguesslist:list):
    checkwordlist = []
    checkworddict = {}
    listcheck = 0
    if word == wordinput:
        checkworddict["geraden"]=True
    else:
        checkworddict["geraden"]=False
    for i in range(len(wordlist)):
        if wordlist[i] == wordtoguesslist[i] and listcheck == 0	:
            checkwordlist.append(1)
            listcheck = 1
        elif wordlist[i] in wordtoguesslist and listcheck == 0:
            checkwordlist.append(2)
            listcheck = 1
        elif wordlist[i] not in wordtoguesslist and listcheck == 0:
            checkwordlist.append(3)
            listcheck = 1
        listcheck=0
    checkworddict["checkwordlist"]=checkwordlist
    return checkworddict

def getletterswithcolor(checkworddict:dict,wordlist:list):
    listtoprint = []
    wordnumber = 0
    totaltext = ""
    for i in checkworddict["checkwordlist"]:
        if i == NUMMERGOED:
            listtoprint.append(colored(wordlist[wordnumber],KLEURGOED))
        elif i == NUMMERHALF:
            listtoprint.append(colored(wordlist[wordnumber],KLEURHALF))
        elif i == NUMMERSLECHT:
            listtoprint.append(colored(wordlist[wordnumber],KLEURSLECHT))
        wordnumber+=1
    for j in range(len(listtoprint)):
        totaltext = totaltext + listtoprint[j]
    return totaltext

def printlingoboard(wordstoprint:list,wordlenght:int):
    print("Lingo Board:")
    if len(wordstoprint) < 5:
        for i in range(len(wordstoprint)):
            print(wordstoprint[i])
        for i in range(5-len(wordstoprint)):
            print("*"*wordlenght)




    
    



        

