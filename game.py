# import rand library
import random

# create choice method
def getChoices():
    player_choice = input("Enter a choices :\n Rock, Paper, Scissors \n").lower()

    # create options dictionary
    options =["rock","paper","scissors"]

    # Choice the random values in options dictionary
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

# create check win method
def check_win(player,computer):
    print(f"You Chose : {player}, Computer Chose :{computer}")
    if player == computer:
        return"It's a Tie...!"

    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes Scissors! Yor Win...!"
        else:
            return "Paper covers Rock! You Lose...!"

    elif player == "paper":
        if computer == "rock":
            return "Paper covers Rock! You Win...!"
        else:
            return "Scissors cut Paper! You Lose...!"

    elif player == "scissors":
        if computer == "paper":
            return "Scissors cut Paper! You Win...!"
        else:
            return "Rock smashes Scissors! You Lose...!"

print(f"HI THIS IS ROCK PAPER SCISSORS GAME ")         
while True: 
    
    # cheking user want paly game or terminating 
    value = input("You want play the game Enter '1', exit the game '0'\n")   
    value = int(value)  
    
    if value == 1:
        # call get choice method
        # passing the values in choice variable
        choice = getChoices()

        # call check win method
        # passing the values in result variable

        result = check_win(choice["player"], choice["computer"])

        # print result
        print(result)
    
    # cheking  user want terminating    
    elif value == 0:
        print("Done. Terminating")
        exit()