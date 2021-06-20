print("Welcome to my 1 st game project!")
name = input("What is your name? ")
age = int(input("What is your age? "))

print("Hi ", name, "you are", age, "years old.")

if age >= 18:
    print("You are allowed! ")
    start = input("Can we start ( yes / no )?  ")
    if start.lower() == "yes":
        print("Let's Start")
        answer_1 = input("1st question: What is the capital of Italy? ")
        if answer_1.title() == 'Rome':
            print("Your answer is TRUE,", name)
        else:
            print("your answer is FALSE, Right answer is Rome.")
        answer_2 = input("2nd question: What is the capital of Uzbekistan ? ")
        if answer_2.title() == 'Tashkent':
            print("Your answer is TRUE,", name)
        else:
            print("your answer is FALSE, Right answer is Tashkent")
        answer_3 = input("3rd question: What is the capital of the UK ? ")
        if answer_3.title() == 'London':
            print("Your answer is TRUE,", name)
        else:
            print("your answer is FALSE, Right answer is London")
        answer_4 = input("4th question: What is the capital of Japan ? ")
        if answer_4.title() == 'Tokyo':
            print("Your answer is TRUE,", name)
        else:
            print("your answer is FALSE, Right answer is Tokyo")
        answer_5 = input("5th question: What is the capital of Lebanon ? ")
        if answer_5.title() == 'Beirut':
            print("Your answer is TRUE,", name)
        else:
            print("your answer is FALSE, Right answer is Beirut")
        answer_6 = input("6th question: What is the capital of Norway ? ")
        if answer_6.title() == 'Oslo':
            print("Your answer is TRUE,", name)
        else:
            print("your answer is FALSE, Right answer is Oslo")
    else:
        print("okay, I got you")
elif age >= 14:
    print("You can play with supervision")
else:
    print("You are not allowed! ")
print('Game is over')

