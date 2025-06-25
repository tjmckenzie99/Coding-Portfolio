# Todd McKenzie, CS 115 Section 002, tmckenzie0034@uky.edu

def main():
  
    print('Lexington Electric Company Batch Billing')
    print('')  
    
    total_bill = 0
    
    customers = 0
    
    total_electric = 0
    
    num_customers = int(input("How many customers to process?"))
    
    if num_customers >= 1:
    
        for students in range(1,num_customers + 1):
        
            customers = customers + 1
        
            print('Processing customer {:.0f} ------'.format(customers))
        
            electric = float(input('Enter electricity used (kWh):'))
        
            type_service = str(input('Type of service (G or R):'))
        
            if (type_service == 'R'):
            
                print('Rate is $0.11704 per kWh')
            
                bill = electric * 0.11704
            
                print('Bill is ${:.2f}'.format(bill))
                print('')   
            
                total_bill = total_bill + bill
                
                total_electric = total_electric + electric
            
            elif (type_service == 'G'):
            
                print('Rate is $0.18483 per kWh')
            
            
                bill = electric * 0.18483
            
                print('Bill is ${:.2f}'.format(bill))
            
                print('')
            
                total_bill = total_bill + bill
                
                total_electric = total_electric + electric
                
            else:
                
                print('<< Invalid : Using General Three Phase rate >>')
                print('')
                
                print('Rate is $0.18483 per kWh')
            
            
                bill = electric * 0.18483
            
                print('Bill is ${:.2f}'.format(bill))
            
                print('')
            
                total_bill = total_bill + bill  
                
                total_electric = total_electric + electric
                
            
        MWh = total_electric / 1000 
    
        mwh_retinue = total_bill / MWh
    
        customer_retinue = total_bill / num_customers
            
        print('')
        print('')
        print("Batch Billing Summary -----------")
        print('Total of bills: ${:.2f}'.format(total_bill))
        print('Total MWh used: {:.2f}'.format(MWh))
        print('Revenue/MWh: ${:.2f}'.format(mwh_retinue))
        print('Revenue/customer: ${:.2f}'.format(customer_retinue))
            
    else:
            
        print('')
        print('')
        print("Batch Billing Summary -----------")
        print('Total of bills: $0')
        print('Total MWh used: 0')
        print('Revenue/MWh: $0')
        print('Revenue/customer: $0')
main()