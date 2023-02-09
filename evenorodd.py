"""
The Complete Python Pro Bootcamp for 2023
Name: Namthi Nguyen
Day 3 exercise #1: Even or odd

"""

#this take an users input for number they want to check
numberforcheck = int(input("What number do you want to check? "))

# this if statement takes in the number and checks for remainder
if numberforcheck % 2 == 0:
    print(f"The number {numberforcheck} .. is a even number")
else:
    print(f"The number {numberforcheck} .. is a odd number")
