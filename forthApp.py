#Randomization (Mersenne Twister) and python lists
import random

# Baker roulette App
'''
names = input("Enter your names separated by commas: ")  # Input should be separated by commas
names_list = names.split(",")
names_list = [name.strip() for name in names_list]  # Corrected variable name from 'user' to 'name'
length1 = len(names_list)  # Corrected variable name from 'lenght1' to 'length1'
random_name = random.randint(0, length1 - 1)
a = names_list[random_name]  # Corrected variable name from 'names' to 'names_list'
print(names_list)
print(f"{a} is going to pay the bill.")
'''

#List of statesof the US
'''
states_of_america = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware",
    "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky",
    "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri",
    "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York",
    "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island",
    "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia",
    "Washington", "West Virginia", "Wisconsin", "Wyoming"]
states_of_america[1] = "Alask"
count = len(states_of_america)
#states_of_america.extend(["Ianosland", "Dankaland"])
print(count)
'''

'''############################ Coin toss
random_coin = random.randint(0, 1)
if random_coin == 1:
    print("Heads")
else:
    print("Tails")
'''

'''############################## Random number between 1 and 10
random_int = random.randint(1, 10)
print(random_int)
'''
