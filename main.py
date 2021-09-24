from os import system
import random

pchoice = ''
comchoice = ''

def cls():
    _ = system('cls')

def win(): # define win script
    print('You won!\nYou: ' + pchoice + '\nCOM: ' + str(comchoice))
    input('Press any button to continue.')

def lose(): # define lose script
    print('You lost!\nYou: ' + pchoice + '\nCOM: ' + str(comchoice))
    input('Press any button to continue.')  

def choice():
    cls()
    pchoice = input('1: Rock\n2: Paper\n3: Scissors\nChoose of of the 3 Options: ')
    if pchoice == ('1') or pchoice == ('2') or pchoice == ('3'):
        comchoice = (random.randint(int(1),int(3)))
        #check for invalid input and compare player/com choices
        if pchoice == str(comchoice):
            print('Tie!\nYou: ' + pchoice + '\nCOM: ' + str(comchoice))
            input('Press any button to continue.')
        elif pchoice is ('1') and comchoice is (2):
            lose()     
        elif pchoice is ('1') and comchoice is (3):
            win()
        elif pchoice is ('2') and comchoice is (1):
            win()
        elif pchoice is ('2') and comchoice is (3):
            lose()
        elif pchoice is ('3') and comchoice is (1):
            lose()
        elif pchoice is ('3') and comchoice is (2):
            win()
        else:
            print('Something has gone wrong.')
            print('Debug:\nYou: ' + pchoice + '\nCOM: ' + str(comchoice))
            input('Press any button.')
    else:
        print('Invalid Input!')
        input('Press any button to retry...')
        choice()
        
try:
    while True:
        cls()
        print('Rock Paper Scissors')
        input('Press any button to start the game.')
        choice()
        def inputok():
            input('')
        


except KeyboardInterrupt:
    cls()
    print('Closed Rock Paper Scissors.')