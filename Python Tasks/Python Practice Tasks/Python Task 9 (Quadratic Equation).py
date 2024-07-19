#Python Task 9
#This program solves the quadratic equation ax**2 + bx + c = 0

#importing the complex math module
import cmath

#initializing the variables a, b and c
a = 1
b = 5
c = 6

#Solution -b +- sqrt(b**2 - 4*a*c) / 2*a

#finding the discriminant
disc =  (b**2) - (4*a*c)

#Finding the solution
Sol_1 = (-b - cmath.sqrt(disc))/(2*a)
Sol_2 = (-b + cmath.sqrt(disc))/(2*a)\

#Displaying the solution
print("The Solutions are {0} and {1}".format(Sol_1,Sol_2))
