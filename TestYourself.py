print('             Welcome to the "how familiar are you with Israel\'s history?" quiz!')
print("                 In this quiz, you will have 5 questions that will test")
print("                                your history knowledge! ")
print()

# question 1
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Question number 1: Who was the first Prime Minister?")
print("1. David Ben Gurion")
print("2. Moshe Sharett ")
print("3. I don\'t know...")
print("4. Benjamin Netanyahu")
choice = input("Enter choice(1/2/3/4): ")

choice1 = int

if choice == '1':
    choice1 = 4
elif choice == '2':
    choice1 = 3
elif choice == '3':
    choice1 = 1
elif choice == '4':
    choice1 = 2
else:
    print("Invalid input")
    choice1 = 0

# question 2
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Question number 2: Who were against Israel in the 'Six-Day War'?")
print("1. Egypt and Syria")
print("2.  Turkey and Iran")
print("3. Iraq, Jordan and Syria")
print("4. Egypt, Iraq, Syria and Jordan")
choice = input("Enter choice(1/2/3/4): ")

choice2 = int

if choice == '1':
    choice2 = 2
elif choice == '2':
    choice2 = 1
elif choice == '3':
    choice2 = 3
elif choice == '4':
    choice2 = 4
else:
    print("Invalid input")
    choice2 = 0

# question 3
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Question number What is the most populated city in Israel?")
print("1. Ramat Gan")
print("2. Tel Aviv ")
print("3. Jerusalem")
print("4. Haifa")
choice = input("Enter choice(1/2/3/4): ")

choice3 = int

if choice == '1':
    choice3 = 1
elif choice == '2':
    choice3 = 2
elif choice == '3':
    choice3 = 4
elif choice == '4':
    choice3 = 1
else:
    print("Invalid input")
    choice3 = 0

# question 4
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Question number 4: When was the Israeli Declaration of Independence?")
print("1. May 14, 1948")
print("2. May 15, 1948")
print("3. September 27, 1948 ")
print("4. I don\'t know...")

choice = input("Enter choice(1/2/3/4): ")

choice4 = int

if choice == '1':
    choice4 = 4
elif choice == '2':
    choice4 = 3
elif choice == '3':
    choice4 = 1
elif choice == '4':
    choice4 = 1
else:
    print("Invalid input")
    choice4 = 0

# question 5
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Question number 5: Who served the longest as a prime minister in Israel?")
print("1. Ehud Barak ")
print("2. Ariel Sharon ")
print("3. David Ben Gurion")
print("4. Benjamin Netanyahu")
choice = input("Enter choice(1/2/3/4): ")
print()

choice5 = int

if choice == '1':
    choice5 = 1
elif choice == '2':
    choice5 = 1
elif choice == '3':
    choice5 = 3
elif choice == '4':
    choice5 = 4
else:
    print("Invalid input")
    choice5 = 0
answer = int
answer = choice1 + choice2 + choice3 + choice4 + choice5
print("Your score is:", answer)
print()

if answer > 19:
    print("You aced the quiz!")
    print("You knew all the answers and proved you know your roots, congrats!")
elif answer < 20 and answer > 15:
    print("You Answered almost everything right! Good job.")
elif answer < 16 and answer > 10:
    print("You know the basics, keep trying.")
elif answer < 10 and answer > 4:
    print("You didn\'t do a very good job.")
    print("Please polish your history skills and try again.")
elif answer < 5 and answer > 0:
    print("Did you even try?")
elif answer == 0:
    print("You didn\'t answer a single question.")
    print("Please follow the instructions and try again")
else:
    print("I think I messed up my code")
# used this to find bugs when I was testing the final score
