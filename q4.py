#
# Name : Dylan Le Voguer
# Assignment 1, Question 4
#

# importing pi from math module
from math import pi
def printHeader(headerCorner,headerBorder, headerSide,companyName):
    companyIntro = "Welcome to "+companyName+"!"
    print(companyIntro)
    print(f"{headerCorner}{headerBorder * (len(companyIntro) + 2)}{headerCorner}")
    print(f"{headerSide} {companyIntro} {headerSide}")
    print(f"{headerCorner}{headerBorder * (len(companyIntro) + 2)}{headerCorner}")

#calling printHeader function
printHeader("+","-","|","CyberCone")

numOfScoops = int(input("How many scoops do you want? "))
print(f"Ok, {numOfScoops} scoops it is.\n")

#ask and print scoop radius, using f strings
scoopRadius = float(input("What is the radius of a scoop in cm? "))
print(f"Each scoop is radius {scoopRadius:.2f}cm\n")

#ask and print cone height, using f strings
coneHeight = float(input("What is the height of the cone in cm? "))
print(f"Cone height is {coneHeight:.2f}cm\n")

#cone volume equation
coneVolume = (pi * scoopRadius ** 2 * coneHeight) / 3

#scoop volume equation
scoopVolume = (4/3) * pi * scoopRadius ** 3

#printing cost and height of cone using f strings
print(f"Cost of your {numOfScoops}-scoop cone: ${((numOfScoops * scoopVolume * 0.75)+ coneVolume * 0.25):.2f}")
print(f"Total height of your {numOfScoops}-scoop cone: {(scoopRadius * 2) * numOfScoops + coneHeight:.2f}cm")