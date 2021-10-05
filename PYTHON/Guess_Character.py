import random

# Shuffling the list
def mylist():
    lst = ["", "", "X"]
    random.shuffle(lst)
    return lst


# Asking user to guess a number
def make_guess():
    guess = ""
    while guess not in [0, 1, 2]:
        guess = int(input("Choose 0, 1 or 2: "))
    return guess


# Checking if guess number match the char
def check(mylist, make_guess):
    if mylist[make_guess] == "X":
        print("Right Guess!")
    else:
        print("Wrong Guess!")


# Calling a finction
check(mylist(), make_guess())
