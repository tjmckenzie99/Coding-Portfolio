# prolog
# Todd McKenzie, CS 115 Section 002, tmckenzie0034@uky.edu
# Purpose: Calculate the equivalent number of miles, feet and yards from kilometers.
# Preconditions: The user provides kilometer values for input.
# Postconditions: The user will be presented that value is miles, feet, and yards.

   # 0. Defining Main 

def main():
   
   # 1. Get needed data from the keyboard, the number of kilometers. 
   
   kilo = float(input('Enter kilometers:\n'))
   
   # 2. Calculate the equivalent miles. 
   
   miles = kilo * 0.621371
   
   # 3. Calculate the equivalent number of feet.
   
   feet = miles * 5280
   
   # 4. Calculate the equivalent number of yards.
   
   yards = miles * 1760
   
   # 5. Print blank line
   
   print(' ')
   
   # 6. Output the input kilometers with label and 3 places.
   # 7. Output the miles with label and 3 places.
   # 8. Output the yards with label and 3 places.
   # 9. Output the feet with label and 3 places.
   
   print(kilo, 'kilometers is', miles, 'miles, which is', yards, 'yards or', feet, 'feet.')
   
if __name__ == "__main__":
   main()
  
   
# Action Plan:  
   
# Normal, integer kilometers
# Input Kilometers: 5
# Expected Result: 3.11 miles, 16404.1944 feet, or 5468.0648 yards

# Normal, float kilometers: 12.5
# Input Kilometers: 12.5 
# Expected Result: 7.77 miles, 41010.486 feet, or 13670.162 yards

# Boundary, zero kilometers
# Input Kilometers: 0
# Expected Result: 0 miles, 0 feet, or 0 yards

# Scientific notation kilometers
# Input Kilometers: 6e3
# Expected Result: 3738.226 miles, 19685033.28 feet, or 6561677.76 yards


      