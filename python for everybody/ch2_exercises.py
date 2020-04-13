# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 08:53:37 2020

@author: migue
"""


#%% Exercise 2: 
# Write a program that uses input to prompt a user for their name and then 
# welcomes them.

input_name = input("What's your name? ")

print("Welcome, " + input_name)


#%% Exercise 3: 
# Write a program to prompt the user for hours and rate per hour to compute 
# gross pay.

hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

out = hours * rate

print("Pay: " + str(out))

#%% Exercise 4: 
# Assume that we execute the following assignment statements:

width = 17
height = 12.0

print(width // 2)

print(width // 2.0)

print(height / 3)

print(1 + 2 * 5)
    
#%% Exercise 5: 
# Write a program which prompts the user for a Celsius temperature, convert 
# the temperature to Fahrenheit, and print out the converted temperature.

celsius_temp = input("Celsius temperature: ")

fahrenheit_temp = float(celsius_temp) * 9/5 + 32

print("Fahrenheit: " + str(fahrenheit_temp))