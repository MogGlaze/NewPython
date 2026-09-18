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

def check_high_honors(overall_grade,student_attendance,missing_assignments):
    if overall_grade >= 90:
        if student_attendance >= 95:

            if missing_assignments == 0:
                return "YES, HONOR STUDENT"

            else:
                return "SORRY NO, YOUR MISSING ASSIGNMENTS"

        else:
             return "Sorry, Attendance is not eligible"

    else:
            return "Sorry Grade is not eligible for honors"

def check_goodstanding(overall_grade,student_attendance):
     if overall_grade >= 70 and student_attendance >= 90:
          return "Good Standing: YES"
     else:
          return "Good Standing: NO"


def check_support(overall_grade,student_attendance):
     if overall_grade < 70 or student_attendance < 80:
          return "Additional Support: RECOMMENDED"
     else:
          return "Additional Support: NOT RECOMMENDED"

student_user = "student"
student_pin = 1234
User = input("Enter Username: ")
Pin = int(input("Enter Pin: "))

if User == student_user:
     if Pin == student_pin:
          print("Login Successful")
     else:
          print("Login Unsucessful: Incorrect PIN")

else:
     print("Login Unsuccessful: Incorrect User")


def grade_level_message(grade_level):
     if grade_level == 9:
          return "Welcome to your freshman year!"
     elif grade_level == 10:
          return "Keep building your skills!"
     elif grade_level == 11:
          return "Junior Year- Keep Pushing!"
     elif grade_level == 12:
          return "Senior Year- finish strong!"
     else:
          return "Invalid grade level."


def strongest_category(avg_assignment,avg_quiz,avg_test):
     if avg_assignment > (avg_quiz and avg_test):
          return "Strongest Category: Assignments"
     elif avg_test


            
        
            
            
    
