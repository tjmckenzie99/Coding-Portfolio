# Purpose: To calculate the height of tree with the information input.
# Pre-cond: The user inputs the angle of elevation, distance from the tree,
# and your height.
# Post-cond: The user is presented the height of the tree.

# use math library for radians function needed to convert input angle to radians
# and tan function used to calculate height

# Indented design below is within main() definition
def main():
    
    # print title and blank line
    
    print('Finding the height of a tree on level ground')
    print(' ')

    # get 3 input values, angle of elevation, distance to base and height of observer
    
    angle = float(input('Angle of elevation to top of tree (deg):'))
    distance = float(input('Distance to the base of tree (ft):'))
    height = float(input('Height of your eyes (ft):'))
    
    
    if angle < 0:
        
        raise ValueError('This number is invalid. Please convert your value into positive angle units')
    
    if angle > 89.99: 
        
        raise ValueError('Angle does not make sense. Please enter a value of 90 or lower.')
    
    # COMPLETE the steps needed here
    
    import math
    
    pi = 3.14159265359
    
    radian = angle * (pi/180)
    
    tree_height = (distance * math.tan(radian) + height)

    # report resulting height, using 2 decimals
    
    print('The height of the tree is {:.2f} feet'.format(tree_height))
    
if __name__ == "__main__":
    main()
    
# Normal case, integers
# Inputs: 45, 40, 5
# Outputs: 45.00 feet

# Normal case, floats
# Inputs: 35.0, 122.5, 4.9
# Output: 90.68 feet

# Point of view at base of tree
# Inputs: 89, 0, 4.8
# Output: 4.80 feet

# Negative Angle
# Inputs: -6, 90, 5.2
# Output: An error message because a tree being 354 degree in angle makes
# no sense. Only should go up to 89.99 degrees.
