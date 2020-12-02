import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        print("Did you mean %s instead" %get_close_matches(word ,data.keys())[0])
        decide = input("Press 'y' for yes or press 'n' to no: ")
        if decide == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif decide == "n":
            return ("You've entered the wrong key")
        else:
            return("You can only type 'y' or 'n' ")
    else:
        print("invalid keyword")
    

    


word = input("Please enter the word you want to search: ")
output = translate(word)

if type(output) == list:
    for item in output:
        print(output)
else:
    print(output)