# ------------------------------------------------------------
# Import libraries
# ------------------------------------------------------------
import random
# ------------------------------------------------------------
# Constants
# ------------------------------------------------------------
ROCK = "ROCK"
PAPER = "PAPER"
SCISSORS = "SCISSORS"
# ------------------------------------------------------------
# Global variables
# ------------------------------------------------------------
choices = [ROCK, PAPER, SCISSORS]
computerChoice = ""
user_input = ""
# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------
computerChoice = choices(random.randint (0, 2))
u = input ("Rock, Paper, Scissors: ")
u = u.upper () #it is put to the upper case because the variables in the list are all upper case and in order to compare they need to have the same case
if u == computerChoice: # checking if the user picked what the computer did
    print ("We have a tie!")
elif u == ROCK: # checking if the user input is rock
    if computerChoice != "PAPER":
        print ("You lose, " + computerChoice + " covers " + u)
    else:
        print ("You win, " + u + " smashes " + computerChoice)
elif u == PAPER: # checking if the user input is paper
    if computerChoice == SCISSORS:
        print ("You lose, " + computerChoice + " cuts " + u)
    else:
        print ("You win, " + u + " covers " + computerChoice)
elif u == SCISSORS:
    if computerChoice == 'SCISSORS':
        print ("You lose, " + computerChoice + " smashes " + u)
    else:
        print ("You win, " + u + " cuts " + computerChoice)
else:
    print("Invalid input")

