# Todd McKenzie, CS 115 Section 002, tmckenzie0034@uky.edu

def main():
    
    print('CS 115 Weighted Score Calculator')
    print('')
    
    students = 0
    sum_weight_grade = 0
    
    num_students = int(input("How many students?"))
    print('')
    
    for students in range(1,num_students + 1):
    
        print('Processing Student {:.0f} .....'.format(students))
        oth_assign = float(input("Enter score for other assignments: (1-100)"))
        
        if oth_assign > 100:
            oth_assign = 100
            print('Other assignments too high, using 100')
            
        lab_test = float(input("Enter score for Lab Test: (1-100)"))
        
        if lab_test > 100:
            lab_test = 100
            print('Lab tests too high, using 100')
            
        midterm = float(input("Enter score for Midterm: (1-100)"))
        
        if midterm > 100:
            midterm = 100
            print('Midterm too high, using 100')
        
        final = float(input("Enter score for Final: (1-100)"))
        if final > 100:
            final = 100
            print('Final too high, using 100')
        
        oth_assign_grade = oth_assign * .45
        lab_test_grade = lab_test * .20
        midterm_grade = midterm * .15
        final_grade = final * .20
        print('')
        weight_grade = oth_assign_grade + lab_test_grade + midterm_grade + final_grade
        
        if weight_grade > 95:
            per_val = "Excellent"
        elif weight_grade >= 75 and weight_grade <= 95:
            per_val = "Good"
        elif weight_grade >= 55 and weight_grade <= 75:
            per_val = "Pass"
        else:
            per_val = "Poor"
            
        print('Weighted score for student is {:.1f} {}'.format(weight_grade, per_val))
        print('')
        print('')
        sum_weight_grade = (sum_weight_grade + weight_grade)
    
    if num_students > 0:
        average_score = (sum_weight_grade)/(num_students)
        print('Average score for class is {:.1f}'.format(average_score))
    else:
        print("Average score for class is 0.0")
    
main()