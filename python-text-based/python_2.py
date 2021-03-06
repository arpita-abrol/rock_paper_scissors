import random

#------------ VARIABLES ------------

# user prompts and responses
prompt = "Rock, Paper, or Scissors?"
rePrompt = "Hmm, I couldn't understand your response."
promptPlay = "Would you like to play again? Yes/No"
computerChoice = "The computer chose "
tie = "It's a tie!"
win = "Good job- you won this round!"
lose = "Looks like the computer won this time"

# variable declarations
options = ["rock", "paper", "scissors"]
optionsPlay = ["yes", "no"]
#-------------------------------------------


def getAndValidate():
    print prompt
    response = raw_input().lower().strip()
    if response not in options:
        print rePrompt
        response = getAndValidate()
    return response

def checkWin(response, aiChoice):
    print computerChoice + aiChoice
    if response == aiChoice:
        print tie
    elif(response == options[0]):
        if(computerChoice == options[1]):
            print lose
        else:
            print(win)
    elif(response == options[1]):
        if(computerChoice == options[2]):
            print lose
        else:
            print win
    else:
        if(computerChoice == options[0]):
            print lose
        else:
            print win

def playAgain():
    print promptPlay
    response = raw_input().lower().strip()
    if response not in optionsPlay:
        print rePrompt
        response = playAgain()
    else:
        if(response == optionsPlay[0]):
            main_three()
        else:
            exit()
    

def main():
    aiChoice = random.choice(options)
    response = getAndValidate()
    checkWin(response, aiChoice)
    playAgain()


main()
    

