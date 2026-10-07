import random ## Gives us access to the random function allowing us to generate a random number

random_number = random.randint(1,10) ### Generates a random number between 1 and 10

previous_guesses = [] ## Stores the previous gusses in this list
tries = 5
user_guess = 0

while(user_guess != random_number and tries > 0): ## repeats the user process of asking a number.
    user_guess = int(input("Enter a number between 1-10: "))
    print(f"Previous Gusses: {previous_guesses}")
    if(user_guess not in previous_guesses):
    
        if(user_guess > 10 or user_guess <= 0):
            print("Invalid input")
        elif(user_guess > random_number):
            previous_guesses.append(user_guess) ## Adds the valid guess into previous guess list
            tries-=1
            print("Too High")
            print(f"Tries left:{tries}")
        elif(user_guess < random_number):
            previous_guesses.append(user_guess) ## Adds valid guess into previous guess list
            tries-=1
            print("Too Low")
            print(f"Tries left:{tries}")
        else:
            print(f"congrats You win!!!!")
            previous_guesses.append(user_guess) ### Adds valid guess into previous guess list
            tries-=1
            print(f"Your Guesses:{previous_guesses}")
            print(f"Your tries:{tries}")

print("Game Over!!!") ### YOU LOSE
print(f"Guesses:{previous_guesses}")
print(f"Correct number was {random_number}")

            
        
            
