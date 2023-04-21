print("Welcome to the Love Calcualtor!")
name1 = input("what is your name? \n")
name2 = input("what is their name? \n")

combine_name = name1 +  name2
namelower =  combine_name.lower() 

t = namelower.count("t")
r = namelower.count("r")
u = namelower.count("u")
e = namelower.count("e")
true = t + r + u + e

l = namelower.count("l")
o = namelower.count("o")
v = namelower.count("v")
e = namelower.count("e")

love = l + o + v + e

finalresult = int(str(true) + str(love)) 

if finalresult < 10 or finalresult > 90:
    print(f"Your score is {finalresult}, you go together like coke and mentos.")
elif finalresult >= 40 and finalresult <= 50 :
        print(f"Your score is {finalresult}, you are alright together.")
        
else:
   print(f"Your score is {finalresult}.") 