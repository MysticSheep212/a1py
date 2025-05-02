#
# Name : Dylan Le Voguer
# Assignment 1, Question 5
#

#imports random module
import random

#randomly choosing between / and \
random.choice('/\\')

#requesting number of rows from user with n variable as requested
n = int(input("Enter a number: "))

#looping through n rows and n*2 columns 
for i in range(n):
    #prints 2 characters because the num of columns is double the num of rows
    for j in range(n*2):
        #prints random character from the options
        print((random.choice('/\\')), end='') 
    #prints a new line 
    print()