#Python Task 8
#This program finds the area of triangle

#initializing the sides of triangle
a=5
b=6
c=7

#Calculating the Semi Perimeter
S = (a + b + c)/2

#Calculating Area
Area = (S*(S-a)*(S-b)*(S-c)) ** 0.5

#Displaying Area
print("The of Given Triangle is %0.2f"%Area)
