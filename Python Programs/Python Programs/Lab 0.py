# Prolog
# Author:  YOUR NAME
# Email:  YOUR EMAIL @uky.edu
# Section: YOUR SECTION
# Date: 1/9/2023
'''
  Purpose: to find the circumference and area of a circle given the diameter. 
  Preconditions: (input)
    User supplies the diameter as float number
  Postconditions: (outputs)
    User greeted and prompted for input of the diameter 
    Circumference and area of the circle is reported
  Reference https://www.mathsisfun.com/geometry/circle.html
    for formula of circumference and area

'''
from math import pi  # the famous 3.14159... to 15 places!

def main():
# Design and implementation

   #  1.  Output a message to identify the program
   print("Calculating circumference and area of a circle\n")

   #  2.  Input diameter from user
   diameter = float(input("Enter diameter (m): "))

   #  3.  Calculate radius from diameter, half the diameter
   radius = diameter / 2

   #  4.  Calculate area  in square meters
   area = pi * radius ** 2   # ** means raise to a power

   #  5.  Calculate the circumference of the circle (in meters)
   circum =  pi *  diameter  

   #  6. Output resulting circumference, area, and inputs 
   print()
   print("The radius of a circle with a diameter of {:.3f} m".format(diameter))
   print("is {:.3f} m".format(radius))
   print()
   print("The circumference of the circle is {:.3f} m".format(circum),
       "and the area is {:.3f} square m".format(area))

main()
# end of program file