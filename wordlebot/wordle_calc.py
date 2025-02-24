from wordlebot_module import wordle_bot
from pathlib import Path
import time

p = Path(__file__).with_name('words.txt')
filename = p.absolute()
file = open(filename,'r')
wordListConst = file.read().upper().split()

writeFile = open('calc.txt','w')

avrgDenom = len(wordListConst)
nums = []

for initialGuess in wordListConst:

    start = time.time()
    guess = initialGuess
    avrgSum=0

    for answer in wordListConst:

        count=1
        result = ""
        for i in range(0,len(answer)):
            if guess[i]==answer[i]:
                result += "G" 
            elif guess[i] in answer:
                result += "Y"
            else:
                result += "N"

        wordList = wordListConst

        while result!="GGGGG":

            count+=1

            [wordList,guess] = wordle_bot(wordList,result,guess)

            result = ""
            for i in range(0,len(answer)):
                if guess[i]==answer[i]:
                    result += "G" 
                elif guess[i] in answer:
                    result += "Y"
                else:
                    result += "N"

        avrgSum+=count
        
    avrg = avrgSum/avrgDenom
    writeFile.write(f"Initial guess: {initialGuess} - Num guesses: {round(avrg,10)}\n")

    nums.append(avrg)
    end = time.time()
    elapsed = end - start

    print(f"{initialGuess}")
    print(f"time: {round(elapsed,3)}")
    print(f"num guesses: {round(avrg,10)}")

nums.sort()   
writeFile.write("\n~~~\n\n")
for num in nums:
    writeFile.write(f"{num}\n")
writeFile.close()