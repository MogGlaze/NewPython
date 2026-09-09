import time

def Stats(name,gender,money):
    inventory = []
    myStats = {"Name:" :name,
               "Gender": gender,
               "Money": money,
               "Inventory" : inventory
               }
    
    
def welcome(name):
    print("Welcome to school simulator ")
    time.sleep(2)
    print(f"All you have to do is complete as many tasks and win")
    time.sleep(2)
    print(f"It's going to be a good time,{name}")
    
    
    
def Morning(name):
    print("Ugh its another boring ass day and you got school today")
    time.sleep(2)
    bed = input("It's 6 am and you got another day(Do you want to wake up and catch the bus? Y/N)")
    if bed == "N":
        
        print("WHAT THE FU$K!?, WHAT DO YOU MEAN NO!!?")
        sleep = input("Sleep or realize to wake up")
        if "zzz" in sleep:
            print("okay fine, whatever be late!")
    
    elif bed == "Y":
        print(f"Alright lets put some clothes on {name}")
        print("We got a big day today")
        print("You look in your closet and find 3 pieces of clothing with your favorite shorts") 
        clothes = input("Choose an option. 1.Clown Costume, 2. Formal suit, 3. Casual shirt") 
    
    
print("Alright lets get moving to the most important meal of the day.")
breakfast = int(input("What would you like to eat?(1.Cereal,2. Ribeye Steak, 3. Banana and yogurt, 4. Nothing): "))
if breakfast == 4:
    print("Okay, looks like your going to starve, don't come crying to me")


print("Next, I find it important that we do a quick jog around the block before the school bus arrives")
jog = input("Would you like to jog, your looking a bit fat")

if jog == 'YES':
    print("good choice,lets get rid of those diabetes")
    print("*****JOGGING******")
    print("Hey fat turd stop jogging we are going to be late")
jog_continue =chr(input("Keep Jogging or Go to the bus"))
if jog_continue == "Yes":
    print("HEY, SORR")




    
welcome("Brandon")
