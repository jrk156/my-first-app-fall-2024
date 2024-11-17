# the "app/rps.py" file (v1)...
from random import choice


#
# USER SELECTION
#

game_continue = True
VALID_OPTIONS = ["rock", "paper", "scissors"]

win_tally = 0
loss_tally = 0
tie_tally = 0

while game_continue == True:

    u = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()
    print("USER CHOICE:", u)
    if u not in VALID_OPTIONS:
        print("OOPS, TRY AGAIN")
        exit()

    #
    # COMPUTER SELECTION
    #

    from random import choice

    c = choice(VALID_OPTIONS)
    print("COMPUTER CHOICE:", c)

    #
    # DETERMINATION OF WINNER
    #
    TIE_GAME_MESSAGE = "TIE GAME"
    USER_WINS_MESSAGE = "USER WINS"
    COMPUTER_WINS_MESSAGE = "COMPUTER WINS"

    def tie_game():
        global tie_tally
        print(TIE_GAME_MESSAGE)
        tie_tally = tie_tally + 1

    def user_wins():
        global win_tally
        print(USER_WINS_MESSAGE)
        win_tally = win_tally + 1
        return win_tally

    def cpu_wins():
        global loss_tally
        print(COMPUTER_WINS_MESSAGE)
        loss_tally = loss_tally + 1
        return loss_tally

    
    
    def print_tally():
        print("\nWINS: ", win_tally, "\nLOSSES: ", loss_tally, 
              "\nDRAWS: ", tie_tally, "\n")

    


    if u == "rock":
        if c == "rock":
            tie_game()
        elif c == "paper":
            user_wins()
        else:
            cpu_wins()

    elif u == "paper":
        if c == "rock":
            user_wins()
        elif c == "paper":
            tie_game()
        else:
            cpu_wins()
    
    else:
        if c == "rock":
            cpu_wins()
        elif c == "paper":
            user_wins()
        else:
            tie_game()



    continue_yes_no = input("Continue? (y/n) ")
    if continue_yes_no == 'y':
        game_continue = True
    else:
        game_continue = False
        print_tally()

