# Todd McKenzie, CS 115 Section 002, tmckenzie0034@uky.edu

def main():
    
    total_score = 0
    student_number = 1
    num_students = 0
    student_list = []
    
    print("Enter student name and four scores:")
    print("Press Enter to stop")
    
    student_info = input("Student {:.0f}:".format(student_number))
    
    if student_info == "":
        
        print("")
        print('No Students Processed ')
        
    else:
    
        while student_info != "":
            
            student_data = student_info.split(",")
            name = student_data[0].strip()
            scores = [int(x.strip()) for x in student_data[1:]]
            student_list.append((name, scores))
            student_number += 1
            num_students += 1
            total_score += sum(scores)
            student_info = input("Student {:.0f}:".format(student_number))
        
        if num_students > 0:
            
            class_avg = total_score / (num_students * 4)
            
        else:
            
            class_avg = 0
            
        print('')
        print("Average grade for class is {:.1f}".format(class_avg))        
            
        print("")
        print("Student    Grade   Passing?")
        
        for i in range(num_students):
            
            name, scores = student_list[i]
            
            avg_grade = sum(scores) / 4
            
            pass_status = "yes" if avg_grade >= 60 else "no"
            
            print(f"{name:7}{avg_grade:7.1f}{pass_status:>8}")

main()