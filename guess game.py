# Guessing a number which I tought

import random

def guess_number(x=10):
    random_number = random.randint(1, x)
    print(f"I thought from 1 to 10, can you guess: ")
    guesses = 0
    while True:
        guesses += 1
        predictical_number = int(input(">>>"))
        if predictical_number < random_number:
            print("False, Bigger than I thought")
        elif predictical_number > random_number:
            print("False, Smaller than I thought")
        else:
            break
    print(f'Congratulations, you find it in {guesses} tries !!!')
    print("Next game >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
# guess_number()

def guess_number_pc(x=10):
    input(f"you should guess from 1 to {x}, please any keyword on your qwerty:   ")
    quyi = 1
    yuqori = x
    predicts = 0
    while True:
        predicts += 1
        if quyi != yuqori:
            taxmin = random.randint(quyi, yuqori)
        else:
            taxmin = quyi
        answer = input(f"Your number is {taxmin}, am I right( yes), "
                       f"My number is bigger than (+), or smaller than (-)".lower())
        if answer == "-":
            yuqori = taxmin - 1
        elif answer == "+":
            quyi = taxmin + 1
        else:
            break
    print(f" I found it with {predicts} tries")
    return predicts
guess_number()
guess_number_pc()
