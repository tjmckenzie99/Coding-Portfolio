# Todd McKenzie, CS 115 Section 002, tmckenzie0034@uky.edu

from graphics import *

def inbetween(pt1, pt2, pt3):
    
    '''
    Purpose:  detect whether a Point pt2 is between Points pt1 and pt3
       assumes that pt1 is to the left of pt3 (x of pt1 is <= x of pt3)
       and that pt1 is above pt3 (y of pt1 is <= y of pt3)
    Preconditions:  pt1 and pt3 are the boundary Points, forming a rectangle.
       pt2 is the Point which is being tested for "betweenness".
    Postconditions:
       returns True if the Point pt2 lies in the rectangle formed by pt1 and pt3.
          This includes pt2 being exactly ON one side of the rectangle.
       returns False if this is not true.  
    '''

    return (pt1.getX()<=pt2.getX()<=pt3.getX()) and (pt1.getY()<=pt2.getY()<=pt3.getY())

# Purpose: To draw the box and count the number of clicks when the click is
# outside the box.
# Pre-conditions: User clicks inside and outside the box.
# Post-conditions: Either a click is added or the loop ends allowing the user to
# exit.

def main():

    # Prepare window at least 500 by 500
    win = GraphWin("CS 115 Homework 9: Click Counter", 500, 500)
    
    # Prompt user with simple instructions
    instr = Text(Point(250, 50), "Click inside the box to exit")
    instr.draw(win)
    
    # Establish points for upper left and lower right corners of box
    # Q1: HOW do you know which point is upper left and which point is lower right?
    #     the higher the number is, the lower it appears in the graphics window. 
    # ( 2 points )    
    box_ul = Point(200, 200)
    box_lr = Point(300, 300)
    
    # Create and draw rectangle button with those points
    box = Rectangle(box_ul, box_lr)
    box.setFill("Yellow")
    box.draw(win)
    
    # Create point for center of button
    box_center = box.getCenter()
    
    # Place "Yes" text object in the center of the button
    # Q2. HOW will you center it? 
    #     using the box.getCenter() function. ( 2 points )    
    yes_text = Text(box_center, "Yes")
    yes_text.draw(win)
    
    # Create and draw Click Count Text object
    click_count = 0
    click_text = Text(Point(250, 400), "Click Count: " + str(click_count))
    click_text.draw(win)
    
    # Sentinel loop to process clicks
    click_pt = win.getMouse()
    
    while not inbetween(box_ul, click_pt, box_lr):
        click_count += 1
        click_text.setText("Click Count: " + str(click_count))
        click_pt = win.getMouse()
    
    # tell the user to click to close
    close_text = Text(Point(250, 450), "Click to close")
    close_text.draw(win)
    win.getMouse()
    
    # close the window and exit properly
    win.close()

main()