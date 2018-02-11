#!/usr/bin/env python3

#Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that 
# they will turn 100 years old.

#Extras:

#Add on to the previous program by asking the user for another number 
# and printing out that many copies of the previous message. 
# (Hint: order of operations exists in Python)
#Print out that many copies of the previous message on separate lines. 
# (Hint: the string "\n is the same as pressing the ENTER button)

import time

name = input ("Give me your name: ")
age = input ("Give me your age: ")

if int(age) >= 100:
    print("Wow, you are very old, just like my dad who is 182 years old.")
else:
    currentyear = time.strftime("%Y")

    year_difference = str(100 - int(age))

    year_i_will_be_100_years_old = int(currentyear) + int(year_difference)
    #print ("You will be 100 years old in " +year_i_will_be_100_years_old)
    print ("{} you will be 100 years old in {}".format(name, year_i_will_be_100_years_old))