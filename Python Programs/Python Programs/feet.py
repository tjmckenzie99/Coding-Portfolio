# Prolog
# Author:  Todd McKenzie
# Email:  tmckenzie0034@uky.edu
# Section: 002
'''
  Purpose: 
      convert feet to inches, using fact that there are 12 inches in 1 foot
  Pre-conditions (input): 
      number of feet (floating point)
  Post-conditions (output): 
      number of inches, floating point with 2 decimals rounded
'''

def main():
# Design and implementation

    #  1.  Output a message to identify the program, and a blank line
    print("Conversion of feet to inches")
    print()

    #  2.  Input amount of feet from user
    feet = float(input("How many feet? "))
    #  3.  Calculate number of inches
    # 12 inches in one foot
    inches = feet * 12

    #  4. Output resulting inches and given number of feet
    print()
    print(feet, "feet is {:.2f} inches".format(inches))

main()
# end of program file

# 1. State what the syntax error was, for example, "it was missing a semicolon".

# There was a missing parathesis. 

# 2. Copy and paste into the comment the error message you got for the error. 
# The error message is in the Shell window. The last line of the error message 
# is the most important; make sure you get that one. The other info starting at 
# "Traceback" can be useful. Copy those also.

# Syntax Error: '(' was never closed: <string>, line 22, pos 17

# 3. Describe how you fixed the syntax error.

# I added the missing parathesis.

# 4. What is the semantics (logic) error? NOT just that "the answer is wrong". 
# Why is the answer wrong? Be specific.

# There was addition instead of a multiplication sign

# 5. State what line the semantics error was on in the program.

# Line 25

# 6. State how you fixed the semantics (logic) error.

# Changed the sign