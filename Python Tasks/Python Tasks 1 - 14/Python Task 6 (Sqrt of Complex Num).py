#Python Task 6
#This program calculates the square root of complex numbers

#Importing complex math module
import cmath

#initializing complex number
num = 1+2j

#calculate sqrt of complex number
num_sqrt= cmath.sqrt(num)

#printing the result
print("The Square root of {0} is {1:0.2f}+{2:0.2f}j".format(num,num_sqrt.real,num_sqrt.imag))
