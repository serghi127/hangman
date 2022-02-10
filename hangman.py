import random
from time import sleep

linecount = 0

popularmovies = open('textfilesforgames\popularmovies', 'r')
celebrities = open('textfilesforgames\celebrities.txt', 'r')
foods = open('textfilesforgames\yummy.txt', 'r')
popularsongs = open('textfilesforgames\popularsongs.txt', 'r')

listofblank = []
incorrectletters = []
correctletters = []
guessedletters = []


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = [':', '-', "'", '.', '?', '!']

playeringame = True
numofguesses = 6
gameover = False

hangmangame = []

def load():
    print('.')
    sleep(0.2)
    print('..')
    sleep(0.2)
    print('...')
    sleep(0.2)
    print('..')
    sleep(0.2)
    print('.')
    sleep(0.2)

def guessletter():
    global gameover
    global numofguesses
    global guessedletters
    global correctletters
    
    while numofguesses > 0 and gameover == False:
        print('\n')
        print(*hangmangame)
        print(*titlelist)
        guess = input("\nEnter a letter. You have " + str(numofguesses) + " lives left!: ")
        print('Guessed letters: ' + str(guessedletters))
        load()

        if guess.lower() in guessedletters:
            print('You already guessed that letter! Guess again!')
            continue

        elif guess.lower() == name.lower() or '__' not in hangmangame:
            gameover = True
            break

        elif guess.lower() in titlelist1:
            print('\nGood job! You guessed a correct letter!')
            if guess.lower() not in guessedletters:
                guessedletters.append(guess.lower())
                guessedletters = sorted(guessedletters)
            if guess.lower() not in correctletters:
                correctletters.append(guess.lower())
                correctletters = sorted(guessedletters)
            for i in range(len(titlelist)):
                if titlelist1[i] == guess.lower():
                    hangmangame[i] = titlelist[i]
                    if '__' not in hangmangame:
                        gameover = True
                        break

        elif guess.lower() in alphabet and guess.lower() not in titlelist1:
            print('\nThe letter you entered is not in the name. Try again!')
            if guess.lower() not in incorrectletters or guess.lower not in guessedletters:
                incorrectletters.append(guess.lower())
                guessedletters.append(guess.lower())
            guessedletters = sorted(guessedletters)
            numofguesses -= 1
        else:
            print('Not a real letter (in the English language)! Guess again!')
            continue

while playeringame:

    if gameover == False:
        popularmovies = open('textfilesforgames\popularmovies', 'r')
        celebrities = open('textfilesforgames\celebrities.txt', 'r')
        foods = open('textfilesforgames\yummy.txt', 'r')
        popularsongs = open('textfilesforgames\popularsongs.txt', 'r')
        

        category = input("Hello! Welcome to the hangman game. Guess letters to get the title, name, or word.\n"
        "To start, select a category.\n"
        "Press 1 for popular movies, 2 for celebrities, 3 for foods, and 4 for popular songs: ")
        if category == '1':
            category1 = popularmovies
            celebrities.close(), foods.close(), popularsongs.close()
        elif category == '2':
            category1 = celebrities
            popularmovies.close(), foods.close(), popularsongs.close()
        elif category == '3':
            category1 = foods
            celebrities.close(), popularmovies.close(), popularsongs.close()
        elif category == '4':
            category1 = popularsongs
            celebrities.close(), foods.close(), popularmovies.close()
        else:
            print('That is not a valid category! Try again!')
            continue
        
        for line in category1:
            listofblank.append(line.strip()) 
        titleindex = random.randint(0, (len(listofblank) - 1))
        name = listofblank[titleindex]
        titlelist = list(name)
        titlelist1 = list(name.lower())
        hangmangame.clear()
        load()

        for letter in titlelist:
            if letter.lower() in alphabet and letter != ' ':
                hangmangame.append('__')
            elif letter in symbols:
                hangmangame.append(letter)
            elif letter == ' ':
                hangmangame.append('   ')
                

        while numofguesses > 0 and gameover == False:
            guessletter()

    elif gameover == True:
        print('\nGood job! You guessed the hangman!')
        sleep(1)
        answer = input('Would you like to play again? Press Y for yes and X for no: ')
        if answer.lower() == 'y':
            numofguesses = 6
            load()
            gameover = False
        elif answer.lower() == 'x':
            print("\nThanks for playing!")
            load()
            print('NEW GAME')
            sleep(1)
            exit()
        else:
            print('Not a valid answer! Try again.')
            continue

    elif numofguesses == 0:
        gameover = True
        print('\nGame Over! The hangman name was ' + name.upper() + '!')
        sleep(1)
        answer = input("Would you like to play again? Press 'Y' for yes and 'X' for no: ")
        if answer.lower() == 'y':
            numofguesses = 6
            load()
            print('NEW GAME')
            gameover = False
        elif answer.lower() == 'x':
            print("\nThanks for playing!")
            load()
            sleep(1)
            exit()
        else:
            print('Not a valid answer! Try again.')
            continue