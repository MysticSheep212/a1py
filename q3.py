#
# Name : Dylan Le Voguer
# Assignment 1, Question 3
#

#asking for user message
userMessage = input("What do you want your sign to say? ")

#asking for user character
userCharacter = input("What character do you want for the box? ")

#calculating width of box
width = len(userMessage) + 4

#printing box
print(userCharacter * width)
print(userCharacter + " " + userMessage + " " + userCharacter)
print(userCharacter * width)