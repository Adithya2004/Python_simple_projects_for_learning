import random
HANGMAN_PICS = ['''
   +---+
       |
       |
       |
      ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
     ===''']
words = "ant baboon badger bat bear beaver camel cat clam cobra cougar crow deer dog donkey duck eagle ferret fox frog goat goose hawk lizard llama mole monkey moose mouse mule newt otter owl panda pigeon python rabbit ram rat raven rhino salmon seal shark skunk sloth snake spider stork swan tiger toad trout turkey weasel whale wolf wombat zebra".split()

def getRandomWord():
    return random.choice(words)
def printHangman(choice):
    print(HANGMAN_PICS[choice])
def initializeGuess(guess_word):
    return ["_" for i in range(len(guess_word))]
def printGuess(guessList):
    temp = ""
    for i in range(len(guessList)-1):
        temp+=guessList[i]+" "
    temp+=guessList[-1]
    print(temp)
def fill(guessList,Word,guess):
    for i in range(len(Word)):
        if Word[i] == guess:
            guessList[i] = guess
    return guessList
print("PLAY HANGMAN")
while True:
    Word = getRandomWord()
    guess_list = initializeGuess(Word)
    ch = 0
    guessed_letters = set()
    letters = set(Word)
    while True:
        printHangman(ch)
        printGuess(guess_list)
        if "_" not in guess_list:
            print("Guessed Correctly!:",Word)
            break
        if ch>=len(Word)+1:
            print(f"Ran out of guesses\nThe word was {Word}")
            break
        guess = input("Guess a Letter:")
        if guess in guessed_letters:
            print("Already Guessed!! Try Again !!")
            continue
        if not guess.isalpha():
            print("Not a Letter!! Try Again !!")
            continue
        if guess in letters:
            print("Good Guess")
            guess_list = fill(guess_list,Word,guess)
            continue
        else:
            print("Wrong Guess")
            ch+=1
            continue
        
    cont = input("Play Again?y/n:")
    if cont == "y":
        continue
    break

