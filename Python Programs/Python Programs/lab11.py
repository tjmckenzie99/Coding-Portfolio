# Todd McKenzie, CS 115 Section 002, tmckenzie0034@uky.edu
# Purpose: 
# Pre-conditions: 
# Post-conditions: 

def main():
    
    print('Enter patient number and three temperature readings')
    print('Enter blank line to stop entering data')
    
    patient_info = input('Enter Patient:')
    
    patient_data = []
    
    diagnosis = 0
    
    no_diagnosis = 0 
    
    fever = 0
    
    low_temp = 0
    
    num_patient = 0
    
    while patient_info != "":
        
        patient, temp1, temp2, temp3 = patient_info.split(',') or patient_info.split(' ')
        
        temp1 = float(temp1)
        
        temp2 = float(temp2)
        
        temp3 = float(temp3)
        
        avg_temp = (temp1 * temp2 * temp3) / 3

        num_patient += 1 
        
        patient_data.append([patient, avg_temp])
        
        patient_info = input('Enter Patient:')
        
    print('')
    
    for patient in patient_data:
        
        PT = patient[0]
        
        avg_temp = patient[1]
        
        if avg_temp > 98.7:
            
            diagnosis = 'fever'
            fever += 1
            
        elif avg_temp <= 98.7 and avg_temp >= 95:
            
            diagnosis = ''
            no_diagnosis += 1 
        
        elif avg_temp < 95.0:
            
            diagnosis = 'chilled'
            low_temp += 1
            
    if num_patient == 0:
        print('There were 0 patients processed') 
        
    else:
        fever_percent = fever / num_patient
        low_temp_percent = low_temp / num_patient
        print('There were {:0f} patients processed'.format(num_patient))
        print('')
        print('{:0f} had a fever ({:.1f}%'.format(fever, fever_percent))
        print('{:0f} had a low temperature ({:.1f}%)'.format(low_temp, low_temp_percent))
    
main()