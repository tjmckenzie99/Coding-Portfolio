# Team 2, Section 2, Gabriel Gesteira, Todd McKenzie, and Evan Kalb
# Purpose: To estimate pi using the Monte Carlo method
# Pre-conditions: The user inputs the number of darts and time taken.
# Post-conditions: The user is presented with approximation of pi and error for approximation.

import math

import random

from time import process_time

def main ():
    
    # Prints titles
    
    print('Estimating pi with the Monte Carlo method')
    print('')
    
    # Intialize variables
    
    darts = 0
    
    inside_circle = 0
    
    outside_circle = 0
    
    # Input value for number of darts

    num_darts = int(input('How many darts for this simulation?'))
    print('')  
    
    # for loop that calculates darts inside the circle.
    
    for darts in range(1,num_darts + 1):
        
        # Creates random x value for circle formula
    
        randi_x = random.uniform(0, 1)
        
        # Creates random y value for circle formula
    
        randi_y = random.uniform(0, 1)
        
        # Plugs values in for circle formula and calculates the answer.
        
        circle_formula = (randi_x) ** 2 + (randi_y) ** 2
        
        # If number does match circle formula adds it to numbers that fall inside the circle.
        
        if (circle_formula < 1):
            
            inside_circle = inside_circle + 1
            
    # Calculates CPU time
            
    time = process_time()
            
    # Prints CPU time
    
    print('Time taken: {:.3f} seconds'.format(time))
    
    # If it takes longer than 60 seconds or equal to 60 seconds, calculates
    # time in minutes and seconds.
    
    if time >= 60:
        
        # Gets time in minutes with decimals
        
        deci_time = time / 60
        
        # Rounds down to get a value to calculate seconds
        
        min_time = math.trunc(deci_time)
        
        # Gets seconds in decimal form.
        
        deci_seconds = deci_time - min_time
        
        # Calculates seconds.
        
        seconds = 60 * deci_seconds
        
        # Prints minutes and seconds.
    
        print('or {:.1f} minutes and {:.3f} seconds'.format(min_time,seconds))
    
    print('')
    
    # Calculates the approximation for pi.
    
    approx_pi = (float(inside_circle) / num_darts) * 4
    
    # Displays the approximation for pi.
    
    print('Approximation to pi is {:.9f}'.format(approx_pi))
    print('')
    
    # Calculates the error for pi.
    
    error_pi = math.pi - approx_pi
    
    # Prints error for approximation
    
    print('Error for this Approximation: {:.9f} - {:.9f} = {:.9f}'.format(math.pi, approx_pi, error_pi))
    
main()