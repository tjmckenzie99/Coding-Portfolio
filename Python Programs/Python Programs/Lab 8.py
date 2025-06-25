# Prolog
# Gabriel Gesteira, Ethan Kalb, Todd McKenzie
#Purpose:
#Engage the user in a Guessing game of "Find the March Madness Champion."
#Pre-conditions (input):
#User provides sets of x and y coordinates by clicking the screen.
#Post-conditions (output):
#Program randomly generates the coordinates of the March Madness Champ hence informing the user
#of their distance from the Champ for each click, as well as their total
#number of Guesses. User either wins or looses within 15 guesses

# Import graphics library
# Import random
from graphics import *
from random import randrange
def main():

 # Set up the graphics window
    win = GraphWin ("March Madness - Find the champion", 500, 500)
    win.setCoords (0, 0, 500, 500)
    win.setBackground("black")

 # Generate the random coordinates for the champion.
    Champ = Point(randrange(0, 500), randrange(0, 500))

 # Prompt the user to find the Champ by clicking
    Click = Text(Point(250, 250), "Click to find the champion")
    Click.setSize(18)
    Click.setTextColor("white")
    Click.draw(win)

 # Display distance from the Champ for each click
    dist_indicator = Text(Point(250, 150), "distance")
    dist_indicator.setSize(18)
    dist_indicator.setTextColor("white")
    dist_indicator.draw(win)

 # Display total number of Guesses
    Guesses_counter = Text(Point(250, 75), "Guesses")
    Guesses_counter.setSize(15)
    Guesses_counter.setTextColor("white")
    Guesses_counter.draw(win)

 # Initialize Guesses counter to zero, increment Guesses counter based on distance.
    Guesses_num = 0
    Guesses = win.getMouse()
    Guesses_num += 1

 # An orange circle is drawn around the user's click, and the distance between
 # the user's click and the Champ is calculated using the distance formula.
    drawPoint(Guesses, "orange", win)
    Guesses_dist = int(distance(Guesses, Champ))

 # Until either the user's Guesses is within ten pixels of the Champ, or they
 # have used all of their 15 Guesses,
    while Guesses_dist > 10 and Guesses_num < 15:

 # Distance label is updated to match current distance to Champ
        dist_indicator.setText("Distance " + str(Guesses_dist))

 # Guesses label is updated to match current number of Guesses
        Guesses_counter.setText("Guesses: " + str(Guesses_num))


 # The user clicks the screen to input their next Guesses, which is marked
 # by an orange circle, and Guesses is assigned to this new coordinate.
 # The Guesses counter is incremented.
        Guesses = win.getMouse()
        Guesses_num += 1
    

        # Guesses_dist is updated to match the user's current distance to the Champ.
        Guesses_dist = int(distance(Guesses, Champ))
       
       
        # The user's distance to the Champ is redrawn to match final Guesses
        dist_indicator.setText("Distance " + str(Guesses_dist))
       
        # The user's number of Guesses is redrawn to match their final Guesses
        Guesses_counter.setText("Guesses: " + str(Guesses_num))
       
        # The Champ's loChampion is revealed, as it is marked by a white circle.
        drawPoint(Guesses, "orange", win)
    
 # If the user won the game, meaning they Guessed within ten pixels of
 # of the Champ's loChampion in at most 15 Guesses,
    drawPoint(Guesses, "white", win)
    
    if Guesses_dist <= 10:

 # The user is given a victory message, and told it is their lucky day.
        Click.setText("YOU FOUND THE Champ!!\n It's your lucky day\n Click to Close")

 # Otherwise,
    else:

 # The user is given a losing message, and wished better luck next time.
        Click.setText("YOU DIDN'T FIND IT!!\n Better luck next time\n Click to Close")

 # Wait for a click from the user before closing the window.
    win.getMouse()
    win.close()

def distance (pt1, pt2):
#purpose: calculate the distance between 2 graphics Points
#pre-conditions: two Point objects
#post-conditions: returns distance using distance formula
    return ((pt1.getX() - pt2.getX())**2 + (pt1.getY() - pt2.getY())** 2) ** 0.5


def drawPoint(pt, color, win):
#purpose: draw a Circle of radius 6 at location given by pt with the color specified on the GraphWin win
#pre-conditions: pt is a Point object which acts as center of circle, color is string, win is GraphWin object used to draw on
#post-conditions: a colored Circle of radius 6 is drawn on win, center at location given by pt
    c = Circle(pt, 6)
    c.setFill(color)
    c.draw(win)
    
main()