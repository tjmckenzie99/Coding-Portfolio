# Todd McKenzie, CS 115 Section 002, tmckenzie0034@uky.edu
# Purpose: To take employees names and numerical values to display payroll and
# wage.
# Pre-conditions: User inputs employee data.
# Post-conditions: User is present with wages and total payroll.

def main():
    
    # Prints all initial titles 
    
    print('Payroll for Clean-As-A-Whistle Cleaning Company')
    print('Enter Employee Information ( Name, hours worked, hourly rate) separated by commas')
    print('Press Enter to stop Entering Employee Information')
    
    # Sets up the storage of employee data and the starts the while loop.
    
    sum_wages = 0
    employee_data = []
    employee_info = input('Enter Employee Info:')
    
    # Sets it up where the while loop continues until nothing is entered
    
    while employee_info != "":
        
        # Makes it where the information can be intepreted as three seperate
        # numbers.
        
        name, hours, rate = employee_info.split(',')
        
        # Makes hours into integer
        
        hours = float(hours)
        
        # Makes rate into integer
        
        rate = float(rate)
        
        # Calculates the wage
        
        wage = hours * rate
        
        # Calculates the sum of wages
        
        sum_wages += wage
        
        # Stores the employees data in a table
        
        employee_data.append({'name': name, 'hours': hours, 'rate': rate, 'wage': wage})
        
        # Allows input of information
        
        employee_info = input('Enter Employee Info:')
        
    # Prints the end result
    
    print('')
    print('Employees with Paychecks')
    
    # Uses the table for the final display
    
    for employee in employee_data:
        
        # Pulls employee name from table
        
        name = employee['name']
        
        # Pulls employee wage from table
        
        wage = employee['wage']
        
        # Print the wage and name
        
        print(name, '${:.2f}'.format(wage))
        
    # Print sum of the wages
        
    print('')
    print('Total Payroll {:.2f}'.format(sum_wages))
        
        
main()