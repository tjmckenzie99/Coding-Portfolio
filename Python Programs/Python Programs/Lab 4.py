#Team 2, section 02, Gabriel Gesteira, Todd McKenzie, and Evan Kalb
#purpose - to take the user on an adventure
#Pre-conditions:  user inputs choices as integers, 1 or 2.
#Post-conditions:  prompts are displayed, results of actions are displayed
#outcome of game is reported


def main():
    # set gold flag to False
    gold = False
    # set coconut flag to False
    coconut = False
    # set lived flag to True
    lived = True

    # display first prompt 
    print("Your three hour Caribbean cruise encounters a perfect storm.")
    print("Tossed overboard, you wake on the beach of a deserted island.")
    print("You see the beach stretching to the north and some trees inland.")
    print("")
    print("Do you")
    print("  1. Walk along the beach")
    print("  2. Head for the trees")

    # get user's first choice
    input_choice = int(input())
    # if user chooses 1
    #display chest prompt Open / Carry
    if input_choice == 1:
        print("You see a chest half buried in the sand")
        print("Do you")
        print("  1. open the chest")
        print("  2. pick up the chest")
        
        # get user's Second choice
        input_choice2 = int(input())
        if input_choice2 == 1:
            print("You open the chest and find 500 Gold doubloons.")
            print("")
            gold = True

        else:
            print("Sorry, as you place your hand under the chest,")
            print("you are bitten by a venomous snake.")
            print("Your suffering is great, followed by your death.")
            print("")
            lived = False

    else:
        print("You see a gorilla next to a tree")
        print("Do you")
        print("1. Arm wrestle the gorilla")
        print("2. Say Hello")

        input_choice3 = int(input())
        if input_choice3 == 1:
            print("You win the match with the gorilla! He gives you a coconut!")
            print("")
            coconut = True

        else:
            print("You say hello to the gorilla, he thumps his chest, and sprints up the mountain")
            print("")
        
    


    print("Adventure Over!")
    print("")
    print("Results: ")
    if lived == True:
        print("Congratulations, you survived the challenge!")
        if gold == True:
            print("You have the Gold")
        if coconut == True:
            print("You have the Coconut")
    else:
        print("You didn't make it!")
main()

# Test Case (1,1) Result: You find 500 gold doubloons, Congratulations! You survived the challenge. You have the Gold.
# Test Case (1,2) Result: You didn't make it!
# Test Case (2,1) Result: Congratulations, you survived the challenge! You have the Coconut
# Test Case (2,2) Result: Congratulations, you survived the challenge!


