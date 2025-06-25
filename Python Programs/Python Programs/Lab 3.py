# Names: Evan Kalb, Todd McKenzie
# Purpose: Enter the coordinates of the three points and then calculate the 
# perimeter and the area of the triangle with given coordinates
# Pre-cond: The user inputs given coordinates X1,Y1, X2, Y2, X3, Y3.
# Post-cond: The user is presented with the perimeter and area of the triangle.

import math

def main():

    #1. Print title, blank line and instructions
    
    print('Triangle Geometry')
    print(' ')
    
    #2. Get 6 inputs from user, a pair for each corner (x,y,x,y,x,y)
    x1 = float(input('x1:'))
    y1 = float(input('y1:'))
    
    print('Second Corner ----')
    x2 = float(input('x2:'))
    y2 = float(input('y2:'))
    
    print('Third Corner -----')
    x3 = float(input('x3:'))
    y3 = float(input('y3:'))
    
    #3. Calculate the distances between each pair of points (lengths of sides)
    
    distance_a = math.sqrt((x2-x1) ** 2 + (y2-y1) **2)
    distance_b = math.sqrt((x3-x2) ** 2 + (y3-y2) **2)
    distance_c = math.sqrt((x3-x1) ** 2 + (y3-y1) **2)
    
    semi_perimeter = (distance_a + distance_b + distance_c)/2
    
    perimeter = (distance_a + distance_b + distance_c)
    
    area = math.sqrt(semi_perimeter*(semi_perimeter-distance_a)*(semi_perimeter-distance_b)*(semi_perimeter-distance_c))
    
    print(f'The perimeter of your triangle is {perimeter:.3f}')
    print(f'The area of your triangle is {area:.3f}')
    
if __name__ == "__main__":
    main()
    
# P = 11.7733, A = 6.000 - A
# P = 16.719, A = 11.000 - B
# P = 1990.138, A = 3725 - C
# P = 3.414, A = 0.500 - D
# P = 0.000, A = 0.000 - E
# P = 19.799, A = 0.000 - F