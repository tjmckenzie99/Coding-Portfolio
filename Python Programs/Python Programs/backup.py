# Todd McKenzie, CS 115 Section 002, tmckenzie0034@uky.edu
# Purpose: To calculate the GPA and grades.
# Pre-conditions: The user inputs number of classes, the grade, and credit hours
# Post-conditions: The user is presented with GPA, total credit hours, and total quality points.

def main ():
    
    print('Semester grades and status for one student')
    print('')
    
    quality_points_grade = {"A":4,"B":3,"C":2,"D":1,"E":0}

#Intialize variables

    classes = 0
    
    quality_points = 0
    
    credits = 0
    
    total_credits = 0
    
#Inputs number of classes
    
    num_classes = float(input("Input number of classes for this student:"))
    
#If there are any classes
    
    if (num_classes > 0):
        
#While loop to display the letter grade and credit hours.
        
        while (num_classes > classes):
            
            classes = (classes + 1)
            
            print('Please enter information for class {:.0f}'.format(classes))
            letter = str(input(" letter grade?"))
            credits = float(input(" credit hours?"))
            
            if (letter == "A" or letter == "a"):
                
                quality_points += quality_points_grade['A'] * credits
                total_credits = total_credits + credits 
                
            elif (letter == "B" or letter == "b"):
                    
                quality_points += quality_points_grade['B'] * credits
                total_credits = total_credits + credits 
                
            elif (letter == "C" or letter == "c"):
                        
                quality_points += quality_points_grade['C'] * credits
                total_credits = total_credits + credits 
                
            elif (letter == "D" or letter == "d"):
                            
                quality_points += quality_points_grade['D'] * credits
                total_credits = total_credits + credits 
                
            elif (letter == "E" or letter == "e"):
                                
                quality_points += quality_points_grade['E'] * credits
                total_credits += credits 
                
            else:
                
                print('*** No quality points awarded for invalid grade ***')
                print('')
                total_credits += credits 
                
        if (total_credits > 0):
    
            gpa = quality_points / total_credits
            
            print('')        
            print('Total Quality Points:{:.2f}'.format(quality_points))
            print('Total Credit Hours:{:.2f}'.format(total_credits))
            print('Grade Point Average:{:.2f}'.format(gpa))
        
            if (gpa > 3.5 and total_credits >= 12):
                
                print("Dean's List")
                
            elif (gpa < 2.0):
                
                print('Academic Probation')
            
        else:
        
            print('')        
            print('Total Quality Points:0.00')
            print('Total Credit Hours:{:.2f}'.format(total_credits))
            print('Grade Point Average: 0.00')
                                                         
    else:
        
        print('')
        print('No classes entered')
                   
main()            
    
#Test Cases
#1.
#Inputs: 5,A,3,B,1,D,2,C,3,E,2
#Outputs: 23, 11, 2.09
#2. 
#Inputs: 4,A,4.5,B,2.5,A,4,A,3
#Outputs: 49.50, 13.00, 3.81, Dean's List
#3.
#Inputs: 4,B,2,C,4,D,3,D,1
#Outputs: 18.00, 10.00, 1.80, Academic Probation
#4.
#Inputs: 3,a,4,b,4,c,4    
#Outputs: 36.00, 12.00, 3.00
#5.
#Inputs: 1,C,3
#Outputs: 6.00, 3.00, 2.00
#6.
#Inputs: 2,P,6,B,3
#Outputs: *** No quality points awarded for invalid grade ***
#7. 
#Inputs: 0
#Outputs: No classes entered