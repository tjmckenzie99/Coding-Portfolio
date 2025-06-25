"""
Program: Payroll for Clean-As-A-Whistle Cleaning Company
Author: Todd McKenzie
Email: tmckenzie0034@uky.edu
Purpose: Calculate payroll and wage for employees
Pre-conditions: User inputs employee data in the format (name, hours worked, hourly rate) separated by commas
Post-conditions: Displays employee wages and total payroll
"""

def calculate_paycheck(data):
    """
    Calculates the amount an employee is paid based on the given data.
    :param data: A list containing the name, hours worked and hourly rate of an employee
    :return: The amount the employee gets paid (float)
    """
    name, hours, rate = data
    return float(hours) * float(rate)

def main():
  
    # Print the initial titles
    print('Payroll for Clean-As-A-Whistle Cleaning Company')
    print('Enter Employee Information ( Name, hours worked, hourly rate) separated by commas')
    print('Press Enter to stop Entering Employee Information')

    # Initialize variables
    sum_wages = 0
    employee_data = []

    # Start the loop to collect employee data
    employee_info = input('Enter Employee Info:')
    while employee_info != "":
        data = employee_info.split(',')
        wage = calculate_paycheck(data)

        # Add to the total wages and store employee data in a list
        sum_wages += wage
        employee_data.append([data[0], wage])

        employee_info = input('Enter Employee Info:')

    # Print employee wages and total payroll
    print('\nEmployees with Paychecks')
    for data in employee_data:
        print(f"{data[0]} ${data[1]:.2f}")
    print(f"\nTotal Payroll ${sum_wages:.2f}")

main()

# Test Cases

# Test Case 1
# Martha $1200.00
# Jim $300.00
# Carl $500.00
# Total Payroll $2000.00

# Test Case 2
# Total Payroll $0
