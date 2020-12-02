import random


x = "y"
while x == "y":
    num = random.randint(1,6)
    print("Welcome to dice rolling!")
    x = input("Type 'y' to play or type 'q' to quit: ")
    if x == "q":
        break   

    if num == 1:
        print("----------")
        print("|        |")
        print("|   1    |")
        print("|        |")
        print("----------")
    
    elif num == 2:
        print("----------")
        print("|        |")
        print("|   2    |")
        print("|        |")
        print("----------")
    elif num == 3:
        print("----------")
        print("|        |")
        print("|   3    |")
        print("|        |")
        print("----------")
    elif num == 4:
        print("----------")
        print("|        |")
        print("|   4    |")
        print("|        |")
        print("----------")
    elif num == 5:
        print("----------")
        print("|        |")
        print("|   5    |")
        print("|        |")
        print("----------")
    elif num == 6:
        print("----------")
        print("|        |")
        print("|   6    |")
        print("|        |")
        print("----------")




