# Todd McKenzie, CS 115 Section 002, tmckenzie0034@uky.edu
# Purpose: To determine the which years are leap years.
# Pre-conditions: The user inputs the start and end years
# Post-conditions: The user is presented with all the leap years.

def main():
    print('To leap or not to leap')
    print(' ')
    
    start = int(input("Please enter the first year:"))
    end = int(input("Please enter the last year:"))    
    
    print(' ')  
    
    # If start year is entered the typical way.
    if start < end:
        print('Leap Years identified inclusively between',start,'and', end, '.')
        
        print(' ')
        
        # Basic iterating loop
        
        for year in range(start, end):
            
            if (0 == year % 4) and (0 != year % 100) or (0 == year % 400):
                
                print (year)
    
    # If the start and end year are entered backwards.        
    else: 
        
        #swaps years
        
        start, end = end,start
    
        print('Leap Years identified inclusively between',start,'and', end, '.')
        
        print(' ')
        
        # Basic iterating loop
        
        for year in range(start, end):
        
            if (0 == year % 4) and (0 != year % 100) or (0 == year % 400):
            
                print (year)
                
            
if __name__ == "__main__":
    main()
    
# 1980 to 1984
# 1980

#1980 to 1988
#1980
#1984

#1976 to 1988
#1976
#1980
#1984

#1974 to 1980
#1976


