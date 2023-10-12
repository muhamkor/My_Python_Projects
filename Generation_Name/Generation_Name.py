# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 21:39:53 2023

@author: mkora
"""

def genaration(b_year):
    # this is a function that computes the name of generation year
    if b_year < 1901:
        return 'to an unknown Generation'
    elif b_year >= 1901 and b_year <= 1924:
        return "The Greatest Generation"
    elif b_year >=1925 and b_year <= 1945:
        return"The Silent Generation"
    elif b_year >=1946 and b_year <= 1964:
        return "The Baby Boomer Generation"
    elif b_year >=1965 and b_year <= 1979:
        return "Generation X"
    elif b_year >=1980 and b_year <= 1994:
        return "Millennial"
    elif b_year >=1995 and b_year <= 2012:
        return "Gen Z"
    elif b_year >=2013 and b_year <= 2025:
        return "Gen Alpha"# using return to make the funtion a fruitful function.
    else:
        return "to a non existing Generation"

while True: # this loop iterates over the input and keeps prompting the user until they type done
    enter_year = input("Enter your Year of Birth to know your Generation Name and done to exit: ")
    if enter_year == 'done':
        break ; quit() # created this code to stop the code when done is typed.
    
    
    try:# this is an error handling code to stop the user from entering bad input 
        b_year = int(enter_year)# the b_year is the parameter we pass to our function to be as the year input by user
        gen_name = genaration(b_year)
        print('You belong to', gen_name)
        
    except ValueError:# text to present to user when the input is bad
        print('Invalid Input, Enter a valid input or done to exit')
        
