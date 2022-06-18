import random

NUM_DIGITS = 3  
MAX_GUESSES = 10


def main():

    print('''Bagels, a deductive logic game.
    By Al Sweigart al@inventwithpython.com

    I am thinking of a {}-digit number with no repeated digits.
    Try to guess what it is. Here are some clues:
    When I say: That means:
    Pico One digit is correct but in the wrong position.
    Fermi One digit is correct and in the right position.
    Bagels No digit is correct.

    For example, if the secret number was 248 and your guess was 843, the
    clues would be Fermi Pico.'''.format(NUM_DIGITS))


    while True: #main game loop
        #Store the secret number the player need to guess
        secretNum = getSecretNUm()
        print('I have thught up a number.')
        print(' You have {} guess to get it '.format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            #Keep looping until they enter a valid guess
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(numGuesses))
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses')
                print('The answer was {}'.format(secretNum))

        #Ask player if they want to play again
        print('Do You Want To Play Again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break

    print('Thanks for playing!')

def getSecretNUm():
    """Return a string made up of NUM_DIGITS unique random digits"""
    number = list('0123456789')
    random.shuffle(number)

    #Get the first NUM_DIGITS in the list for the secret number 

    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(number[i])

    return secretNum

def getClues(guess, secretNum):
    """Return a string with the pico, fermi , bagels clues for a guess"""

    if guess == secretNum:
        return 'You go it!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # A correct digit is in the correct pleace
            clues.append('Fermi')

        elif guess[i] in secretNum:
            #A correct digit is in the incorrect place
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels' # There are no correct digit at all

    else:
        #Sort the clues into alpabetic order so there original order
        clues.sort()
        #Make a single string from the list of string clues
        return ' '.join(clues)



main()    
            