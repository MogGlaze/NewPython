# Name:
# Period:

# ============================================================
# Python Skills Check — Slides 61–116
# CONDITIONALS & FUNCTIONS — CHALLENGE VERSION
# ============================================================

# DIRECTIONS
# ============================================================
# - I recommend you create a repo first and clone it.
# - Drag this file into your repo and push when you are done.
#
# Complete each task underneath its directions.
#
# RULES:
# - Use ONLY concepts we have learned in class.
# - Use the EXACT variable and function names provided.
# - Do not delete the directions.
# - Your entire Python file must run without errors.
# - Do NOT manually type an answer that Python should determine.
# - Pay attention to indentation.
# - Read carefully. MANY questions are intentionally tricky.
# - Unless a task says otherwise, do NOT use min() or max().
# - Your conditions should work even if the variable values are changed.
#
# IMPORTANT:
# Some questions are designed so that the ORDER of your conditions matters.
# Some questions have edge cases such as ties or boundary values.
# Test your logic carefully.


# ============================================================
# SECTION 1 — COMPARISON WARM-UP
# ============================================================

# TASK 1:
# Create:
#
number_one = 25
number_two = 40
#
# Write an if statement that prints:
#
# number_two is greater
#
# ONLY if number_two is greater than number_one.
if number_two > number_one:
    print("number_two is greater")

# TASK 2:
# Create:
#
score = 80
#
# Print:
# Passing score
#
# if score is GREATER THAN OR EQUAL TO 70.
if score >= 70:
    print("Passing score")


# TASK 3:
# Create:
#
lives = 0
#
# Print:
#Game over
#
# ONLY if lives is exactly 0.
if lives == 0:
    print("Game over")

# TASK 4:
# Create:
#
username = "student"
#
# Print:
# Different username
#
# ONLY if username is NOT equal to "admin".
if username != "admin":
    print("Different username")


# ============================================================
# SECTION 2 — BOUNDARIES & ORDER MATTER
# ============================================================

# TASK 5:
# Create:
#
age = 18
#
# Print:
# Child       if age is under 13
# Teen        if age is 13 through 17
# Adult       if age is 18 through 64
# Senior      if age is 65 or older
#
# Use if / elif / else.
#
# THINK:
# Which condition should be checked first?

if age >= 65:
    print("Senior")
elif age >= 18:
    print("Adult")
elif age >= 13:
    print("Teen")
else:
    print("Child")


# TASK 6:
# Create:
#
grade = 90
#
# Print:
# A if grade is 90 or higher
# B if grade is 80–89
# C if grade is 70–79
# D if grade is 60–69
# F if grade is below 60
#
# IMPORTANT:
# grade = 90 should print ONLY:
# A
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")
       


# TASK 7:
# Create:
#
temperature = 70
#
# Print:
# Cold       if below 50
# Mild       if 50 through 69
# Warm       if 70 through 89
# Hot        if 90 or higher
#
# Be careful with 50, 70, and 90.

if temperature >= 90:
    print("HOT")
elif temperature >= 70:
    print("Warm")
elif temperature >= 50:
    print("Mild") 
else:
    print("Cold")


# TASK 8:
# Create:
#
speed = 65
#
# Print:
# Too Slow       if speed is below 25
# Normal         if speed is 25 through 65
# Speeding       if speed is 66 through 80
# Reckless       if speed is above 80
#
# The value 65 must print:
# Normal

if speed > 80:
    print("Reckless")
elif speed >= 66:
    print("Speeding")
elif speed >= 25:
    print("Normal")
else:
    print("Too Slow")
           
    


# TASK 9:
# Create:
#
amount = 100
#
# Print:
# Small purchase       if amount is below 25
# Medium purchase      if amount is 25 through 99
# Large purchase       if amount is 100 through 499
# Huge purchase        if amount is 500 or more
#
# THINK carefully about your comparison operators.

if amount >= 500:
    print("Huge purchase")
elif amount >= 100:
    print("Large purchase")
elif amount >= 25:
    print("Medium purchase")
else:
    print("Small purchase")            


# ============================================================
# SECTION 3 — AND / OR THINKING
# ============================================================

# TASK 10:
# Create:
#
age = 16
has_ticket = True
#
# Print:
# You may enter
#
# ONLY if age is at least 13 AND has_ticket is True.
#
# Otherwise print:
# Entry denied
if (age >= 16 and has_ticket ):
    print("You may enter")
else:
    print("Entry denied")    


# TASK 11:
# Create:
#
temperature = 91
#
# Print:
# Extreme temperature
#
# if temperature is below 32 OR above 90.
#
# Otherwise print:
# Normal temperature

if temperature > 90 or temperature < 32:
    print("Extreme temperature")
else:
    print("Normal temperature")


# TASK 12:
# Create:
#
username = "admin"
password = "python123"
#
# Print:
# Access granted
#
# ONLY if BOTH values are correct.
#
# Otherwise print:
# Access denied
if username == "admin" and password == "python123":
    print("Access granted")
else:
    print("Access denied")


# TASK 13:
# Create:
#
age = 70
has_membership = False
#
# Print:
# Discount applies
#
# if the person is 65 or older OR has_membership is True.
#
# Otherwise print:
# No discount
if age >= 65 or has_membership:
    print("Discount applies")
else:
    print("No discount")


# TASK 14:
# Create:
#
number = 25
#
# Print:
# In range
#
# if number is from 10 through 30 INCLUDING 10 and 30.
#
# Otherwise print:
# Out of range

if number >= 10 and number <= 30:
    print("In range")
else:
    print("Out of range")   


# TASK 15:
# Create:
#
number = 10
#
# Print:
# Outside middle range
#
# if number is LESS THAN 20 OR GREATER THAN 80.
#
# Otherwise print:
# Inside middle range
#
# Test mentally with:
# 10
# 50
# 90

if number < 20 or number > 80:
    print("Outside middle range")
else:
    print("Inside middle range")


# ============================================================
# SECTION 4 — HIGHEST / LOWEST / MIDDLE
# ============================================================

# TASK 16:
# Create:
#
a = 12
b = 7
c = 19
#
# WITHOUT using max(), determine which variable contains
# the HIGHEST value.
#
# Print:
# a is highest
# OR
# b is highest
# OR
# c is highest

if a > (c and b):
    print("a is the highest")
elif b > (c and a):
    print("b is the highest")
else:
    print("C is the highest")

# TASK 17:
# Create:
#
x = 44
y = 13
z = 28
#
# WITHOUT using min(), determine which variable contains
# the LOWEST value.
#
# Print the correct variable name followed by:
# is lowest
if x < (y and z):
    print(f"x is lowest")
elif y < (x and z):
    print("y is the lowest")
else:
    print("z is lowest")


# TASK 18:
# Create:
#
num1 = 10
num2 = 30
num3 = 20
#
# WITHOUT using min(), max(), or sorting,
# determine the MIDDLE value.
#
# Print:
# Middle: [value]
#
# HINT:
# The middle value is not the highest and not the lowest.

if num1 > num2 and num1 < num3:
    print(f"Middle:{num1}")
elif num2 > num1 and num2 < num3:
    print(f"Middle: {num2}")
else:
    print(f"Middle:{num3}")


# TASK 19:
# Create:
#
first = 20
second = 20
third = 8
#
# Determine what is highest.
#
# Your program must correctly handle the tie.
#
# Possible outputs:
# first is highest
# second is highest
# third is highest
# first and second are tied for highest
# first and third are tied for highest
# second and third are tied for highest
# all three are tied

if first > (third and second):
    print("first is highest")
elif second > (third and first):
    print("second is highest")
elif third > (second and first):
    print("third is highest")
elif first == second:
    print("first and second are tied")
elif first == third:
    print("first and third are tied")
elif second == third:
    print("Second and third are tied")
else:
    print("all three are tied")


# TASK 20:
# Create:
#
first = 5
second = 5
third = 5
#
# Determine whether:
#
# - all three are equal
# - exactly two are equal
# - none are equal
#
# Print ONE of:
#
# All equal
# Exactly two equal
# All different
#
# Your code should still work if the values are changed.

if first == third and first == second and third == second:
    print("all three are equal")
elif first == third or second == third or second == first:
    print("exactly two are equal")
else:
    print("All different")
    


# TASK 21:
# Create:
#
# a = 9
# b = 4
# c = 9
#
# Determine whether AT LEAST TWO numbers match.
#
# Print:
# A match exists
#
# Otherwise print:
# No match

if a == b:
    print("A and B match exist")
elif a == c:
    print("a and c match exist")
elif b == c:
    print("b and c match exist")
else:
    print("no match")


# TASK 22:
# Create:
#
a = 14
b = 7
c = 20
#
# Determine whether a is BETWEEN b and c.
#
# Print:
# a is between b and c
#
# if that is true.
#
# Otherwise print:
# a is not between b and c
#
# IMPORTANT:
# Your code should still work if b is greater than c.

if a < c and a > b:
    print("a is between b and c")

elif a < b and a > c:
    print("a is between b and c")
    
else:
    print("a is not between b and c")


# TASK 23:
# Create:
#
a = 50
b = 20
c = 80
#
# Determine whether b is the lowest AND c is the highest.
#
# If BOTH are true, print:
# Correct order
#
# Otherwise print:
# Different order

if b < (c and a) and c > (a and b):
    print("Correct order")
else:
    print("Different order")


# ============================================================
# SECTION 5 — USER INPUT LOGIC
# ============================================================

# TASK 24:
# Ask the user for THREE whole numbers.
#
# Store them in:
#
first_number = int(input("Number: "))
second_number = int(input("Number2: "))
third_number = int(input("Number3: "))
#
# WITHOUT using min() or max(), print the LOWEST number.

if third_number < (first_number and second_number):
    print(f"{third_number}")
elif second_number < (first_number and third_number):
    print(f"{second_number}")
else:
    print(f"{first_number}")


# TASK 25:
# Ask the user for THREE whole numbers.
#
# Store them in:
#
value1 = int(input("Value: "))
value2 = int(input("Value2: "))
value3 = int(input("Value3: "))
#
# WITHOUT using min() or max(), print the HIGHEST number.
if value1 < (value2 and value3):
    print(f"{value1}")
elif value2 <(value1 and value3):
    print(value2)
else:
    print(value3)

# TASK 26:
# Ask the user for THREE whole numbers.
#
# Store them in:
#
n1 = int(input("n1: "))
n2 = int(input("n2: "))
n3 = int(input("n3: "))
#
# Determine whether the user entered them in STRICTLY increasing order.
#
# Example:
# 3, 8, 10 -> Increasing
#
# 3, 3, 10 -> NOT Increasing
#
# Print:
# Increasing
# OR
# Not increasing
if n1 < (n2 and n3):
    if n2 < n3:
        print("Increasing")
else:
    print("Not Increasing")


# TASK 27:
# Ask the user for THREE whole numbers.
#
# Store them in:
#
n1 = int(input("n1: "))
n2 = int(input("n2: "))
n3 = int(input("n3: "))
#
# Determine whether the numbers are in STRICTLY decreasing order.
#
# Print:
# Decreasing
# OR
# Not decreasing
if n1 >(n2 and n3):
    if n2 > n3:
        print("Decreasing")
else:
    print("Not decreasing")

# TASK 28:
# Ask the user for THREE whole numbers.
#
# Store them in:
#
a = int(input("First: "))
b = int(input("Second: "))
c = int(input("Third: "))
#
# Print:
# All same
# if all three match
#
# Two same
# if exactly two match
#
# All different
# if none match

if a == b and b == c and a == c:
    print("all three match")
elif a == b or b ==c or a == c:
    print("exactly two match")
else:
    print("None match")


# TASK 29:
# Ask the user for a score from 0 to 100.
#
# Store it in:
#
user_score = int(input("Score: "))

if score > 100 or score < 0:
    print("Invalid score")
elif score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("FAILURE F")
#
# FIRST determine if the score is valid.
#
# If it is below 0 OR above 100, print:
# Invalid score
#
# Otherwise print the letter grade:
# A, B, C, D, or F
#
# THINK:
# You should not assign a letter grade to an invalid score.



# ============================================================
# SECTION 6 — FUNCTIONS BASICS
# ============================================================

# TASK 30:
# Create a function named:
#
def say_hello():
    print("Hello")
#
# It should print:
# Hello!
#
# Call it once.
say_hello()



# TASK 31:
# Create a function named:
#
def greet_student(name):
    print("Hello " + name)
#
# Give it ONE parameter:
#
# name
#
# Print:
# Hello [name]
#
# Call it THREE times using different names.
greet_student("Brandon")
greet_student("Gurt")
greet_student("Roselyn")



# TASK 32:
# Create a function named:
#
def add_three(a,b,c):
    sum = a + b + c
    print(sum)
#
# Give it THREE parameters:
#
# a
# b
# c
#
# Print the sum of all three.
#
# Call it at least TWO times.
add_three(4,7,2)
add_three(5,8,1)


# ============================================================
# SECTION 7 — FUNCTIONS + CONDITIONALS
# ============================================================

# TASK 33:
# Create a function named:
#
def check_number(number):
    if number < 0:
        print("Negative")
    elif number > 0:
        print("Positive")
    else:
        print("Zero")
        
check_number(10)
check_number(-5)
check_number(0)
#
# Give it ONE parameter:
#
# number
#
# Print:
# Positive
# Negative
# or
# Zero
#
# Call it using:
# 10
# -5
# 0


# TASK 34:
# Create a function named:
#
def check_even_odd(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")
check_even_odd(5)
check_even_odd(2)
check_even_odd(1)
check_even_odd(9)
#
# Give it ONE parameter:
#
# number
#
# Print:
# Even
# OR
# Odd
#
# Test it at least FOUR times.


# TASK 35:
# Create a function named:
#
def ticket_type(age):
    if age >= 65:
        print("Senior")
    elif age >= 18:
        print("Adult")
    elif age >= 13:
        print("Teen")
    else:
        print("Child")

ticket_type(12)
ticket_type(13)
ticket_type(17)
ticket_type(18)
ticket_type(64)
ticket_type(65)

# Give it ONE parameter:
#
# age
#
# Print:
# Child
# Teen
# Adult
# Senior
#
# using these ranges:
#
# Child: under 13
# Teen: 13–17
# Adult: 18–64
# Senior: 65+
#
# Test boundary values:
# 12
# 13
# 17
# 18
# 64
# 65


# TASK 36:
# Create a function named:
#
def find_highest(a,b,c):
    if a > (b and c):
        return a
    elif b >(a and c):
        return b
    else:
        return c

    
#
# Give it THREE parameters:
#
# a
# b
# c
#
# WITHOUT using max(), print the highest value.
#
# Test:
print(find_highest(5, 20, 11))
print(find_highest(100, 25, 60))
print(find_highest(8, 9, 30))


# TASK 37:
# Create a function named:
#
def find_lowest(a,b,c):
    if a < (b and c):
        return a
    elif b < (a and c):
        return b
    else:
        return c
print(find_lowest(1,2,3))
print(find_lowest(1,6,32))
print(find_lowest(9,2,43))

#
# Give it THREE parameters:
#
# a
# b
# c
#
# WITHOUT using min(), print the lowest value.
#
# Test at least THREE times.


# TASK 38:
# Create a function named:
#
def find_middle(a,b,c):
    if a > b and a < c:
        if a > c and a < b:
            return a
    elif b > a and b < c:
        if b < a and b > c:
            return b
    else:
        return c
    
    
#
# Give it THREE parameters:
#
# a
# b
# c
#
# WITHOUT using min(), max(), or sorting,
# print the MIDDLE value.
#
# Test:
print(find_middle(10, 30, 20))
print(find_middle(100, 5, 50))
print(find_middle(7, 9, 8))


# TASK 39:
# Create a function named:
#
def compare_three(a,b,c):
    if a ==b and b == c and a == c:
        print("All equal")
    elif a == b or b == c or a == c:
        print("Exactly two are equal")
    else:
        print("All different")
        
compare_three(3,3,3)
compare_three(5,5,7)
compare_three(2,7,5)
#
# Give it THREE parameters:
#
# a
# b
# c
#
# Print ONE of:
#
# All equal
# Exactly two equal
# All different
#
# Test all three situations.


# TASK 40:
# Create a function named:
#
def is_in_range(number,low,high):
    if (number >= low and number <= high):
        print("In range")
    else:
        print("Out of range")
#
# Give it THREE parameters:
#
# number
# low
# high
#
# Print:
# In range
#
# if number is between low and high INCLUDING the endpoints.
#
# Otherwise print:
# Out of range
#
# IMPORTANT:
# Your function should still work if low and high
# are accidentally passed in backwards.
#
# Example:
# is_in_range(50, 100, 1)
#
# should still print:
# In range


# ============================================================
# SECTION 8 — RETURN VALUES
# ============================================================

# TASK 41:
# Create a function named:
#
def multiply_numbers(num1,num2):
    total = num1 * num2
    return total
multiplication_result = multiply_numbers(6,7)
print(multiplication_result)
#
# Give it TWO parameters:
#
# num1
# num2
#
# RETURN their product.
#
# Store the result of:
# multiply_numbers(6, 7)
#
# inside:
# multiplication_result
#
# Print multiplication_result.


# TASK 42:
# Create a function named:
#
def larger_number(a,b):
    if a > b:
        return a
    elif a == b:
        return a
    else:
        return b

bigger = larger_number(15,40)
print(bigger)
#
# Give it TWO parameters:
#
# a
# b
#
# RETURN the larger value.
#
# If they are equal, RETURN that value.
#
# Store the result of:
# larger_number(15, 40)
#
# inside:
# bigger
#
# Print bigger.


# TASK 43:
# Create a function named:
#
def highest_of_three(a,b,c):
    if a > (b and c):
        return a
    elif b > (a and c):
        return b
    else:
        return c

#
# Give it THREE parameters:
#
# a
# b
# c
#
# WITHOUT using max(), RETURN the highest value.
#
# Store:
# highest_of_three(18, 42, 27)
#
# inside:
highest_result = highest_of_three(18,42,27)
print(highest_result)
# Print highest_result.


# TASK 44:
# Create a function named:
#
def lowest_of_three(a,b,c):
    if a < (b and c):
        return a
    elif b < (a and c):
        return b
    else:
        return c
print(lowest_of_three(5,9,2))
print(lowest_of_three(4,8,1))
print(lowest_of_three(4,49,8))
#
# Give it THREE parameters:
#
# a
# b
# c
#
# WITHOUT using min(), RETURN the lowest value.
#
# Test it at least THREE times.


# TASK 45:
# Create a function named:
#
def middle_of_three(a,b,c):
    if (a > b and a < c) or (a > c and a < b):
        return a
    elif (b > a and b < c) or (b < a and b > c):
        return b
    else:
        return c

# Give it THREE parameters:
#
# a
# b
# c
#
# RETURN the middle value.
#
# Do NOT use min(), max(), or sorting.
#
# Test:
print(middle_of_three(10, 30, 20))
print(middle_of_three(50, 5, 25))
print(middle_of_three(8, 7, 9))


# ============================================================
# SECTION 9 — RETURN + REUSE
# ============================================================

# TASK 46:
# Create a function named:
#
def get_highest(a,b,c):
    if a > (b and c):
        return a
    elif b > (a and c):
        return b
    else:
        return c
    
#
# Give it THREE parameters and RETURN the highest number.
#
# Then create another function named:
#
def get_lowest(a,b,c):
    if a < (b and c):
        return a
    elif b < (a and c):
        return b
    else:
        return c
    
#
# Give it THREE parameters and RETURN the lowest number.
#
# Use:
#
# a = 30
# b = 10
# c = 20
#
# Store the returned values in:
#
highest = get_highest(30,10,20)
lowest = get_lowest(30,10,20)
#
# Then calculate:
#
# difference
#
# by subtracting lowest from highest.
difference = highest = lowest
print(difference)
# Print difference.
#
# IMPORTANT:
# Do NOT repeat the highest/lowest logic outside the functions.


# TASK 47:
# Create:
high = get_highest(9,4,15)
low = get_lowest(9,4,15)

if (high - low) > 10:
    print("Large spread")
else:
    print("Small spread")
# a = 9
# b = 4
# c = 15
#
# Use your get_highest() and get_lowest() functions from above.
#
# Store both returned values.
#
# Then determine if the difference between highest and lowest
# is greater than 10.
#
# Print:
# Large spread
#
# or:
# Small spread


# TASK 48:
# Create a function named:
#
def best_of_two(a,b):
    if a > b:
        return a
    else:
        return b
#
# Give it TWO parameters and RETURN the larger value.
#
# Then use it to determine the highest of THREE numbers
# WITHOUT writing a new three-number comparison.
#
# You should call best_of_two() more than once.
highest = best_of_two(12,50)
highest = best_of_two(50,31)

print(highest)
# Use:
# a = 12
# b = 50
# c = 31
#
# Store the final answer in:
#
# highest
#
# Print highest.
#
# THINK:
# How can one function call feed into another?


# TASK 49:
# Create a function named:
#
def worst_of_two(a,b):
    if a > b:
        return b
    else:
        return a


lowest = worst_of_two(22,5)
lowest = worst_of_two(5,17)
print(lowest)
#
# Give it TWO parameters and RETURN the smaller value.
#
# Use it more than once to find the LOWEST of:
#
# a = 22
# b = 5
# c = 17
#
# Store the final result in:
#
# lowest
#
# Print lowest.


# ============================================================
# SECTION 10 — LOGIC CHALLENGES
# ============================================================

# TASK 50:
# Create:


a = 12
b = 7
c = 19

if (b > a and b < c) or (b > c and b < a):
    print("b is the middle")
else:
    print("B is not the middle")
#
# Determine whether b is the MIDDLE value.
#
# Print:
# b is middle
#
# or:
# b is not middle
#
# Do NOT calculate the middle value separately first.


# TASK 51:
# Create:
#
a = 25
b = 25
c = 10

if a 
else:
    print("Highest is unique")
# Determine whether the HIGHEST value appears more than once.
#
# Print:
# Highest is tied
#
# or:
# Highest is unique


# TASK 52:
# Create:
#
a = 3
b = 8
c = 5
#
# Determine whether the numbers are:
#
# Strictly increasing
# Strictly decreasing
# Neither
#
# Print ONE result.

if a > b > c:
    print("Decreasing")
elif a < b < c:
    print("Increasing")
else:
    print("Neither")

# TASK 53:
# Create:
#
# a = 5
# b = 5
# c = 10
#
# Determine whether the values are in NON-DECREASING order.
#
# This means each value may stay the same or get larger.
#
# Examples:
# 3, 3, 7 -> yes
# 3, 7, 7 -> yes
# 3, 7, 2 -> no
#
# Print:
# Non-decreasing
# OR
# Not non-decreasing
if a <= b <= b <= c:
    print("Non-Decreasing")
else:
    print("Not Non-Decreasing")


# TASK 54:
# Create:
#
age = 17
has_permission = True
has_ticket = False
#
# A person may enter if:
#
# - they are 18 or older
#
# OR
#
# - they are under 18 AND have_permission is True AND have_ticket is True
#
# Print:
# Entry allowed
#
# or:
# Entry denied
#
# Read this one carefully.
if age >= 18 or (age <= 18 and has_permission and has_ticket):
    print("Entry allowed")
else:
    print("Entry denied")


# TASK 55:
# Create:
#
score = 88
attendance = 92
#

if score >= 90 and attendance >= 90:
    print("HONORS")
elif score >= 70 and attendance >= 75:
    print("Pass")
else:
    print("Fail") 
# Print:
# Honors
#
# if score is at least 90 AND attendance is at least 90.
#
# Print:
# Pass
#
# if score is at least 70 AND attendance is at least 75,
# but the student did not qualify for Honors.
#
# Otherwise print:
# Fail
#
# Only ONE message should print.


# ============================================================
# SECTION 11 — DEBUGGING CHALLENGES
# ============================================================

# TASK 56:
# The programmer wants exactly ONE result.
#
# Fix the code so score = 95 prints ONLY:
#
# Excellent
#
score = 95
#
if score >= 95:
    print("Excellent")
elif score >= 70:
    print("passing")
else:
    print("fail")


# TASK 57:
# The programmer wants 18 to count as Adult.
#
# Fix the logic.
#
age = 18

if age >= 18:
    print("Adult")
else:
    print("Minor")


# TASK 58:
# The programmer wants numbers from 10 through 20,
# INCLUDING 10 and 20, to print:
#
# Valid
#
# Fix the condition.
#
number = 20

if number >= 10 and number <= 20:
    print("Valid")
else:
    print("Invalid")


# TASK 59:
# The programmer wants the function to RETURN the answer.
#
# Fix it.
#
def add_numbers(a, b):
    total = a + b
    return total

result = add_numbers(4, 6)
print(result)


# TASK 60:
# Fix the function so the variable result works outside
# of the function.
#
def subtract(a, b):
    result = a - b
    return result

result = subtract(20, 8)
print(result)


# ============================================================
# FINAL BOSS 1 — THREE NUMBER ANALYZER
# ============================================================

# TASK 61:
# Create a function named:
#

        
        
#
# Give it THREE parameters:
#
# a
# b
# c
#
# It must:
#
# 1. Determine the highest value.
# 2. Determine the lowest value.
# 3. Determine the middle value.
# 4. Determine whether all three are equal.
# 5. Determine whether exactly two are equal.
#
# Print:
#
# Highest: [value]
# Lowest: [value]
# Middle: [value]
#
# Then print ONE of:
#
# All equal
# Exactly two equal
# All different
#
# RESTRICTIONS:
# - Do NOT use min()
# - Do NOT use max()
# - Do NOT use sorting
#
# Test:
# analyze_three_numbers(8, 3, 15)
# analyze_three_numbers(20, 20, 20)
# analyze_three_numbers(5, 5, 9)
# analyze_three_numbers(-5, 0, -12)


# ============================================================
# FINAL BOSS 2 — NUMBER RANKING
# ============================================================

# TASK 62:
# Ask the user for THREE whole numbers.
#
# Store them in:

num1 = int(input("Number1: "))
num2 = int(input("Number2: "))
num3 = int(input("Number3: "))
#
# Print the numbers from LOWEST to HIGHEST.

if num1 > (num2 and num3):
    print(num1)
    if num2 >= num3:
        print(num2)
        print(num3)
    else:
        print(num3)
        print(num2)
elif num2 >(num3 and num1):
    print(num2)
    if num3 >= num1:
        print(num3)
        print(num1)
    else:
        print(num1)
        print(num3)
else:
    print(num3)
    if num2 >= num1:
        print(num2)
        print(num1)
    else:
        print(num1)
        print(num2)
# Example:
# User enters:
# 30
# 10
# 20
#
# Output:
# 10
# 20
# 30
#
# RESTRICTIONS:
# - Do NOT use min()
# - Do NOT use max()
# - Do NOT use sorting
#
# Your program must still work if the order of inputs changes.


# ============================================================
# FINAL BOSS 3 — FUNCTION REUSE
# ============================================================

# TASK 63:
# Create these THREE functions:
#
def get_highest(a, b, c):
    if a >(b and c):
        return a
    elif b > (a and c):
        return b
    else:
        return c
def get_lowest(a, b, c):
    if a < (b and c):
        return a
    elif b < (a and c):
        return b
    else:
        return c
def get_middle(a, b, c):
    if (a > b and a < c) or (a < b and a > c):
        return a
    elif(b > a and b < c) or (b < a and b > c):
        return b
    else:
        return c
#
# Each function must RETURN the correct value.
#
# Ask the user for THREE whole numbers.
#
# Store them in:


first = int(input("Num1: "))
second = int(input("Num2: "))
third = int(input("Num3: "))
#
# Call all three functions.
#
# Store the returned results in:
#
highest = get_highest(first,second,third)
lowest = get_lowest(first,second,third)
middle = get_middle(first,second,third)
#
# Then print:
#
print(f"Highest: {highest}")
print(f"Middle: {middle}")
print(f"Lowest: {lowest}")
#
# Do NOT use min(), max(), or sorting.


# ============================================================
# FINAL BOSS 4 — CONDITIONAL DECISION SYSTEM
# ============================================================

# TASK 64:
# Create a function named:
#
def admission_decision(grade,attendance,interview):
    if grade >= 90 and attendance >= 90:
        print("accepted")
    elif grade >= 80 and attendance >= 80 and interview =="pass":
        print("Accepted")
    else:
        print("Not accepted")
#
# Give it THREE parameters:
#
# grade
# attendance
# interview
#
# Rules:
#
# - If grade is 90 or higher AND attendance is 90 or higher,
#   print "Accepted"
#
# - Otherwise, if grade is 80 or higher AND attendance is 80 or higher
#   AND interview is "pass", print "Accepted"
#
# - Otherwise print "Not accepted"
#
# Test:
#
admission_decision(95, 95, "fail")
admission_decision(85, 85, "pass")
admission_decision(85, 85, "fail")
admission_decision(75, 100, "pass")
#
# THINK:
# The first person should still be accepted even though
# the interview value is "fail".


# ============================================================
# FINAL BOSS 5 — THINK CAREFULLY
# ============================================================

# TASK 65:
# Create:
#
a = 15
b = 8
c = 15
#
# Your program must determine BOTH:
#
# 1. The highest value
# 2. Whether that highest value is unique or tied


if a >= (b and c):
    if a >( b and c):
        print(f"Highest: {a}")
        print("Unique highest")
    else:
        print(f"Highest:{a}")
        print("Tied highest")
elif b>= (a and c):
    if b >(a and c):
        print(f"Highest:{b}")
        print(f"unique Highest")
    else:
        print(f"Highest:{b}")
        print("Tied Highest")
else:
    if c > (a and b):
        print(f"Highest:{c}")
        print("Unique Highest")
    else:
        print(f"Highest:{c}")
        print("Tied Highest")
#
# Highest: [value]
#
# Then print ONE of:
#
# Unique highest
# Tied highest
#
# RESTRICTIONS:
# - Do NOT use min()
# - Do NOT use max()
# - Do NOT use sorting
#
# Your logic should still work if the variable values change.




# ============================================================
# SECTION 12 — LEETCODE-STYLE REAL PROBLEM CHALLENGES
# ============================================================
#
# These problems are intentionally DIFFERENT from the earlier tasks.
# Instead of simply asking you to find the highest number, check a range,
# or assign a grade, each problem gives you a small situation to solve.
#
# RULES:
# - Use the EXACT function name and parameters given.
# - Do NOT use input() unless the problem specifically tells you to.
# - RETURN the answer unless the problem specifically tells you to print.
# - Your function must work for ALL valid test cases.
# - Do NOT hard-code the example answers.
# - Use only concepts covered in class.
# - Test every example after writing your function.


# ------------------------------------------------------------
# LEETCODE-STYLE TASK 66 — TEMPERATURE CONVERTER
# ------------------------------------------------------------
#
# Write a function named:
#
def convert_temperature(temperature,scale):
    
    if scale == "F":
        Celsius = (temperature-32) / 1.8
        return Celsius
    elif scale == "C":
        Fahrenheit = (temperature * 1.8 + 32)
        return Fahrenheit
    else:
        return "Nada"
        
#
# Parameters:
#
# temperature
# scale
#
# The scale will be either:
#
# "C"
# or
# "F"
#
# If scale is "C", the temperature given is Celsius.
# Convert it to Fahrenheit using:
#
# Fahrenheit = Celsius * 1.8 + 32
#
# If scale is "F", the temperature given is Fahrenheit.
# Convert it to Celsius using:
#
# Celsius = (Fahrenheit - 32) / 1.8
#
# RETURN the converted temperature.
#
# Examples:
#
# convert_temperature(0, "C")      -> 32
# convert_temperature(100, "C")    -> 212
# convert_temperature(32, "F")     -> 0
# convert_temperature(68, "F")     -> 20
#
# CHALLENGE:
# The same function must be able to convert in BOTH directions.


# ------------------------------------------------------------
# LEETCODE-STYLE TASK 67 — KELVIN CONVERTER
# ------------------------------------------------------------
#
# Write a function named:
#
def to_kelvin(temperature,scale):
    if scale == "C":
        Kelvin = temperature + 273.15
        return Kelvin
    elif scale == "F":
        Celsius = (temperature - 32) / 1.8
        Kelvin = Celsius + 273.15
        return Kelvin
    else:
        return "Nada"
#
# Parameters:
#
# temperature
# scale
#
# If scale is "C":
#
# Kelvin = Celsius + 273.15
#
# If scale is "F":
#
# First convert Fahrenheit to Celsius:
#
# Celsius = (Fahrenheit - 32) / 1.8
#
# Then convert Celsius to Kelvin.
#
# RETURN the Kelvin temperature.
#
# Examples:
#
# to_kelvin(0, "C")     -> 273.15
# to_kelvin(100, "C")   -> 373.15
# to_kelvin(32, "F")    -> 273.15
# to_kelvin(212, "F")   -> 373.15
#
# THINK:
# One input can require TWO calculations before you return the answer.


# ------------------------------------------------------------
# LEETCODE-STYLE TASK 68 — PARKING GARAGE
# ------------------------------------------------------------
#
# Write a function named:
#
def parking_cost(hours):
    
    if hours <= 8:
        total = 5 + 3 * (hours - 1)
        return total
    else:
        total = 25
        return total
#
# Parameter:
#
# hours
#
# Parking costs:
#
# First hour: $5
# Each additional hour: $3
#
# If the car is parked for more than 8 hours,
# the maximum daily charge is $25.
#
# RETURN the total parking cost.
#
# Examples:
#
# parking_cost(1)   -> 5
# parking_cost(2)   -> 8
# parking_cost(5)   -> 17
# parking_cost(9)   -> 25
# parking_cost(20)  -> 25
#
# THINK:
# Do not accidentally charge $3 for the first hour.


# ------------------------------------------------------------
# LEETCODE-STYLE TASK 69 — MOVIE TICKET TOTAL
# ------------------------------------------------------------
#
# Write a function named:
#
def movie_total(age,is_weekend):
    if age >= 65:
        if is_weekend:
            return(7 + 3)
        else:
            return 7
    elif age <= 64 and age >= 13:
        if is_weekend:
            return (12 + 3)
        else:
            return 12
    else:
        if is_weekend:
            return (8+3)
        else:
            return 8
#
# Parameters:
#
# age
# is_weekend
#
# Ticket prices:
#
# Under 13: $8
# Ages 13–64: $12
# Age 65+: $7
#
# On weekends, add $3 to the ticket price.
#
# RETURN the final ticket price.
#
# Examples:
#
# movie_total(10, False)  -> 8
# movie_total(10, True)   -> 11
# movie_total(30, False)  -> 12
# movie_total(70, True)   -> 10
#
# THINK:
# First determine the base ticket price.
# Then decide whether something must be added.


# ------------------------------------------------------------
# LEETCODE-STYLE TASK 70 — ELECTRIC BILL
# ------------------------------------------------------------
#
# Write a function named:
#
def electric_bill(usage):
    if usage <= 100:
        total = usage * 0.1
        return total
    else:
        total = usage * 0.20 + 10
        
#
# Parameter:
#
# usage
#
# The bill is calculated using these rules:
#
# 0–100 units:
# $0.10 per unit
#
# More than 100 units:
# The first 100 units cost $0.10 each.
# Every unit AFTER 100 costs $0.20 each.
#
# RETURN the total bill.
#
# Examples:
#
# electric_bill(50)   -> 5.0
# electric_bill(100)  -> 10.0
# electric_bill(120)  -> 14.0
# electric_bill(200)  -> 30.0
#
# IMPORTANT:
# For 120 units, only 20 units should be charged at $0.20.


# ------------------------------------------------------------
# LEETCODE-STYLE TASK 71 — LEAP YEAR
# ------------------------------------------------------------
#
# Write a function named:
#
def is_leap_year(year):
    if year % 400 == 0 or (year % 4 ==0 and not year % 100 ==0):
        return True
    else:
        return False
#
# Parameter:
#
# year
#
# A year is a leap year if:
#
# - it is divisible by 400
#
# OR
#
# - it is divisible by 4 BUT NOT divisible by 100
#
# RETURN True if it is a leap year.
# Otherwise RETURN False.
#
# Examples:
#
# is_leap_year(2024)  -> True
# is_leap_year(2025)  -> False
# is_leap_year(1900)  -> False
# is_leap_year(2000)  -> True
#
# This problem is intentionally tricky.
#
# THINK:
# A year divisible by 100 is NOT automatically a leap year.


# ------------------------------------------------------------
# LEETCODE-STYLE TASK 72 — TRIANGLE VALIDITY
# ------------------------------------------------------------
#
# Write a function named:
#
def valid_triangle(a,b,c):
    if (a + b > c) or (a + c > b) or (b + c > a):
        return True
    else:
        return False
#
# Parameters:
#
# a
# b
# c
#
# Three side lengths can form a triangle only if:
#
# a + b > c
# a + c > b
# b + c > a
#
# ALL THREE conditions must be true.
#
# RETURN True if the sides can form a triangle.
# Otherwise RETURN False.
#
# Examples:
#
# valid_triangle(3, 4, 5)   -> True
# valid_triangle(5, 5, 5)   -> True
# valid_triangle(1, 2, 10)  -> False
# valid_triangle(2, 3, 5)   -> False
#
# Notice that 2 + 3 = 5 is NOT enough.
# It must be GREATER THAN.


# ------------------------------------------------------------
# LEETCODE-STYLE TASK 73 — TRIANGLE TYPE
# ------------------------------------------------------------
#
# Write a function named:
#
def triangle_type(a,b,c):
    if a ^ 2 + b ^2 == c ^2 or b ^ 2 + c ^2 == a ^ 2 or a ^ 2 + c ^ 2 == b ^ 2:
        if (a == b == c):
         return "equilateral"
        elif a == b or b == c or a == c:
         return "isosceles"
        else:
            return "scalene"
    else:
        return "invalid"
#
# Parameters:
#
# a
# b
# c
#
# First, determine whether the three sides form a valid triangle.
#
# If they do NOT, RETURN:
#
# "invalid"
#
# If all three sides are equal, RETURN:
#
# "equilateral"
#
# If exactly two sides are equal, RETURN:
#
# "isosceles"
#
# Otherwise RETURN:
#
# "scalene"
#
# Examples:
#
# triangle_type(3, 3, 3)   -> "equilateral"
# triangle_type(5, 5, 8)   -> "isosceles"
# triangle_type(3, 4, 5)   -> "scalene"
# triangle_type(1, 2, 10)  -> "invalid"
#
# THINK:
# Check whether the triangle is valid BEFORE classifying it.


# ------------------------------------------------------------
# LEETCODE-STYLE TASK 74 — ROCK PAPER SCISSORS
# ------------------------------------------------------------
#
# Write a function named:
#
def rps_winner(player1,player2):
    if player1 == "rock":
        if player2 == "scissors":
            return player1
        elif player2 == "paper":
            return player2
        else:
            return "tie"
    elif player1 == "scissors":
        if player2 == "rock":
            return player2
        elif player2 == "paper":
            return player1
        else:
            return "tie"
    elif player1 == "paper":
        if player2 == "scissors":
            return player2
        elif player2 == "rock":
            return player1
        else:
            return "tie"
    else:
        return "Make a valid selection"
#
# Parameters:
#
# player1
# player2
#
# Each argument will be:
#
# "rock"
# "paper"
# or
# "scissors"
#
# RETURN:
#
# "tie"
#
# if both players choose the same thing.
#
# RETURN:
#
# "player1"
#
# if player 1 wins.
#
# RETURN:
#
# "player2"
#
# if player 2 wins.
#
# Rules:
#
# rock beats scissors
# scissors beats paper
# paper beats rock
#
# Examples:
#
# rps_winner("rock", "scissors")  -> "player1"
# rps_winner("paper", "rock")     -> "player1"
# rps_winner("rock", "paper")     -> "player2"
# rps_winner("paper", "paper")    -> "tie"
#
# This is a logic problem.
# There are several possible combinations.


# ------------------------------------------------------------
# LEETCODE-STYLE TASK 75 — CLOSEST TO 100
# ------------------------------------------------------------
#
# Write a function named:
#
def closest_to_100(a,b):
    
    if (100 - a) < (100 - b):
        return a
    elif (100 - a) == (100 - b):
        return -1
    else:
        return b
# Parameters:
#
# a
# b
#
# RETURN whichever number is closer to 100.
#
# If they are equally far away from 100, RETURN:
#
# -1
#
# Examples:
#
# closest_to_100(90, 80)    -> 90
# closest_to_100(105, 120)  -> 105
# closest_to_100(90, 110)   -> -1
#
# RESTRICTION:
# Do NOT use abs().
#
# THINK:
# A number may be above OR below 100.
# You will need to determine each number's distance from 100.


# ------------------------------------------------------------
# LEETCODE-STYLE TASK 76 — DELIVERY FEE
# ------------------------------------------------------------
#
# Write a function named:
#
def delivery_fee(order_total,distance):
    if order_total >= 50 and distance <= 5:
        return 0
    elif distance <= 5:
        return 5
    else:
        return 10
#
# Parameters:
#
# order_total
# distance
#
# Rules:
#
# If order_total is $50 or more AND distance is 5 miles or less:
# RETURN 0
#
# Otherwise, if distance is 5 miles or less:
# RETURN 5
#
# Otherwise:
# RETURN 10
#
# Examples:
#
# delivery_fee(60, 3)  -> 0
# delivery_fee(30, 3)  -> 5
# delivery_fee(60, 8)  -> 10
# delivery_fee(30, 8)  -> 10
#
# THINK:
# A large order does NOT always mean free delivery.


# ------------------------------------------------------------
# LEETCODE-STYLE TASK 77 — ATM WITHDRAWAL
# ------------------------------------------------------------
#
# Write a function named:
#
def can_withdraw(balance,amount):
    if amount > 0 and amount <= balance and amount % 20 == 0:
        return True
    else:
        return False

#
# Parameters:
#
# balance
# amount
#
# A withdrawal is allowed only if:
#
# - amount is greater than 0
# - amount is less than or equal to balance
# - amount is divisible by 20
#
# RETURN True if the withdrawal is allowed.
# Otherwise RETURN False.
#
# Examples:
#
# can_withdraw(500, 100)  -> True
# can_withdraw(500, 125)  -> False
# can_withdraw(50, 100)   -> False
# can_withdraw(500, 0)    -> False
#
# ALL conditions must be true.


# ------------------------------------------------------------
# LEETCODE-STYLE TASK 78 — RESTAURANT TIP
# ------------------------------------------------------------
#
# Write a function named:
#
def tip_amount(bill,service):
    if service == "poor":
        return (bill * 0.10)
    elif service == "good":
        return (bill * 0.18)
    elif service == "excellent":
        return (bill * 0.25)
    else:
        return "Sorry didnt get that"
#
# Parameters:
#
# bill
# service
#
# service will be:
#
# "poor"
# "good"
# or
# "excellent"
#
# Tip rules:
#
# poor       -> 10%
# good       -> 18%
# excellent  -> 25%
#
# RETURN the tip amount.
#
# Examples:
#
# tip_amount(100, "poor")       -> 10
# tip_amount(100, "good")       -> 18
# tip_amount(100, "excellent")  -> 25
# tip_amount(80, "good")        -> 14.4
#
# THINK:
# RETURN only the TIP, not the final bill.


# ------------------------------------------------------------
# LEETCODE-STYLE TASK 79 — PHONE BATTERY WARNING
# ------------------------------------------------------------
#
# Write a function named:
#
def battery_status(battery,is_charging):
    
    if battery <= 5 and not is_charging:
        return "critical"
    elif battery <= 20 and not is_charging:
        return "low"
    elif is_charging:
        return "Charging"
    else:
        return "Normal"
    
    
    
#
# Parameters:
#battery
# is_charging
#
# RETURN:
#
# "critical"
# if battery is 5 or lower AND it is NOT charging
#
# "low"
# if battery is 20 or lower AND it is NOT charging
#
# "charging"
# if is_charging is True
#
# "normal"
# otherwise
#
# Examples:
#
# battery_status(3, False)   -> "critical"
# battery_status(15, False)  -> "low"
# battery_status(3, True)    -> "charging"
# battery_status(80, False)  -> "normal"
#
# THINK:
# The order of the conditions matters.


# ------------------------------------------------------------
# LEETCODE-STYLE TASK 80 — TAXI FARE
# ------------------------------------------------------------
#
# Write a function named:
#
def taxi_fare(miles,is_night):
    if is_night:
        total = 9 + miles * 2
        return total
    else:
        total = 4 + miles * 2
        return total
#
# Parameters:
#
# miles
# is_night
#
# Fare rules:
#
# Base fare: $4
# Each mile: $2
#
# If is_night is True, add a $5 night fee.
#
# RETURN the total fare.
#
# Examples:
#
# taxi_fare(0, False)  -> 4
# taxi_fare(5, False)  -> 14
# taxi_fare(5, True)   -> 19
#
# Build the final answer from the rules instead of
# hard-coding different totals.


# ------------------------------------------------------------
# LEETCODE-STYLE TASK 81 — GAME DAMAGE
# ------------------------------------------------------------
#
# Write a function named:
#
def calculate_damage(attack,defense,critical):
    damage = attack - defense
    if damage < 0:
        return 0
    elif critical:
        return damage * 2
    else:
        return damage
#
# Parameters:
#
# attack
# defense
# critical
#
# First calculate:
#
# damage = attack - defense
#
# If damage would be less than 0, damage becomes 0.
#
# If critical is True, DOUBLE the damage.
#
# RETURN the final damage.
#
# Examples:
#
# calculate_damage(20, 5, False)  -> 15
# calculate_damage(20, 5, True)   -> 30
# calculate_damage(5, 20, False)  -> 0
# calculate_damage(5, 20, True)   -> 0
#
# THINK:
# The critical hit should happen AFTER defense is removed.


# ------------------------------------------------------------
# LEETCODE-STYLE TASK 82 — STORE COUPON
# ------------------------------------------------------------
#
# Write a function named:
#
def final_price(price,coupon):
    if coupon == "none":
        return price
    elif coupon =="SAVE10":
        return price * 0.9
    elif coupon == "SAVE25":
        return price * 0.75
    else:
        return "Invalid Coupon"
    
#
# Parameters:
#
# price
# coupon
#
# coupon will be:
#
# "none"
# "SAVE10"
# "SAVE25"
#
# Rules:
#
# "none"   -> no discount
# "SAVE10" -> 10% off
# "SAVE25" -> 25% off
#
# RETURN the FINAL price after the discount.
#
# Examples:
#
# final_price(100, "none")    -> 100
# final_price(100, "SAVE10")  -> 90
# final_price(100, "SAVE25")  -> 75
# final_price(80, "SAVE25")   -> 60
#
# THINK:
# A 25% discount means the customer pays 75% of the price.


# ============================================================
# GIT CHECK
# ============================================================

# When you are completely finished:
#
# 1. Save your file.
# 2. Run your ENTIRE program.
# 3. Fix all errors.
# 4. Make sure you can explain your code.
#
# Then use:
#
# git status
# git add .
# git commit -m "Complete conditionals and functions challenge"
# git push
