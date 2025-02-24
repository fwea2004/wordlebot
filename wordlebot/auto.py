from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from wordlebot_module import wordle_bot
from pathlib import Path 

p = Path(__file__).with_name('words.txt')
filename = p.absolute()
file = open(filename,'r')
wordList = file.read().upper().split()

driver = webdriver.Chrome()
driver.get("https://www.nytimes.com/games/wordle/index.html")

close = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/button').click()
time.sleep(0.5)
play = driver.find_element(By.XPATH, '//button[@data-testid = "Play"]').click()
time.sleep(0.5)
exitPopup = driver.find_element(By.XPATH, '//button[@aria-label = "Close"]').click()
time.sleep(0.5)

io = driver.find_element(By.XPATH, '/html/body')
guess = "AIRNS"

count=0
cycle=0
while True:

    io.send_keys(guess)
    io.send_keys(Keys.ENTER)
    time.sleep(2)

    count+=1
    line = driver.find_element(By.XPATH, f'//*[@id="wordle-app-game"]/div[1]/div/div[{count}]')
    tiles = line.find_elements(By.XPATH, '//div[@aria-roledescription = "tile"]')

    tiles = []
    for i in range(1,6):
        xpath = f'//*[@id="wordle-app-game"]/div[1]/div/div[{count}]/div[{i}]/div'
        tiles.append(driver.find_element(By.XPATH, xpath).get_attribute('data-state'))

    result = ""
    for tile in tiles:
        if tile=="correct":
            result = result + "G"
        elif tile=="present":
                result = result + "Y"
        elif tile=="absent":
            result = result + "N"
        else:
            print("Result attribution error")

    if result == "GGGGG":
        time.sleep(20)
        quit()

    [wordlistNew,guess] = wordle_bot(wordList,result,guess,cycle)
    wordList = wordlistNew    
    cycle+=1
    
         