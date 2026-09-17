#Brandon
#AM
#Student Perfomer Analyzer

# Program Introduction

print("=========STUDENT PERFORMANCE ANALYZER========")

#Asks for user Name
name = input("StudentName: ")

##ASks for Grade level
grade_level = input("Grade Level: ")

#Asks for student assignment average
avg_assignemnt = float(input("Assignment Average: "))

## asks for students quiz average
avg_quiz = float(input("Quiz Average: "))

##Asks for student test average
avg_test = float(input("Test Average: "))

## asks for student attendance
student_attendance = float(input("Attendance Percentage: "))

## asks for number of missing assignments
missing_assignments = int(input("Missing Assignments: "))

def calculate_grade(avg_assignment,avg_quiz,avg_test):
    overall_grade = avg_assignment * 0.3 + avg_quiz * 0.3 + avg_test * 0.4
    return overall_grade


def letter_grade(overall_grade):
    if overall_grade >= 90:
        return "Letter Grade: A"
    elif overall_grade >= 80:
        return "Letter Grade: B"
    elif overall_grade >= 70:
        return "Letter Grade: C"
    elif overall_grade >= 60:
        return "Letter Grade: D"
    else:
        return "Letter Grade: F"
    
def attendance_status(student_attendance):
    if student_attendance >= 95:
        return "Attendance Status: Excellent"
    elif student_attendance >= 90:
        return "Attendance Status: Good"
    elif student_attendance >= 80:
        return "Attendance Status: Warning"
    else:
        return "Attendance Status: Poor"
    
def assignment_status(missing_assignments):
    if missing_assignments == 0:
        return "Missing Assignment Status: Perfect"
    elif missing_assignments == (1 or 2):
        return "Missing Assignment Status: Good"
    elif missing_assignments == (3 or 4):
        return "Missing Assignment Status: Warning"
    else:
        return "Missing Assignment Status: Critical"
    
def check_eligibility(overall_grade,student_attendance,missing_assignments):
    if overall_grade >= 70:
        if student_attendance >= 90:
            if missing_assignments > 2:
                return "Academic Eligibility: ELIGIBLE, STUDENT PASSED ALL 3 REQUIREMENTS"
            
            else:
                return "Academic Eligibility: NOT ELIGIBLE, REASON: Too many missing assignments"
                
        else:
            return "Academic Eligibility: NOT ELIGIBLE, REASON: Attendance is too low"
    
    
    else:
        return "Academic Eligibility: NOT ELIGIBLE, REASON: Overall Grade is too Low"
        
            
            
    