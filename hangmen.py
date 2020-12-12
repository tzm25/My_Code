import random

def hangmen():
    word = random.choice(["ironman","thor","captainamerica","chhottabheem","superman","heimdal"])
    validletter = "abcdefghijklmnopqrstuvwxyz"
    guess_made = ""
    turns = 0

    while len(word) > 0:
        main = ""
        missed = 0

        for letter in word:
            if letter in guess_made:
                main = main + letter
            else:
                main = main + "_" + " "

        if main == word:
            print(main)
            print("You win!")
            break
        
        print("Guess the word!")
        guess = input()

        if guess in validletter:
            guess_made = guess_made + guess
        else:
            print("Please enter a valid letter")
            guess = input()
        if guess not in word:
            turns -= 1





name = input("Please enter your name: ")
print("Welcome", name)
print("-------------")

print("Try to guess a word in less than 10 try.")


hangmen()