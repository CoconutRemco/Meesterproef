from LingoFunctions import *
repeat = True
repeat2 = True
while repeat == True:
    wordstoprint = []
    wordtoguess = GetWord()
    pogingen = 0
    geraden = False
    showintro()
    showrules()
    while pogingen <= MAX_POGINGEN and geraden == False:
        print(wordtoguess)
        wordlength = GetWordLength(wordtoguess)
        wordtoguesslist = wordtoguessinletters(wordtoguess)
        printfirtslingoletter(wordtoguesslist)
        wordchecked = wordcheck(wordlength)
        wordlist = wordinletters(wordchecked)
        checkworddict = checkwords(wordtoguess,wordchecked,wordlist,wordtoguesslist)
        totaltext = getletterswithcolor(checkworddict,wordlist)
        wordstoprint.append(totaltext)
        printlingoboard(wordstoprint,GetWordLength(wordtoguess))
        pogingen += 1
        if checkworddict["geraden"] == True:
            geraden = True
            print("Gefeliciteerd, je hebt het woord geraden! in " + str(pogingen) + " pogingen!")
            playagain=keepplaying()
            if playagain == False:
                repeat = False
            else:
                repeat = True
        elif pogingen == MAX_POGINGEN:
            print("Je hebt het woord niet geraden, het woord was: " + wordtoguess)
            playagain=keepplaying()
            if playagain == False:
                repeat = False
                showoutro()
            else:
                repeat = True
 

    



