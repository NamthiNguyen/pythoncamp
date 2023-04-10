# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
pizzabill = 0

if size == "L" or size == "l":
    pizzabill = 25
    if add_pepperoni == "Y":
        pizzabill += 3

elif size == "M" or size == "m":
    pizzabill = 20
    if add_pepperoni == "Y":
        pizzabill += 3

elif size == "S" or size == "s":
    pizzabill = 15
    if add_pepperoni == "Y":
        pizzabill += 2
    
else:
    print("Do you not want to order pizza?")


if extra_cheese == "Y" or extra_cheese == "y":
    pizzabill += 1
    
print(f"Your final bill for your pizza is ${pizzabill}.")
    