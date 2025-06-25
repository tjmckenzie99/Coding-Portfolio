# Names: Evan Kalb, Todd McKenzie
# Purpose: To calculate the amout paid to a loan
# Pre-cond: The user inputs amout, rate, and number of years.
# Post-cond: The user is presented the payment amount per period.

def main():

    #1. Print title
    
    print('Inflated Payment Calculator')
    print(' ')
    
    #2. Get inputs from user (principal, number years, interest rate)
    
    loan_amount = float(input('Enter initial amount of loan:'))
    
    num_years = float(input('Number of years to pay back loan:'))
    
    interest_rate = float(input('Interest rate per year (%):'))
    
    #3. Convert annual percentage rate to monthly rate
    
    month_percent_rate = (interest_rate/100)/12
    
    #4. Convert years to months
    
    num_months = (num_years * 12)
    
    #5. what? (5 points)
    
    pay_amount1 = ((month_percent_rate) * (1 + month_percent_rate) ** (num_months))
    pay_amount2 = ((1 + month_percent_rate) ** num_months) - 1                     
    
    pay_amount = (loan_amount * (pay_amount1/pay_amount2))
                                  
    #6. what? (5 points)
    
    print(f'Payment is ${pay_amount:.2f}')

if __name__ == "__main__":
    main()

# $117.80
# $1330.60
# $60540211602.40
# $0.08
# Cant divide by 0