def checkwords(word:str,wordinput:str,wordlist:list,wordtoguesslist:list):
    checkwordlist = []
    checkworddict = {}
    wordtoguesslistcopy = wordtoguesslist.copy()
    listcheck = 0
    if word == wordinput:
        checkworddict["geraden"]=True
    else:
        checkworddict["geraden"]=False
    for i in range(len(wordlist)):
        if wordlist[i] == wordtoguesslist[i] and listcheck == 0	:
            checkwordlist.append(1)
            wordtoguesslistcopy.remove(wordlist[i])
            listcheck = 1
        elif wordlist[i] in wordtoguesslist and listcheck == 0 and wordlist[i]  in wordtoguesslistcopy:
            checkwordlist.append(2)
            listcheck = 1
        elif wordlist[i] not in wordtoguesslistcopy and listcheck == 0:
            checkwordlist.append(3)
            listcheck = 1
        listcheck=0

def checkwords(word:str,wordinput:str,wordlist:list,wordtoguesslist:list):
    checkwordlist = []
    checkworddict = {}
    if word == wordinput:
        checkworddict["geraden"]=True
    else:
        checkworddict["geraden"]=False
    for i in range(len(word)):
        if wordlist(i)==wordtoguesslist(i):
            checkwordlist.append(1)
        else:
            checkwordlist.append("+")
    for i in range(len(word)):
        if wordlist(i) in wordtoguesslist and checkwordlist(i) == "+":
            checkwordlist(i) == 2
    for i in range(len(word)):
        if wordlist(i) not in wordtoguesslist and checkwordlist(i) == "+":
            checkwordlist(i) == 3
    checkworddict["checklist"]=checkwordlist
    return checkworddict