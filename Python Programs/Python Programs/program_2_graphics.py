# Todd McKenzie, CS 115 Section 002, tmckenzie0034@uky.edu
# Purpose: This a game called don't hit 21! If a player hits 21 or over they lose.
# Pre-conditions: User decides to roll or pass.
# Post-conditions: The user is presented with if they won the game or not.


from graphics import *
import random

def draw_die(num, win):
    """
    Draws an image of a die with the given number in the center.
    Returns the Image object so it can be undrawn when necessary.
    """
    
    filename = "{}.gif".format(num)
    img = Image(Point(0.5 * win.getWidth(), 0.5 * win.getHeight()), filename)
    img.draw(win)
    return img

def inbetween(p, p1, p2):
    """
    Returns True if point p is between points p1 and p2
    (inclusive of the endpoints), otherwise False.
    """
    return (p1.getX() <= p.getX() <= p2.getX() or
            p2.getX() <= p.getX() <= p1.getX()) and \
           (p1.getY() <= p.getY() <= p2.getY() or
            p2.getY() <= p.getY() <= p1.getY())

def pass_or_roll(pname, passcount, win):
    """
    Asks the player whether they want to pass or roll, using buttons on the screen.
    Returns 'P' or 'R' based on the user's choice.
    """
    
    # If passcount is zero. It just runs the rolls.
    
    if passcount == 0:
        
        return 'R'
    
    # Draws the pass and roll boxes.
    
    else:
        
        roll_box = Rectangle(Point(0.2 * win.getWidth(), 0.45 * win.getHeight()), Point(0.4 * win.getWidth(), 0.65 * win.getHeight()))
        roll_text = Text(roll_box.getCenter(), "Roll")
        roll_text.setSize(int(0.025 * win.getWidth()))
        roll_box.draw(win)
        roll_text.draw(win)        
    
        pass_box = Rectangle(Point(0.6 * win.getWidth(), 0.45 * win.getHeight()), Point(0.8 * win.getWidth(), 0.65 * win.getHeight()))
        pass_text = Text(pass_box.getCenter(), "Pass")
        pass_text.setSize(int(0.025 * win.getWidth()))
        pass_box.draw(win)
        pass_text.draw(win)
        
        prompt = Text(Point(0.5 * win.getWidth(), 0.1 * win.getHeight()), "{}: Click a box.".format(pname))
        prompt.setSize(int(0.03 * win.getWidth()))
        prompt.draw(win)
        
        
        # Wait for user to click a button
        click = win.getMouse()
        while not (inbetween(click, roll_box.getP1(), roll_box.getP2()) or
                   inbetween(click, pass_box.getP1(), pass_box.getP2())):
            click = win.getMouse()
            
        # Undraws everything
        
        prompt.undraw()
        roll_box.undraw()
        roll_text.undraw()
        pass_box.undraw()
        pass_text.undraw()
        
        
        # Returns choice
        
        if inbetween(click, roll_box.getP1(), roll_box.getP2()):
            return 'R'
        else:
            return 'P'
    
        click = win.getMouse()
        while not (inbetween(click, roll_box.getP1(), roll_box.getP2()) or
                   inbetween(click, pass_box.getP1(), pass_box.getP2())):
        
            click = win.getMouse()
            
        # Undraws everything.
        
        prompt.undraw()
        roll_box.undraw()
        roll_text.undraw()
        pass_box.undraw()
        pass_text.undraw()
        
        if inbetween(click, roll_box.getP1(), roll_box.getP2()):
            return 'R'
        else:
            return 'P'

def play_turn(pname, total, passcount, win):
    """
    Performs one player's turn, either rolling or passing as the player chooses.
    Returns the updated roll total and pass count.
    """
    
    # Displays turn
    
    prompt = Text(Point(100, 50), "{}'s turn. ".format(pname))
    prompt.draw(win)
    choice = pass_or_roll(pname, passcount, win)
    message = Text(Point(0.5 * win.getWidth(), 0.7 * win.getHeight()), '')
    
    # If the user rolls, roll for the value and image. Display both.
    
    if choice == 'R':
        roll = random.randint(1, 6)
        total += roll
        die_img = draw_die(roll, win)
        
        # If the passcount is zero, automatically roll.
        
        if passcount == 0:
            message.setText(f"Out of passes. Rolled a {roll}")
            message.setSize(int(0.025 * win.getWidth()))
            message.draw(win) 
            
    # If users passes, displays the pass dice and moves on to the next player.
    
    else:
        prompt.setText("{} passed.".format(pname))
        passcount -= 1
        die_img = draw_die(0, win)
        
    # Undraws everything.
    
    win.getMouse()
    prompt.undraw()
    die_img.undraw()
    message.undraw()
    
    return total, passcount

# Purpose: Puts everything all together to make the game work.
# Preconditions: User inputs roll or pass
# Postconditions: User wins or does not win.

def main():
    
    # Displays the name of the game.
    
    win = GraphWin("Roll 21 Game", 500, 500)
    
    # Displays title screen and rules.
    
    title = Text(Point(250, 100), "Don't hit 21 or over!")
    title.setSize(30)
    title.setStyle("bold")
    title.draw(win)

    rules = Text(Point(250, 250), "Each player tries not to get to 21. Each player has three passes which allow them not to roll a round.")
    rules.setSize(8)
    rules.draw(win)

    click_to_start = Text(Point(250, 400), "Click anywhere to start.")
    click_to_start.setSize(20)
    click_to_start.draw(win)
    

    win.getMouse()

    # Undraws everything.
    title.undraw()
    rules.undraw()
    click_to_start.undraw()    
    
    # Ask for player names
    player1_name = Entry(Point(100, 50), 10)
    player1_name.draw(win)
    player1_name.setText("Player 1")
    
    player2_name = Entry(Point(400, 50), 10)
    player2_name.draw(win)
    player2_name.setText("Player 2")
    
    # Wait for the user to enter names
    flag = True
    while flag:
        click = win.getMouse()
        if inbetween(click, Point(0, 0), Point(500, 500)):
            flag = False
    
    # Store the player names
    player1 = player1_name.getText()
    player2 = player2_name.getText()
    
    # Remove the name entry boxes from the window
    player1_name.undraw()
    player2_name.undraw()
    
    # Intializes total scores and passcounts.
    total1, total2 = 0, 0
    passcount1, passcount2 = 3, 3
    round_num = 1
    
    # Draw initial score text
    score1_text = Text(Point(100, 75), f"{player1}: 0")
    score1_text.setSize(20)
    score1_text.draw(win)
    
    pass1_text = Text(Point(100, 100), f"Passes: {passcount1}")
    pass1_text.setSize(12)
    pass1_text.draw(win)
    
    score2_text = Text(Point(400, 75), f"{player2}: 0")
    score2_text.setSize(20)
    score2_text.draw(win)
    
    pass2_text = Text(Point(400, 100), f"Passes: {passcount2}")
    pass2_text.setSize(12)
    pass2_text.draw(win)
    
    # While either player has not won yet, the game keeps going.
    
    while total1 < 21 and total2 < 21:
    
        # Draw round number
        
        round_text = Text(Point(250, 25), f"Round {round_num}")
        round_text.setSize(20)
        round_text.draw(win)
    
        # Update and redraw player 1's score and pass count
        
        total1, passcount1 = play_turn(player1, total1, passcount1, win)
        score1_text.setText(f"{player1}: {total1}")
        pass1_text.setText(f"Passes: {passcount1}")
        score1_text.undraw()
        score1_text.draw(win)
        pass1_text.undraw()
        pass1_text.draw(win)
        
        # Checks if player 1 has lost on their turn.
        
        if total1 > 21: 
            
            winner_text = Text(Point(250, 250), f"{player2} wins!")
            winner_text.setSize(30)
            winner_text.draw(win)
            
            win.getMouse()
            win.close()
            
        else: 
    
            # Update and redraw player 2's score and pass count
            
            total2, passcount2 = play_turn(player2, total2, passcount2, win)
            score2_text.setText(f"{player2}: {total2}")
            pass2_text.setText(f"Passes: {passcount2}")
            score2_text.undraw()
            score2_text.draw(win)
            pass2_text.undraw()
            pass2_text.draw(win)
        
            # Undraw round number
            
            round_text.undraw()
        
            # Increment round number
            
            round_num += 1
        
    # Determine winner and display message
    
    if total1 >= 21:
        winner_text = Text(Point(250, 250), f"{player2} wins!")
    elif total2 >= 21:
        winner_text = Text(Point(250, 250), f"{player1} wins!")
    
    winner_text.setSize(30)
    winner_text.draw(win)
    
    win.getMouse()
    win.close()

main()
