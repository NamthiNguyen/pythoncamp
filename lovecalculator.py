print("Welcome to the Love Calcualtor!")
name1 = input("what is your name? \n")
name2 = input("what is their name? \n")

# combine_name = name1 +  name2
# namelower =  combine_name.lower() 

# t = namelower.count("t")
# r = namelower.count("r")
# u = namelower.count("u")
# e = namelower.count("e")
# true = t + r + u + e

# l = namelower.count("l")
# o = namelower.count("o")
# v = namelower.count("v")
# e = namelower.count("e")

# love = l + o + v + e

# finalresult = int(str(true) + str(love)) 

# if finalresult < 10 or finalresult > 90:
#     print(f"Your score is {finalresult}, you go together like coke and mentos.")
# elif finalresult >= 40 and finalresult <= 50 :
#         print(f"Your score is {finalresult}, you are alright together.")
        
# else:
#    print(f"Your score is {finalresult}.") 

lowercase_name1 = name1.lower()
lowercase_name2 = name2.lower()

L = lowercase_name1.count("l") + lowercase_name2.count("l")
o = lowercase_name1.count("o") + lowercase_name2.count("o")
v = lowercase_name1.count("v") + lowercase_name2.count("v")
e = lowercase_name1.count("e") + lowercase_name2.count("e")
love = L + o + v + e

t = lowercase_name1.count("t") + lowercase_name2.count("t")
r = lowercase_name1.count("r") + lowercase_name2.count("r")
u = lowercase_name1.count("u") + lowercase_name2.count("u")
ee = lowercase_name1.count("e") + lowercase_name2.count("e")
true = t + r + u + ee

truelove = int(str(true) + str(love))

if truelove < 10 or truelove > 90:
    print(f"Your score is {truelove} , you go together like coke and mentos.")
elif truelove >=40 and truelove <=50:
    print(f"Your socre is {truelove} , you are alright together.")
else:
    print(f"Your score is {truelove}.")
