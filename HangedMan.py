import random

red = lambda text: '\033[0;31m' + text + '\033[0m'
blue = lambda text: '\033[0;34m' + text + '\033[0m'
cyan = lambda text: '\033[0;36m' + text + '\033[0m'

word_bank = ["publisher", "hypothermia", "transparent", "wristwatch",
             "relationship", "grandfather", "caterpillar", "notification",
             "policeman", "companion", "javascript", "jerusalem", "stingray"]
hidden = random.choice(word_bank)
hid_list = list(hidden)
attempts = int(10)
guess = ''
guess_list = list(guess)
guess_word = []
length = len(hidden)
letters = "abcdefghijklmnopqrstuvwxyz"
mistake = []
# ------------------------------------------------------------------------------
print()
print("                  (\.---./) ")
print("                   /.-.-.\ ")
print("                  /| 0_0 |\ ")
print("                 |_`-(v)-'_|")
print("                 \`-._._.-'/            ")
print("   ---------~-(((.`-\_|_/-'.)))-~---------")
print("  |               `.     .'              |")
print("  |                 `._.'                |")
print("  |     Welcome to the game 'HANGMAN'!   |")
print("  |                                      |")
print("   -------------~--~---~~~----~----------- ")
print()
print(cyan("Instructions:"))
print(cyan("You get a random word, and you have to guess what it is!"))
print(cyan("You have 10 attempts, each turn you will be asked for a letter"))
print(cyan("If the letter is not part of the hidden word, you will lose 1 attempt"))
print(cyan("You can guessing the word when you have 5 attempts"))
print()
print("Ready to have some fun? let\'s start!")
print()


def start():
    for i in hidden:
        guess_word.append("*")
    print("A random word was chosen")
    print(guess_word)
    print("The word has", length, "letters in it")
    print("Please make sure you guess only 1 letter")
    print("Or a word with", length, "letters")
    print()


start()


def check():
    if guess_word == hid_list:
        print()
        print("Bullseye! you won! the word was: ", hidden)
        print("Thanks for playing :] ")
    else:
        if attempts > 0:
            print("The hidden word is:")
            print(guess_word)
            print("The letters you used so far are: ", mistake)
            print()
            turn()
        else:
            print("You don\'t have more attempts! you lose")
            print("The hidden word was: ", hidden)
            exit()


def word_guess():
    global mistake
    if guess == hidden:
        print()
        print("Congrats! you won! the word was: ", hidden)
        print("Thanks for playing :] ")
        exit()
    else:
        mistake.append(guess)
        print(red("Sorry! the word is incorrect"))
        print()
        check()


def turn():
    global guess
    global attempts
    global mistake
    global guess_word

    print("You have", attempts, "attempts left")
    guess = input("What is your next guess? ").lower()
    if guess in letters:
        if guess in mistake:
            print("You already used that letter!")
            print()
            turn()
        else:
            if len(guess) == 1:
                if guess in hid_list:
                    mistake.append(guess)
                    print(blue("Congrats! you found a letter"))
                    print()
                    for x in range(0, length):
                        if hidden[x] == guess:
                            guess_word[x] = guess
                    check()
                if guess not in hid_list:
                    mistake.append(guess)
                    print(red("Sorry! the letter is incorrect"))
                    attempts -= 1
                    print()
                    check()
            else:
                print("I said 1 letter only!")
                print()
                turn()
    elif len(guess) == length:
        if attempts < 6:
            if guess in mistake:
                print("You already used that word!")
                print()
                turn()
            else:
                word_guess()
        else:
            print("You cant guess the word yet!")
            print()
            turn()
    else:
        print("I said 1 letter only!")
        print()
        turn()


turn()
