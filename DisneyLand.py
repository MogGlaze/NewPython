## Introduction prints for user
print("Welcome to the Disneyland Budget Manager")
print("I will ask you questions about your trip")
print("Then I will calculate your estimate for the trip")
##Asks user for name
name = input("What is your name: ")

##Asks for number of people
number_of_people = int(input("How many people are going to Disneyland?:"))

## Asks for park of days
number_of_park_days = int(input("How many days will you spend at Disneyland?:"))

#Asks for hotel days
nunber_of_hotel_days = int(input("How many nights will you stay at a hotel?:"))

print("")
## Asks for price of Day Park Hopper(3 DAY HOPPER 535.00)
Day_Park_Hopper = float(input("What is the Park Hopper ticket price per person?:"))

## Asks for Total ticket Cost
total_ticket_cost = Day_Park_Hopper * number_of_people

food_cost_per_person = float(input("How much will ONE person spend on food each day?:"))

total_food_cost = food_cost_per_person * number_of_people * number_of_park_days

souvenir_cost_per_person = float(input("How much will ONE person spend on souvenirs?:"))

total_souvenir_cost = souvenir_cost_per_person * number_of_people
print("")


hotel_per_night_cost = float(input("How much does ONE hotel room cost per night?:"))

total_hotel_rooms = int(input("How many hotel rooms will your group need?:"))

total_hotel_cost = hotel_per_night_cost * total_hotel_rooms *  nunber_of_hotel_days
print("")

one_way_distance = float(input("How many miles away from Disneyland do you live?:"))

vehicle_mpg = float(input("How many miles per gallon does your vehicle get?:"))

round_trip_distance = 2 * one_way_distance
## Finds the average national gas price(=4.09) as a decimal
gas_price = float(input("What is today's price of regular gas per gallon?:"))

gallons_needed = round_trip_distance / vehicle_mpg

total_gas_cost = gallons_needed * gas_price

daily_parking_cost = float(input("How much does Disneyland parking cost per day?:"))

print("")
total_parking_cost = daily_parking_cost * number_of_park_days
## Calculates total trip cost
final_trip_cost =  round(total_food_cost + total_gas_cost + total_parking_cost + total_souvenir_cost + total_hotel_cost + total_ticket_cost,2)
## Calculates average cost per person
cost_per_person = final_trip_cost / number_of_people
## Calculates average cost per day
cost_per_day = final_trip_cost / number_of_park_days

trip_budget = float(input("How much money does your group have available for the Disneyland trip?:"))

budget_difference = round(trip_budget - final_trip_cost,2)

print("")
#### Review
print("DISNEYLAND TRIP REPORT ---------")
print("")
print(f"Traveler:{name}")
print("")
print(f"People Going:{number_of_people}")
print(f"Disneyland Park Days:{number_of_park_days}")
print(f"Hotel Nights:{nunber_of_hotel_days}")
print("")

print("PARK HOPPER TICKETS ---------")
print("")
print(f"Park hopper Price Per Person:${Day_Park_Hopper:.2f}")
print(f"Total Ticket Cost:${total_ticket_cost:.2f}")
print("")

print("ADD ONS ---------")
print("")

print(f"Total Food Cost:${total_food_cost:.2f}")
print(f"Total Sourvenir Cost:${total_souvenir_cost:.2f}")
print("")
print("HOTEL ---------")
print("")
print(f"Total Hotel Cost:${total_hotel_cost:.2f}")
print("")
print("DRIVING ---------")
print("")
print(f"Round-Trip Distance:{round_trip_distance:.2f}")
print(f"Gallons required:{gallons_needed:.2f}")
print(f"Total Gas Cost:${total_gas_cost:.2f}")
print(f"Parking:{total_parking_cost:.2f}")
print("")
print("TRIP TOTAL------")
print("")
print(f"Total Disneyland Trip Cost(Excluding Taxes):${final_trip_cost:.2f}")
print("")
print(f"Average Cost Per Person:${cost_per_person:.2f}")
print(f"Average Cost Park Day:${ cost_per_day:.2f}")
print("")
print("BUDGET------")
print("")
print(f"Trip Budget:${trip_budget:.2f}")
print(f"Budget Difference:${budget_difference:.2f}")
print("")
print("Mickey Mouse would thank you for your money")
print("Follow the path to your Magic Journey")




