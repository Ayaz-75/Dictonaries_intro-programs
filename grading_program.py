



#program for grading system

student_score={
    "Ayaz":80,
    "Wasi":95,
    "Muzi":85 

}

student_grade={}
for key in student_score:
    score=student_score[key]
    
    if score>91:
        student_grade[key]="Outstanding"
        
    elif student_score[key]>81 and student_score[key]<91:
        student_grade[key]="Exceed Expectations"
        
    elif student_score[key]>71 and student_score[key]<81:
        student_grade[key]="Acceptable"

    elif student_score[key]<70:
        student_grade[key]="Fail"


print(student_grade)