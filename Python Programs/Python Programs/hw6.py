
# Todd McKenzie, CS 115 Section 002, tmckenzie0034@uky.edu
# Purpose: To calculate the pay someone would get depending on doodads and overtime
# Pre-conditions: The user inputs how many days the employee worked and their doodads worked.
# Post-conditions: The user is presented with the doodads, pay, and extra pay (if applicable.)

def main ():
    
    print('Dudley Doodad Payroll')
    print('')
    
    # Allow user to input pay rate and days worked
    
    employee_name = str(input("Enter name of employee:"))
    doodad_rate = float(input("Enter rate per doodad:"))
    days_worked = int(input("How many days worked this week?"))
    
    # Intitalize variables
    
    days = 0
    
    doodads = 0
    
    total_doodads = 0
    
    # Determines if any days were worked.
    
    if (days_worked > 0):
        
        # While loop. Prompts user with how many doodads worked each day depending on the
        
        while (days_worked > days):
            
            days = (days + 1)
            
            doodads = int(input('Doodads done on Day {:.0f}:?'.format(days)))
            
            total_doodads = (total_doodads + doodads)  
            
        #Used to calculate overtime pay based on if the user worke over 65 hours.
            
        if (total_doodads > 65):
                
            total_doodads_over = total_doodads - 65
                
            overtime = total_doodads_over * 1.3
            
            extra_doodad_pay = doodad_rate * total_doodads_over * 1.3
                
            complete_total = (65 * doodad_rate) + (total_doodads_over * 1.3 * doodad_rate)
                
            #If overtime was worked displays total doodads, extra pay from said doodads, and the employee pay and their name.   
                
            print('')
            print('Total doodads done: {:.0f}'.format(total_doodads))
            print('Extra doodad pay ${:.2f}'.format(extra_doodad_pay))
            print('The pay for',employee_name,'is ${:.2f}'.format(complete_total))                 
                
        else:
            
            #If overtime was not worked total pay and doodads calculated.
                
            complete_total = total_doodads * doodad_rate
            print('')
            print('Total doodads done: {:.0f}'.format(total_doodads))
            print('The pay for',employee_name,'is ${:.2f}'.format(complete_total))                
                          
        
    else:
        
        #Displays 0 for everything if the person did not work any days.
        
        print('')
        print('Total doodads done: 0')
        print('The pay for',employee_name,' is $0.00')        
                  
if __name__ == "__main__":
        main()
    
# Expected Outcomes
# 1. Total Doodads: 20, Extra Pay: N/A, Payday: $450.
# 2. Total Doodads: 109, Extra Pay: $1287.00, Payday: $2749.50.
# 3. Total Doodads: 135, Extra Pay: $1820.00, Payday: $3120.00.
# 4. Total Doodads: 35, Extra Pay: N/A, Payday: $647.50.