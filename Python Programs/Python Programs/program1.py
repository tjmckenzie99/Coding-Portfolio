# Todd McKenzie, CS 115 Section 002, tmckenzie0034@uky.edu
# Purpose: To calculate the area in square milimeters and how many dies you can cut.
# Pre-conditions: The user inputs the diameter of the wafer and the area of a single die.
# Post-conditions: The user is present the area in square milimeters.

# import pi and sqrt 

from math import sqrt

from math import pi

from math import trunc

# define main

def main():

# Display the title
    
    print('--- Wafer Fabrication Economics ---')
    print('')
    
# Set up the inputs for the diameter of the wafer and the area of a single die.
    
    wafer_diameter = float(input("What is the diameter of the wafer? (mm)"))
    die_area = float(input("What is the area of a single die? (mm^2)"))
    
# Set up intial if and else statement stating that if a value is below or at 0 it will display
# that the value is nonsensical.      
    
    if (die_area > 0):
        
# Calculate the wafer area using pi and the radius (1/2d).
        
        wafer_radius = (1/2)*(wafer_diameter)
        
        wafer_area = pi*((wafer_radius)**2)
        
# Calculate the dies per wafer. NOTE TO SELF: No decimal points (cant cut half a die)
        
        die_per_wafer = (((wafer_area)/(die_area))-((pi*(wafer_diameter))/((sqrt(2*die_area)))))
        no_deci_wafer = trunc(die_per_wafer)
        
# Display dies per wafer and area in final statement.
        
        print('')
        print('From a wafer with area',f'{wafer_area:.3f}','square millimeters, you can cut',f'{no_deci_wafer:.0f}','dies.')
        
        
# Display warning that it does not account for defects etc.
        
        print("This does not take into account defective dies, alignment markings and test sites on the wafer's")
        
        
    else:
        
        print('')
        print('Invalid die area value. No dies possible.')


#Test Cases:
# A: 31415.926, 1167
# B: 70685.835, 865
# C: 17671.459, 1319

if __name__ == "__main__":
    main()