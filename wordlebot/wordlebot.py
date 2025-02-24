from pathlib import Path
from wordlebot_module import wordle_bot

#import file of wordle dictionary
p = Path(__file__).with_name('words.txt')
filename = p.absolute()
file = open(filename,"r")
wordList = file.read().upper().split()

#take initial guess
guess = input("Enter Initial Guess: ")

#main loop
cycle=0
while True:
    try:
        #take outcome
        result = input("Enter outcome. Green, yellow or neither (G/Y/N): ").upper()
        
        #check if right
        if result == "GGGGG":
            print("Hey congrats!")
            quit()

        try:
            [wordList,guess] = wordle_bot(wordList,result,guess,cycle)
            cycle+=1
        except TypeError:
            print("Function failed, maybe update words.txt")
            quit()

        #display next guess
        if len(wordList)>1:
            print(f"Next guess should be: {wordList[0]}")
        elif len(wordList)==1:
            print(f"Pretty sure the correct answer is: {wordList[0]}")
            quit()

    #escape option
    except KeyboardInterrupt:
        quit()