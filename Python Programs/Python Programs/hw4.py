'''
Prelog: Todd McKenzie, CS 115 Section 002
Purpose:  offer the user a choice of food items, calculate total bill
Pre-conditions:  user enters 5 or 6 y's or n's depending on desired items (strings)
Post-conditions:  prompts for choices, total bill before (float) and after 20% tip, (float)
    and parting message.
'''
def main():
    
    # name of food vendor
    
    print("Welcome to Chuy's")
    print('Please answer each question with y or n')

    # give user instructions of expected inputs
    
    food_cost = {"chi_boom_boom":14.09,"chi_flaunt":11.86,"crisp_tacos":11.44,"quesadilla":8.49,"quesadilla_guac": 10.93,"tres_leches":9.00}
    
    
    # initialize total bill to zero
    
    total_bill = 0
    
    # ask first choice
    # if the user desired the item, 
        #add price to total bill
        
    x = (input('Would you like to try our Chicka-Chicka Boom-Boom?'))
    
    if x == "y":
    
        total_bill += food_cost['chi_boom_boom']
        
    x = (input('Can I get you some Chicken Flautas?'))
    
    if x == "y":
    
        total_bill += food_cost['chi_flaunt']
        
    x = (input('How about Crispy Tacos?'))
    
    if x == "y":
        
        total_bill += food_cost['crisp_tacos']
        
    x = (input('Can I interest you in some Quesadillas?')) 
        
    if x == "y": 
        
        x = (input('Would you like a Quesadilla with Guac?'))
        
        if x == "y":
        
            total_bill += food_cost['quesadilla']
        
        if x == "n":
            
            total_bill += food_cost['quesadilla_guac']
        
    x = (input('Would you like to try our Tres Leches?')) 
    
    if x == "y":
        
        total_bill += food_cost['tres_leches']

# complete the design for the rest of the menu

    print(' ')

    # output blank line
    
    print(f'The total for your food is ${total_bill:.2f}')
    
    # output total bill before 20% tip 
    
    tip_bill = total_bill * 1.20
    
    print(f'Your total with 20% tip is ${tip_bill:.2f}')
    
    print('Thanks for choosing to eat with us today!')
    
   
# complete rest of design

if __name__ == "__main__":
    main()

# $25.95, $31.14
# $11.86, $14.23
# $10.93, $13.12
# $37.39, $44.87
# $0.00, $0.00
# $54.88, $65.86