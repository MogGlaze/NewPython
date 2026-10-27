
# Name:
# Period:
# ============================================================
# Python Skills Check — LISTS & LOOPS
# CHALLENGE VERSION — 40 TASKS
# ============================================================
# DIRECTIONS:
# - Create a repository, clone it, and add this file.
# - Complete each task UNDER its directions.
# - Do not delete the directions.
# - Use ONLY concepts learned in class, except for 'in' and 'not in'.
# You must research these two new operators independently in Section 5.
# - Use the EXACT variable and function names provided.
# - The entire file must run without errors.
# - Do not hard-code results Python should calculate.
# - Unless a task says otherwise, do NOT use sum(), min(), max(),
# sorted(), sort(), list comprehensions, sets, or dictionaries.
# - For functions, RETURN values when instructed; do not just print.
# - Test edge cases and change the starting values to check your logic.
# - Tasks that ask for input() may be tested individually.
# ============================================================
# SECTION 1 — LIST FUNDAMENTALS (TASKS 1–6)
# ============================================================
# TASK 1:
# Create a list named scores containing 85, 92, 78, 96, 88.
# Print the entire list and its length using len().
scores = [85,92,78,96,88]
print(len(scores))
# TASK 2:
# Using scores from Task 1, print the FIRST, THIRD, and LAST
# elements on separate lines. Use indexes, not hard-coded values.
print(scores[0])
print(scores[2])
print(scores[-1])
# TASK 3:
# Change the third element of scores to 100.
# Print the updated list. Do not create a replacement list.
scores[2] = 100
# TASK 4:
games = ["Minecraft", "Roblox", "Fortnite"]
games.append("Valorant")
games.insert(1,"Rocket League")
print(games)
# Append "Valorant" and insert "Rocket League" at index 1.
# Print games. Check the order carefully.
# TASK 5:
# Using games from Task 4, remove "Roblox" with remove().
games.remove("Roblox")
removed_game = games.pop()
print(games)
print(removed_game)
# Then pop the FIRST item into a variable named removed_game.
# Print removed_game and the remaining games list.
# TASK 6:
colors = ["red", "blue", "green", "yellow", "purple"]
green_index = colors.index("green")
# Store the index of "green" in green_index using index().
# Print green_index. Then replace "yellow" with "orange".
print(green_index)
colors[3] = "orange"
print(colors)
# Print the new list.
# ============================================================
# SECTION 2 — FOR LOOPS & RANGE (TASKS 7–12)
# ============================================================
# TASK 7:
# Use a for loop with range() to print numbers 1 through 20,
# INCLUDING 20. Do not manually print the numbers.
for i in range(1,21):
    print(i)
# TASK 8:
# Use a for loop with range() to print 30, 27, 24, ... 0.
# IMPORTANT: The zero must be included.
for i in range(30,-1,-3):
    print(i)
# TASK 9:
# Use a for loop to print all EVEN numbers from 1 to 50.
# You MUST use an if statement and the % operator inside the loop.
for i in range(1,51):
    if i % 2 == 0:
        print(i)
# TASK 10:
# Create number = 7.
# Print its multiplication table from 1 through 12 using a for loop.
number = 7
for i in range(1,13):
    print(f"{number} x {i} = {number * i}")
# Example line: 7 x 3 = 21
# Your code must also work if number changes.
# TASK 11:
students = ["Alex", "Jordan", "Taylor", "Morgan", "Casey"]
# Use a for loop to print "Student: " followed by each name.
for names in students:
    print(names)

# Do NOT write five separate print statements.
# TASK 12:
# Using students, print a NUMBERED roster:

for i in range(len(students)):
    print(f"{i}. {students[i]}")
# 1. Alex
# 2. Jordan
# ...
# 5. Casey
# Use range(len(students)) OR enumerate().
# ============================================================
# SECTION 3 — WHILE LOOPS & VALIDATION (TASKS 13–18)
# ============================================================
# TASK 13:
# Create countdown = 10.
# Use a while loop to print from countdown down to 0.
# Then print "Blast off!". Avoid an infinite loop.

countdown = 10
while(countdown != 0):
    print(countdown)
    countdown-=1
print("Blast Off!")
# TASK 14:
password = "Python123"
entry = input("Password: ")
# Keep asking the user for a password until it matches.
# Print "Access granted" exactly once after a correct entry.
while(entry != password):
    entry = input("Password: ")

print("Access granted")
# TASK 15:
# Ask the user for an integer between 1 and 10 INCLUSIVE.
# Keep asking while the value is invalid.
# After a valid entry, print "Valid number".
# Test 0, 1, 10, and 11.
num = 11
while(num > 10 and num < 1):
    num = int(input("Number: "))
    if(num >= 1 and num <= 10):
        break
    print("Invalid")

print("Valid number")


    
# TASK 16:
total = 0
inte = 1
while(inte != 0):
    inte = int(input("What is an integer: "))
    if(inte == 0):
        break
    total += inte
print(total)
# Repeatedly ask for an integer. Add each nonzero entry to total.
# Stop when the user enters 0, then print total.
# Example inputs: 5, 8, -2, 0 -> Total: 11.
# TASK 17:
# Create secret = "robot" and attempts = 3.
secret = "robot"
attempts = 3

guess = ""
while(guess != secret):
    guess = input("Secret?: ")
    if attempts == 0:
        print("You lose")
        break
    attempts -= 1
if(guess == secret):
    print("you Win")
# Ask the user to guess secret, allowing AT MOST 3 guesses.
# Print "Correct" if guessed in time; otherwise "Out of attempts".
# Make sure a correct guess does NOT print both messages.
# TASK 18:
# Make a while-loop menu:
# 1. Say Hello
# 2. Say Goodbye
# 3. Exit

inpput = 0
while(inpput != 3):
    print(" 1.Say Hello")
    print("2.Say Goodbye")
    print("3. Exit")
    inpput = int(input("Option what?: "))
    
    if(inpput == 1):
        print("Hello")
    elif(inpput == 2):
        print("Goodbye")
    else:
        print("Invalid option")
    
# Repeat until the user enters 3. Handle invalid choices.
# Print "Goodbye" only when option 2 is selected.
# ============================================================
# SECTION 4 — PROCESSING LISTS WITH LOOPS (TASKS 19–24)
# ============================================================
# TASK 19:
numbers = [4, 8, 15, 16, 23, 42]
# Use a for loop to calculate and print their total.
# Do NOT use sum().
total = 0
for sum in numbers:
    total += sum
print(total)
# TASK 20:
grades = [90, 85, 78, 92, 88]
sum = 0
average = sum / len(grades)
for sums in grades:
    sum += sums
print(average)
# Use a loop and len() to calculate the average.
# Print the average. Do NOT use sum().
# TASK 21:
numbers = [3, 8, 12, 7, 15, 20, 24, 9]
evens = 0
odds = 0
for nums in numbers:
    if(nums % 2 == 0):
        evens += 1
    else:
        odds += 1

print(f"Even:{evens} Odds:{odds} ")
# Use ONE loop to count even and odd values separately.
# Print "Even: [count]" and "Odd: [count]".
# TASK 22:
numbers = [-14, -67, -23, -89, -45]
high = -10000
for i in range(len(numbers)):
    if numbers[i] > high:
        high = numbers[i]

print(high)
    
# Use a loop to find and print the HIGHEST number.
# Do NOT use max() or sorting.
# IMPORTANT: Starting your answer at 0 gives a wrong result.
# TASK 23:
numbers = [14, 67, 23, 89, 45, 12]
lowest = 1000000

for i in range(len(numbers)):
    if numbers[i] < lowest:
        lowest = numbers[i]
# Use a loop to find and print the LOWEST number.
# Do NOT use min() or sorting.
# Your logic must also work with all-negative numbers.
# TASK 24:
numbers = [5, 2, 5, 8, 5, 3, 2, 5]
target = 5.
count = 0
for num in numbers:
    if num == target:
        count += 1

print(count)
        
# Use a loop to count how often target appears; print the count.
# Do NOT use count(). It must work if target changes.
# ============================================================
# SECTION 5 — IN / NOT IN (TASKS 25–30)
# ============================================================
# INDEPENDENT RESEARCH REQUIRED:
# We have NOT covered 'in' and 'not in' in class. Before starting
# Tasks 25–30, research both operators on your own using reliable
# Python learning resources or the official Python documentation.
# Learn what each operator does, how it works with lists, and how
# to use it inside if statements and while loops.
# Write a short comment in your code explaining the difference
# between 'in' and 'not in' in your own words.
# The examples below are starting hints, NOT a substitute for research.

#Brandon: "IN simply means if the specific data is in a list while NOT IN is simply just the opposite, NOT in the data"

#
# NEW CONCEPT:
# 'in' checks whether a value is in a list.
# Example: "apple" in ["apple", "banana"] evaluates to True.
# 'not in' checks whether a value is missing.
# Example: "grape" not in ["apple", "banana"] evaluates to True.
# These expressions are useful in if statements and while loops.
# TASK 25:
foods = ["pizza", "burger", "tacos", "sushi", "pasta"]
# Ask the user to enter a food.
food = input("FOOD!: ")
if food in foods:
    print("Available")
else:
    print("Not available")
# Use 'in' to print "Available" or "Not available".
# Do NOT use index() to search.
# TASK 26:
supplies = ["pencil", "notebook", "eraser", "backpack"]
supply = input("SUPPLY: ")
if supply not in supplies:
    print("NEED TO BUY")
else:
    print("Already have it")
# Use 'not in' to print "Need to buy" if it is missing,
# otherwise print "Already have it".
# TASK 27:
usernames = ["alex123", "gamer99", "pythonpro"]
username = input("Enter Userame: ")

if username in usernames:
    print("User Taken")
else:
    print("Good Choice")
    usernames.append(username)
# Ask the user to enter a new username.
# If it is already in the list, print "Username taken".
# Otherwise append it and print the updated list.
# Do not allow duplicates.
# TASK 28:
# Modify the idea from Task 27 using a NEW list named accounts.
accounts = ["admin", "guest"]
name = ""
while(name not in accounts):
    name = input("USERNAME ")
    accounts.append(name)
print(accounts)
# Use a while loop to keep asking until the entered name
# is NOT in accounts. Append the accepted name and print accounts.
# REQUIREMENT: Use 'not in' in your solution.
# TASK 29:
secret_words = ["dragon", "robot", "python", "galaxy"]
word = ""
count = 0
while(word not in secret_words):
    word = input("Give a word:")
    count += 1
print(count)
# Keep asking the user for a word UNTIL it is in secret_words.
# Count and print the number of guesses made.
# A correct first guess should count as 1.
# TASK 30:
guests = []
count = 0
name = ""


while(count != 5):
    name = input("Name: ")
    if name not in guests:
        guests.append(name)
        count += 1
    else:
        print("Guest already in")
print(guests)
print(len(guests))
# Ask the user to enter EXACTLY FIVE UNIQUE guest names.
# If a name is already in guests, reject it and ask again.
# Use a while loop, 'in' or 'not in', and append().
# Print the finished list and its length.
# ============================================================
# SECTION 6 — LISTS + FUNCTIONS (TASKS 31–35)
# ============================================================
# TASK 31:
# Create a function named count_positive(numbers).
# RETURN how many elements are greater than 0.
# Do NOT use count().
# Test: count_positive([-2, 0, 4, 9, -1]) -> 2

def count_positive(numbers):
    pos_num = 0
    for num in numbers:
        if num > 0:
            pos_num += 1
    
    return pos_num
print(count_positive([-2,0,4,9,0,-1]))
# TASK 32:
def find_item(items, target):
    index = 0
    for item in items:
        if item == target:
            return index
        elif target not in items:
            return -1
    index += 1

# RETURN the index of the FIRST matching item, or -1 if missing.
# Do NOT use index().
print(find_item(["cat", "dog", "cat"], "cat"))
# Test: find_item(["cat", "dog"], "fish") -> -1
# TASK 33:

            
# Create a function named unique_items(items).
# RETURN a NEW list without duplicate values, preserving first
# appearance order. REQUIREMENT: Use 'not in'.
# Test: unique_items([1, 2, 2, 3, 1, 4]) -> [1, 2, 3, 4]
# TASK 34:
def common_items(list1, list2):
    common = []
    for lis1 in list1:
        if lis1 in list2:
            if lis1 not in common:
                common.append(lis1)
    


    return common
# Create a function named common_items(list1, list2).
# RETURN a NEW list of values found in BOTH lists.
# Include each matching value only once, in list1's order.
# REQUIREMENT: Use both 'in' and 'not in'.
# Test: common_items([1, 2, 3, 3], [3, 4, 1]) -> [1, 3]
# TASK 35:
def reverse_list(items):
    index = 0
    reverse = []
    for i in range(len(items)):
        reverse.append(items[index - i])
    
    return reverse

        
# Create a function named reverse_list(items).
# RETURN a NEW list in reverse order, without changing items.
# Do NOT use reverse(), reversed(), or [::-1].
# Test: reverse_list([10, 20, 30]) -> [30, 20, 10]
# ============================================================
# SECTION 7 — DEBUGGING (TASKS 36–37)
# ============================================================
# TASK 36:
# Fix this code so it prints 1, 2, 3, 4, 5 exactly once each.
# Explain in a comment what was wrong.
#
number = 1
while number <= 5:
    print(number) 
    number += 1 ### Forgot the iteration adding to add the counter
#
# Do NOT replace the while loop with a for loop.
# TASK 37:
# Fix this code so it removes ALL 4s without skipping any.
# Explain in a comment why the original approach can fail.
#
values = [4, 4, 7, 4, 9]
target = 4
while target in values:
    values.remove(target)
print(values)
#
# Expected: [7, 9]
# HINT: A while loop and 'in' can help.
# ============================================================
# FINAL BOSS CHALLENGES (TASKS 38–40)
# ============================================================
# TASK 38 — SHOPPING LIST MANAGER:
# Build a menu-driven program with:

shopping_list = []
choice = 0
while(choice != 5):
    choice = int(input("OPTION: "))
    
    print("1. Add item")
    print("2. Remove item")
    print("3. View numbered items")
    print("4. Search for item")
    print("5. Exit")
    
    if(choice == 1):
        add_item = input("ADD: ")
        if add_item not in shopping_list:
            shopping_list.append(add_item)
          
    elif(choice == 2):
        remove_item = input("Remove what?: ")
        if remove_item in shopping_list:
            shopping_list.remove(remove_item)
    
    elif(choice == 3):
        for item in shopping_list:
            print(f"{item}")
    
    elif(choice == 4):
        searched_item = input("Search what: ")
        if searched_item in shopping_list:
            print("FOUND IT")
        else:
            print("Does not exist")
    else:
        print("Hey I said Pick an option")

print("Goodbye")
        
# Start with shopping_list = [].
# REQUIREMENTS:
# - Use a while loop for the menu and a for loop to display items.
# - Use 'in' to prevent duplicates and 'not in' to reject missing items.
# - Handle an empty list and invalid menu selections.
# - Keep running until the user chooses Exit.
# TASK 39 — GRADE ANALYZER:
highest_grade = 0
lowest_grade = 10000
sum = 0

passing_count = 0
failing_count = 0
def analyze_grades(grades):
    for grade in grades:
        if grade >= highest_grade:
            highest_grade = grade
        elif(grade <= lowest_grade):
            lowest_grade = grade
        if grade >= 70:
            passing_count += 1
        else:
            failing_count += 1
        sum += grade
    if grades == []:
        return []
    else:
        average_grade = sum / len(grade)
        return [highest_grade,lowest_grade,average_grade,passing_count,failing_count]
        

# RETURN a list containing, IN THIS ORDER:
# [highest_grade, lowest_grade, average_grade, passing_count, failing_count]
# Passing means 70 or higher.
# Do NOT use sum(), min(), max(), or sorting.
# For an empty list, RETURN [].
# Test: analyze_grades([95, 82, 67, 74, 58])
# Expected: [95, 58, 75.2, 3, 2]
# Test with a single grade and all-negative values too.
# TASK 40 — STUDENT ATTENDANCE SYSTEM:
# Start with:
students = ["Alex", "Jordan", "Taylor", "Morgan", "Casey"]
present = []
absent = []


for student in students:
        status = input("Was this student Absent or Present? P or A:")
        while(status != "x"):
          if(status == "A"):
                absent.append(student)
                break
          elif(status == "P"):
                present.append(student)
                break
          else:
                print("Present or absent!!")
                break

def attendance_percentage(present,students):
    if students == []:
        return 0
    return len(present)/len(students)

print(present)
print(absent)
print(len(present))
print(len(absent))
print(attendance_percentage(present,students))


            
# For EACH student, ask whether they are Present (P) or Absent (A).
# REQUIREMENTS:
# - Use a for loop to process the student list.
# - Use a while loop to reject anything other than P or A.
# - Prevent duplicate attendance records using 'in' / 'not in'.
# - Print numbered present and absent lists.
# - Print the number present, number absent, and attendance percentage.
# - Print "Perfect Attendance!" if everyone is present.
# - Create attendance_percentage(present, students) that RETURNS
# the percentage; if students is empty, RETURN 0.
# - Test with all present, all absent, and a mixture.
# ============================================================
# END OF CHECKPOINT — REVIEW YOUR WORK BEFORE PUSHING
# ============================================================
