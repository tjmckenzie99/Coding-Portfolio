# Todd McKenzie, CS 115 Section 002, tmckenzie0034@uky.edu

# Purpose: This function determines the friendliness of the first and second
# value. Friendliness is if the sum of the factors or the number divided by the
# original number.
# Pre-conditions: The sum of the factors divided by the original number is
# needed.
# Post-conditions: The friendilness value is returned.

# Defines how the friendliness is calculated.

def friendliness_val(first_number, second_number):
    
    # Calculates the sum of the numbers divided by the original. 
    
    sum_num1 = factors(first_number)/first_number
    sum_num2 = factors(second_number)/second_number
    
    # Determines if the two numbers are friendly.
    
    if (sum_num1 == sum_num2):
        
        friend_val = True
        
    else:
        
        friend_val = False   
        
    # Shows what is the "result" of this defined function.    
        
    return friend_val

# Purpose: This function determines the factors and sums them up.
# Pre-conditions: The first and second number are needed.
# Post-conditions: The sum of the factors is returned.

# Defines factoring and summing function.

def factors(x):
    
    # Intializes sum_num
    
    sum_num = 0
    
    # Determines the factors
    
    for i in range(1, x + 1):
        
        if x % i == 0:
            
    # Sums up the factors
            
            sum_num = sum_num + i
            
     # Shows what is the "result" of this defined function.
            
    return sum_num

# Purpose: This function displays the title and allows inputs for the first and
# second number and prevents negative values.
# Pre-conditions: The user inputs the two values
# Post-conditions: The user is presented with if the numbers are friendly or
# not.

# Defines main

def main():
    
    # Print titles
    
    print('Divisible Number Calculator')
    print()
    
    # Asks user for first number
    
    first_number = int(input("Enter first number:"))
    
    # Determines if the first number is greater than 0 and if it is not makes
    # the user input the value again.
    
    while first_number <= 0:
        
        print("Please enter a number greater than zero")
        first_number = int(input("Enter first number:"))
        
    # Asks user for second number
    
    second_number = int(input("Enter second number:"))
        
    # Determines if the second number is greater than 0 and if it is not makes
    # the user input the value again.        
    
    while second_number <= 0:
        
        print("Please enter a number greater than zero")
        second_number = int(input("Enter first number:"))
    
    print()
    
    # Determines if the friend value is true or not and prints the answer
    # accordingly.
    
    friend_val = friendliness_val(first_number, second_number)
    
    if friend_val == True:
        
        print(first_number, "and", second_number, "are friendly")
        
    elif friend_val == False:
        
        print(first_number, "and", second_number, "are not friendly")
        
main()

# Test Case Factors:
# 13, 14
# 25, 31
# 221, 252

# Test Case Friendliness:
# 80, 200: Friendly
# 12, 15: Not Friendly

# Test Case Main Function
# 30, 140: Friendly
# 120, 150: Not Friendly
# 0: Rejects Value
