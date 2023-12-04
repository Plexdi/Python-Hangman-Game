import random 
import os
import time

anime = ["Naruto", "Bleach", "OnePiece", "DragonBall", "Nanatsu", "AttackOnTitan", "Naruto", "Boruto", "DeathNote", "HunterXHunter",
          "FairyTail", "OnePunchMan", "Naruto", "DragonBall", "Naruto", "OnePiece", "AttackOnTitan", "DemonSlayer", "BlackClover",
           "TokyoGhoul"]

fruits = ["Apple", "Banana", "Orange", "Grapes", "Strawberry", "Watermelon", "Pineapple", "Kiwi", "Mango", "Blueberry", "Cherry",
           "Peach", "Lemon", "Pear", "Raspberry", "Coconut", "Avocado", "Blackberry", "Cranberry", "Pomegranate", "Guava", "Apricot",
             "Plum", "Fig", "Papaya", "Lime", "Lychee", "Cantaloupe", "Honeydew", "Nectarine", "Dragonfruit", "Passion Fruit", "Mandarin", 
             "Tangerine", "Kumquat", "Starfruit", "Grenadilla", "Currant", "Acai Berry", "Boysenberry", "Elderberry", "Mulberry", "Gooseberry",
               "Durian", "Persimmon"]


computer_parts = ["CPU", "GPU", "RAM", "HDD", "SSD", "Motherboard", "PSU", "Case", "Monitor", "Keyboard", "Mouse", "Speakers", "Headphones", "Webcam", "Microphone",
                 "UPS", "Printer", "Scanner", "Router", "Modem", "Trackpad", "Joystick", 
                    ]




types = ['Anime','Fruits','Computer Parts'] 
tries = 11
user_tries = 0 
num = 1 

def Fruits(): #fruits function 
    global user_tries 
    chosen_word = random.choice(fruits)
    len_word = '_' *len(chosen_word) 

    def update_word(chosen_word, len_word, letter):
        new_word = list(len_word) #converting the underscore into a list so that it is easier to replace.
        for i in range(len(chosen_word)):
            if chosen_word[i] == letter: 
                new_word[i] = letter
        return ''.join(new_word) 
    
    def text():
        text = f'The chosen word was {chosen_word}'
        

        for char in text: #loops through the text character by character
            print(char, end='', flush = True) #print out letter by letter. end='' prevent it from making new line. 
            time.sleep(0.05) #it stop every 0.05 second before running the letter 




    while user_tries < tries: # if user_tries is smaller than the string 'tries = 11' in line 24 then it will run this loops
        print(" ".join(len_word))
        guess = input('Type in your guess: ')

        if guess.lower() == 'quit':
            text()
            quit()

        if not guess.isalpha(): #checking if the user input is is a letter 
            continue

        if guess in chosen_word:
            len_word = update_word(chosen_word, len_word, guess)
            print('Correct.')

        

        else:
            print('That is incorrect try again.')
            user_tries += 1 
            continue

        if len_word == chosen_word:
            print('You have won')
            break



    if user_tries >= tries:
        print('you have lost. Better luck next time.')

        print("You've guessed the word: ", chosen_word)


def Computers():
    global user_tries 
    chosen_word = random.choice(computer_parts)
    len_word = '_' *len(chosen_word)

    def update_word(chosen_word, len_word, letter):
        new_word = list(len_word)
        for i in range(len(chosen_word)):
            if chosen_word[i] == letter:
                new_word[i] = letter
        return ''.join(new_word)
    
    def text():
        text = f'The chosen word was {chosen_word}'
        

        for char in text:
            print(char, end='', flush = True)
            time.sleep(0.05)



    while user_tries < tries:
        print(" ".join(len_word))
        guess = input('Type in your guess: ')

        if guess.lower() == 'quit':
            text()
            quit()

        if not guess.isalpha():
            continue

        if guess in chosen_word:
            len_word = update_word(chosen_word, len_word, guess)
            print('Correct.')

        else:
            print('That is incorrect try again.')
            user_tries += 1 
            continue

        if len_word == chosen_word:
            print('You have won')
            break

    if user_tries >= tries:
        print('you have lost. Better luck next time.')

        print("You've guessed the word: ", chosen_word)

            

def Anime():
    global user_tries  # Declare user_tries as a global variable
    chosen_word = random.choice(anime)
    len_Word = '_' * len(chosen_word)

    def update_word(chosen_word, len_Word, letter):
        new_word = list(len_Word)
        for i in range(len(chosen_word)):
            if chosen_word[i] == letter:
                new_word[i] = letter  # Update the character in the list
        return ''.join(new_word)

    def text():
        text = f'The chosen word was {chosen_word}'
        

        for char in text:
            print(char, end='', flush = True)
            time.sleep(0.05)
            


    while user_tries < tries:
        print(" ".join(len_Word))
        Guess = input('Type in your guess: ')
        
        if Guess == 'quit':
            text()
            quit()

        if not Guess.isalpha():
            continue

        if Guess in chosen_word:
            len_Word = update_word(chosen_word, len_Word, Guess)
            print('Correct')

        else:
            print('That is incorrect, try again')
            user_tries += 1

        if len_Word == chosen_word:
            print('You won!')
            break

    if user_tries >= tries:
        print('You lost.')

    print("You've guessed the word: ", chosen_word)

def Txt():
    text = f'Your chosen category is: {userchoice}'

    for char in text:
        print(char, end='', flush = True)
        time.sleep(0.05)

def text2():
    text = f'\nif you would like to quit. Type "quit".'

    for char in text:
        print(char, end='', flush = True)
        time.sleep(0.05)



for items in types:
    print(f'{num}: {items}')
    num += 1 
while True:
    userchoice = int(input('Enter a number from 1 to 4: '))
    if userchoice == 1:
        os.system('clear')
        userchoice = 'Anime'
        Txt()
        text2()
        

        time.sleep(3.5)
        os.system('clear')
        Anime()



    elif userchoice == 2:
        os.system('clear')
        userchoice = 'Fruits'
        Txt()
        text2()
        
        time.sleep(3.5)
        os.system('clear')
        Fruits()


    elif userchoice == 3:
        os.system('clear')
        userchoice = 'Computer Parts'
        Txt()
        text2()

        time.sleep(3.5)
        os.system('cls')
        Computers()

      



    elif userchoice != int:
        print('that is not a valid number try again.')
        continue

    else:
        print("Please enter in a number.")
        continue