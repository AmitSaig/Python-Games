import random
money = int(50)
money1 = int(50)
money2 = int(50)
mode = int(0)
name = ''
name2 = ''

def single():
    print("\\\\\\\\\\\\\\\\\\\Welcome to the///////////")
    print("/////////'WAR' card game!\\\\\\\\\\\\\\\\\\\ ")
    name = input("Please enter your name: ")

    print("welcome to the game", name + "!", "you currently have:", money, "$")
    # assigning card suits
    suit1 = ''
    suit2 = ''
    checker(money)

# assigning func to play again
def newgame():
    print("Would you like to play again?")
    choice = input("yes or no: ")
    if choice == 'yes':
        print("Lets go!")
        print()
        checker(money)
    elif choice == 'no':
        print("See you next time!")
        print("~~you left with", money, "$~~~")
        exit()
    else:
        print("answer only with yes or no!!")
        print()
        newgame()

def newgame2():
    print("Would you like to play again?")
    choice = input("yes or no: ")
    if choice == 'yes':
        print("Lets go!")
        print()
        checker2(money1, money2)
    elif choice == 'no':
        print("See you next time!")
        print(name, "left with", money1, "$ and", name2, "left with", money2, "$")
        exit()
    else:
        print("Answer only with yes or no!!")
        print()
        newgame2()

# assigning func to play
def play2():
    global money1
    global money2
    global bet
    dealer = random.randint(1, 12)
    player = random.randint(1, 12)
    ransuit1 = random.randint(1, 4)
    ransuit2 = random.randint(1, 4)
    if ransuit1 == 1:
        suit1 = '♠'
    elif ransuit1 == 2:
        suit1 = '♥'
    elif ransuit1 == 3:
        suit1 = '♣'
    elif ransuit1 == 4:
        suit1 = '♦'
    if ransuit2 == 1:
        suit2 = '♠'
    elif ransuit2 == 2:
        suit2 = '♥'
    elif ransuit2 == 3:
        suit2 = '♣'
    elif ransuit2 == 4:
        suit2 = '♦'

    print(name, "draw", player, suit1, "and", name2, "draw", dealer, suit2)
    if player > dealer:
        money1 = money1 + bet
        money2 = money2 - bet
        print("Congrats!", name, " won this round")
        print(name, "have:", money1, "$, and", name2, "have:", money2, "$")
        if money2 == 0:
            print("Sorry!", name2, "lost all his money!")
            print(name, "wins with", money1, "$!")
            exit()
        else:
            print()
            newgame2()
    elif player == dealer:
        print("It\'s a draw! let\'s try again")
        print()
        play2()
    else:
        money2 = money2 + bet
        money1 = money1 - bet
        print(name2, "won this round!")
        print(name2, "have:", money2, "$, and", name, "have:", money1, "$")
        if money1 == 0:
            print("Sorry!", name, "lost all his money!")
            print(name2, "wins with", money2, "$!")
            exit()
        else:
            print()
            newgame2()

def play():
    global money
    global bet
    dealer = random.randint(1, 12)
    player = random.randint(1, 12)
    ransuit1 = random.randint(1, 4)
    ransuit2 = random.randint(1, 4)
    if ransuit1 == 1:
        suit1 = '♠'
    elif ransuit1 == 2:
        suit1 = '♥'
    elif ransuit1 == 3:
        suit1 = '♣'
    elif ransuit1 == 4:
        suit1 = '♦'
    if ransuit2 == 1:
        suit2 = '♠'
    elif ransuit2 == 2:
        suit2 = '♥'
    elif ransuit2 == 3:
        suit2 = '♣'
    elif ransuit2 == 4:
        suit2 = '♦'

    print("I draw", dealer, suit1, "and you draw", player, suit2)
    if player > dealer:
        money = money + bet
        print("Congrats! you won this round")
        print("Now you have:", money, "$")
        print()
        newgame()
    elif player == dealer:
        print("It\'s a draw! let\'s try again")
        print()
        play()
    else:
        money = money - bet
        print("You lost this round!")
        print("Now you have:", money, "$")
        if money == 0:
            print("Sorry! you lost all your money!")
            print("We can\'t keep playing if you have no money, BYE!")
            exit()
        else:
            print()
            newgame()


# assigning a func to check currency
def checker(money):
    global bet
    bet = int(input("Please place your bet on the next round: "))
    if money >= bet:
        money = money - bet
        print("Lets play! you bet", bet, "$ this round")
        print()
        play()
    else:
        print("Sorry, we can\'t keep playing if you try to cheat")
        print("Take your", money, "$ and LEAVE!")
        exit()

def checker2(money1, money2):
    global bet
    bet = int(input("Please place your bet on the next round: "))
    if money1 >= bet and money2 >= bet:
        money1 = money1 - bet
        money2 = money2 - bet
        print("Lets play! you bet", bet, "$ this round")
        print()
        play2()
    else:
        print("Sorry, you can\'t keep playing if someone is trying to cheat")
        print("Take your earnings and LEAVE!")
        exit()

def start():
    print("For player vs. AI press 1")
    print("For player vs. player press 2")
    mode = int(input("Choose game mode: "))

    if mode == 1:
        print()
        single()
    elif mode == 2:
        print()
        multi()
    else:
        print("You did not enter a valid game mode, run again to start")
        exit()


def multi():
    global name
    global name2
    print("\\\\\\\\\\\\\\\\\\\Welcome to the///////////")
    print("/////////'WAR' card game!\\\\\\\\\\\\\\\\\\\ ")
    name = input("Please enter the name of the 1st player: ")
    name2 = input("Please enter the name of the 2nd player: ")
    print()

    print("welcome to the game", name, "and", name2, "!", "you start with 50$ each.")
    # assigning card suits
    suit1 = ''
    suit2 = ''
    checker2(money1, money2)






start()
