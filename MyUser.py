print("Hello Paisano!")
print("Mario will ask you a couple of questions.")
print("Then I will find how long you have been alive for.")

## Input asks for User name
name = input("What is your name?: ")

## Input asks for a Integer Birth Year
birth_year = int(input("What year were you born?:"))

## asks for your favorite food
favorite_food = input("What is your favorite food?:")

## asks user for favorite hobby
favorite_hobby = input("What is your favortite hobby?:")
## What city do you live
city = input("What city do you live?: ")

## Asks user their favorite Superhero
favorite_superhero = input("What is your favorite superhero?:")

## Ask user their favorite ride
favorite_amusement_park_ride = input("What is your favorite ride?:")

## Calulcates and stores Age
age = 2026 - birth_year

## Calculates age as month
months_alive = age * 12

##Caluclates the leap year days
leap_year_days = int(age/4)

##Calcuates Days as alive
days_alive = age * 365 + leap_year_days

## Calculates Hours as alive
hours_alive = age * 24 * 365

## Calculates minutes as alive
minutes_alive = age * 24 * 365 * 60

## Calculates seconds as alive
seconds_alive = age * 24 * 365 * 60 * 60

##Prints all of profile information
print("-------Profile-----")
print("Your name is", name)
print("Your birth year is",birth_year)
print("Your favorite food is",favorite_food)
print("Your favorite hobby is",favorite_hobby)
print("Your favorite city",city)
print("Your favorite superhero is",favorite_superhero)
print("Your favorite ride is",favorite_amusement_park_ride)

print("You are", 18 ,"years old")
print("You have been alive for: ")
print("You witnessed",leap_year_days,"leap years")
print(months_alive,"months")
print(days_alive,"days including", leap_year_days, "leap days")
print(hours_alive, "hours")
print(minutes_alive, "minutes")
print(seconds_alive, "seconds")

print("See ya next time")