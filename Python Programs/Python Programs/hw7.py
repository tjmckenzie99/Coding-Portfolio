# Todd McKenzie, CS 115 Section 002, tmckenzie0034@uky.edu
# Purpose: To create a card for someones birthday
# Pre-conditions: The user inputs their name.
# Post-conditions: The user is presented with my poorly drawn birthday 
# card with their name at the top.

from graphics import *

def main():

    # Creates the window for application
    window = GraphWin("Happy birthday!", 500, 600)

    # Allows user to input their name in.
    prompt = Text(Point(250, 50), "Please enter your name:")
    
    # Draw prompt
    prompt.draw(window)

    # Creates the input box
    input_box = Entry(Point(250, 100), 20)
    # Makes the text blank
    input_box.setText("")
    # Draws the input box
    input_box.draw(window)
    # Gets the mouse to advance
    window.getMouse()
    # Gets the input box name
    name = str(input_box.getText())

    prompt.undraw()
    input_box.undraw()

    # Show happy birthday text with the name
    birthday = Text(Point(250, 60), "Happy birthday!")
    # Show name as inputted in input box
    print_name = Text(Point(250, 80), name)
    # Draw happy birthday text in the frame
    birthday.draw(window)
    # Draw name text in the frame
    print_name.draw(window)

    # Closes window text
    close_text = Text(Point(55, 10), "Click to close window")
    close_text.draw(window)

    # Defines the first line for balloon the first balloon
    line1 = Line(Point(300, 300), Point(300, 500))
    # Draws the line
    line1.draw(window)

    # Defines the balloon circle for the first balloon.
    balloon1 = Circle(Point(300, 250), 50)
    # Fills the balloon with pink
    balloon1.setFill("pink")
    # Draws the circle
    balloon1.draw(window)

    # Defines the second line for the second balloon 
    line2 = Line(Point(100, 300), Point(100, 500))
    # Draws the second line
    line2.draw(window)

    # Define balloon number 2
    balloon2 = Oval(Point(150, 300), Point(50, 150))
    # Set oval to red
    balloon2.setFill("red")
    # Draw a oval
    balloon2.draw(window)
    
    # Defines the third line for the third balloon 
    line3 = Line(Point(100, 500), Point(100, 600))
    # Draws the third line
    line3.draw(window)

    # Define balloon number 3
    balloon3 = Oval(Point(150, 500), Point(50, 350))
    # Set oval to purple
    balloon3.setFill("purple")
    # Draw a oval
    balloon3.draw(window) 
    
    # Defines the fourth line for balloon the fourth balloon
    line4 = Line(Point(400, 250), Point(400, 700))
    # Draws the line
    line4.draw(window)
   

    # Define balloon number 4
    balloon4 = Oval(Point(450, 400), Point(350, 250))
    # Set oval to green
    balloon4.setFill("green")
    # Draw a oval
    balloon4.draw(window)    

    # Defines the rectangle
    rectangle = Rectangle(Point(150, 400), Point(250, 300))
    # Fills the rectangle with blue
    rectangle.setFill("blue")
    # Draws the rectangle
    rectangle.draw(window)

    # Closes the window
    window.getMouse()
    window.close()

main()