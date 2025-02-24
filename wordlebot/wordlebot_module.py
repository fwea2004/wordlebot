'''
function: wordle_bot
inputs:  wordle dictionary, result and guess
outputs: list of updated wordlist and new next guess
'''
def wordle_bot(wordList,result,guess,cycle):

    #filter result into green, yellow and grey
    potentWord = []
    greenLets = []
    yellowLets = []
    greyLets = []
    numGYN = [0,0,0]
    for k in range(0,len(guess)):
        if result[k]=="G":
            greenLets.append(guess[k])
            potentWord.append(guess[k])
            numGYN[0]+=1 
        elif result[k]=="Y":
            yellowLets.append(guess[k])
            potentWord.append(1)
            numGYN[1]+=1
        else:
            greyLets.append(guess[k])
            potentWord.append(0)
            numGYN[2]+=1

    #second exclusion guess
    """
    if (numGYN[2]>1) and cycle==0:
        for word in wordList:
            if len(list(set(word).intersection(guess)))==0:
                return [wordList,word]
    """
    
    #check for green and grey repeat problem
    dbls = list(set(greenLets).intersection(greyLets))

    #filter out greens and greys
    shortlist = []
    for word in wordList:

        #set vars
        indx=0
        dblsCount=0
        greenNum=0
        greyCheck=0

        #loop for letters in each word
        for letter in word:
            if str(letter)==str(potentWord[indx]):
                greenNum+=1
            if potentWord[indx]==0:
                if str(guess[indx]) in str(word):
                    if str(guess[indx]) not in yellowLets:
                        if str(guess[indx]) not in greenLets:
                            greyCheck=1

            if letter in dbls:
                dblsCount+=1

            
            indx+=1
        
        #check if all greens and greys are accounted for 
        if numGYN[0]==greenNum:
            if dblsCount<2:
                if greyCheck==0:
                    shortlist.append(word)

    #update wordlist
    wordList = shortlist

    #filter out yellows
    shortlist = []
    for word in wordList:

        #set vars
        indx=0
        yellowNum=0

        #loop for letters in each word
        for letter in potentWord:
            if letter:
                if guess[indx] in str(word):
                    if str(guess[indx])!=str(word[indx]):
                        yellowNum+=1

            indx+=1

        #check if all yellows are accounted for
        if yellowNum==numGYN[1]:
            shortlist.append(word)

    #update wordlist
    wordList=shortlist

    #define common letters
    commonLets = ['A','E','S','O','R','I','L','T','N','U']
    uncommonLets = ['J','Q','X','Z']

    #update next guess
    if len(wordList)==0:
        print("Wordlist error")
        return 1
    else:

        #check if guess is certain
        if len(wordList)==1:
            winner = [wordList[0]]
            return [wordList,winner]

        #finding highest count of common letters
        winner = [wordList[0],len(set(commonLets).intersection(wordList[0])),len(set(uncommonLets).intersection(wordList[0]))]    
        for k in range(0,len(wordList)-1):

            toBeat = [wordList[k+1],len(set(commonLets).intersection(wordList[k+1])),len(set(uncommonLets).intersection(wordList[k]))]

            if (toBeat[1]>winner[1]) and (toBeat[2]<=winner[2]):
                winner = toBeat
                
        #return most probable guess/expected answer
        return [wordList,winner[0]]
