# Todd McKenzie, CS 115 Section 002, tmckenzie0034@uky.edu

import random

def pass_or_roll(player_name, pass_num):
    
    while True:
        
        # If the player has no passes left, automatically roll
        
        if pass_num == 0:
            
            roll = random.randint(1, 6)
            
            # Displaying the result of the roll
            
            print("{} rolled a {} roll".format(player_name, roll))
            
            # Returning the choice as 'R' and the roll value
            
            return 'R', roll
        
        # If the player has passes left, prompt them to choose
        
        else:
            
            player_turn = input("Player {} (P)ass or (R)oll? ".format(player_name))

            if player_turn == 'R' or player_turn == 'r':

                # Generating a random number between 1 to 6 inclusive

                roll = random.randint(1, 6)

                # Displaying the result of the roll

                print("{} rolled a {} roll".format(player_name, roll))

                # Returning the choice as 'R' and the roll value

                return 'R', roll

            elif player_turn == 'P' or player_turn == 'p':

                # Decrementing the number of passes the player has left

                pass_num -= 1

                # Displaying that the player passed the roll

                print(player_name, "passed the roll")

                # Returning the choice as 'P' and None as roll value

                return 'P', None

            else:

                # Displaying that the player has entered an invalid response

                print("Invalid response, P or R please.")

def play_turn(player_name, player_num, pass_num):
    
    # Getting the player's choice and the roll value
    
    choice, roll = pass_or_roll(player_name, pass_num)
    
    # Updating the player's score or pass count based on their choice
    
    if choice == 'R':
        
        player_num += roll
    
    elif choice == 'P':
        
        pass_num -= 1
        
    # Returning the updated score and pass count
        
    return player_num, pass_num

def main():
    
    # prints title
    
    print("Don't get to 21!")
    print('')
    print("Each player tries not to get to 21")
    print('Each player has 3 passes, which allow them to not roll on a round.')
    print('')
    
    # initializes variables
    
    player1_pass_num = 3
    player2_pass_num = 3
    roll_num = 0
    num_round = 0
    player1_num = 0
    turn = 0
    player2_num = 0
    
    # Enter player names
    
    player1 = input('Who is player 1? ')
    player2 = input('Who is player 2? ')
    print('')
    
    # Running each round of the game until one player has scored 21 or more points
    
    while (player1_num < 21 and player2_num < 21):
        num_round += 1
        print("Round {}:".format(num_round))
        
        # Player 1 turn
        player1_num, player1_pass_num = play_turn(player1, player1_num, player1_pass_num)
        
        # Player 2 turn
        player2_num, player2_pass_num = play_turn(player2, player2_num, player2_pass_num)
        
        # Displaying the scores and passes for both players after each round
        print('')
        print("{} total roll {} passes {}      |        {} total roll {} passes {}".format(player1 ,player1_num, player1_pass_num, player2,player2_num, player2_pass_num))
        print('')
        print('')
    
    # Determines winner   
    
    if player1_num >= 21:
        
        print("{} is the winner!".format(player2))
        
    else:
        
        print("{} is the winner!".format(player1))    
    
main()

