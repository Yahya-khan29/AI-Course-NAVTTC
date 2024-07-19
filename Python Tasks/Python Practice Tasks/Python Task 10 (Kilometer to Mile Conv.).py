#Python Task 10
#This program Convert Kilometer to Miles

#Taking Kilometer input from the user
Kilo = float(input("Enter Value in Kilometers: "))

#Conversion Factor
conv_fact = 0.621371

#Convert kilometer to miles
miles = Kilo*conv_fact

#Display Miles
print("%0.2f Kilometers is equal to %0.2f Miles"%(Kilo,miles))
