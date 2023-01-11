from LingoFunctions import *
repeat = True
repeat2 = True
wordstoprint = []
while repeat == True:
    wordtoguess = GetWord()
    pogingen = 0
    geraden = False
    while pogingen <= MAX_POGINGEN and geraden == False:
        print(wordtoguess)
        wordlength = GetWordLength(wordtoguess)
        wordchecked = wordcheck(wordlength)
        wordtoguesslist = wordtoguessinletters(wordtoguess)
        wordlist = wordinletters(wordchecked)
        checkworddict = checkwords(wordtoguess,wordchecked,wordlist,wordtoguesslist)
        totaltext = getletterswithcolor(checkworddict,wordlist)
        wordstoprint.append(totaltext)
        printlingoboard(wordstoprint,GetWordLength(wordtoguess))
        pogingen += 1
        if checkworddict["geraden"] == True:
            geraden = True
            print("Gefeliciteerd, je hebt het woord geraden! in " + str(pogingen) + " pogingen!")
        else:
            print("Helaas, je hebt het woord niet geraden!")
        if pogingen == MAX_POGINGEN:
            print("Je hebt het woord niet geraden, het woord was: " + wordtoguess)
            while repeat2 == True:
                try:
                    nogeenkeer = input("Wil je nog een keer spelen? Ja/Nee").lower()
                    if nogeenkeer == "ja":
                        repeat=True
                    elif nogeenkeer == "nee":
                        repeat=False
                    else:
                        print("Je hebt geen geldige invoer gegeven")
                    repeat2 = False
                except:
                    print("Je hebt geen geldige invoer gegeven")
                    repeat2 = True
                

    



