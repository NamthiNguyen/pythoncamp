# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
pizzabill = 0

if size == "S" or size == "s":
    pizzabill += 15
elif size == "M" or size == "m":
    pizzabill += 20
else:
    pizzabill += 25

if add_pepperoni == "Y" or add_pepperoni == "y":
   if size == "S" or size == "s":
       pizzabill += 2
   else:
        pizzabill += 3
    
if  extra_cheese == "Y" or extra_cheese == "y":
    pizzabill += 1
    
    
print(f"Your final bill for your pizza is: ${pizzabill}.")
    