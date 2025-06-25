# Todd McKenzie, CS 115 Section 002, tmckenzie0034@uky.edu
# Purpose: This program takes patient numbers and their temperature readings, 
# calculates the average temperature, diagnoses the temperature condition 
# and displays the results.
# Pre-conditions: The user must input patient numbers and their temperature readings.
# Post-conditions: The program will display the patient data, diagnoses and overall statistics.

def main():
    
    # Print introduction message
    print('Enter patient number and three temperature readings')
    print('Enter blank line to stop entering data')
    
    # Prompt user to enter patient data and initialize variables
    patient_info = input('Enter Patient:')
    patient_data = []
    diagnosis = 0
    no_diagnosis = 0 
    fever = 0
    low_temp = 0
    num_patient = 0
    
    # Loop to collect patient data until user enters blank line
    while patient_info != "":
        
        # Split patient data into patient number and three temperature readings
        patient_info = patient_info.replace(',', ' ')
        patient, temp1, temp2, temp3 = patient_info.split()
        
        # Convert temperature readings to float
        temp1 = float(temp1)
        temp2 = float(temp2)
        temp3 = float(temp3)
        
        # Calculate the average temperature
        avg_temp = (temp1 + temp2 + temp3) / 3
        
        # Increment number of patients processed and store patient data
        num_patient += 1 
        patient_data.append([patient, avg_temp])
        
        # Prompt user to enter next patient data
        patient_info = input('Enter Patient:')
        
    # Display the patient data, diagnoses and overall statistics
    print('')
    print('PT      AVG      Diagnosis')
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
            
        # Print patient data and diagnosis
        print('{:<6} {:<8.2f}  {}'.format(PT, avg_temp, diagnosis))
    
    # Calculate and display overall statistics
    if num_patient == 0:
        print('There were 0 patients processed')
    else:
        fever_percent = fever / num_patient
        low_temp_percent = low_temp / num_patient
        print('There were {:d} patients processed'.format(num_patient))
        print('')
        print('{:d} had a fever ({:.1f}%)'.format(fever, fever_percent*100))
        print('{:d} had a low temperature ({:.1f}%)'.format(low_temp, low_temp_percent*100))
    
main()

# Test Cases 

# Test Case 1
# Enter Patient: 00001, 100, 100, 100
# Enter Patient:00002, 98, 98, 98
#
# PT      AVG      Diagnosis
# 00001  100.00    fever
# 00002  98.00     
# There were 2 patients processed

# 1 had a fever (50.0%)
# 0 had a low temperature (0.0%)


# Test Case 2
# Enter Patient:00001, 98, 98, 98
#
# PT      AVG      Diagnosis
# 00001  98.00     
# There were 1 patients processed

# 0 had a fever (0.0%)
# 0 had a low temperature (0.0%)

