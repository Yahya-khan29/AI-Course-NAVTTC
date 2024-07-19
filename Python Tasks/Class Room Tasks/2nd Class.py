#Task 1 Compare user input with given list and if user input matches any
#value in list show clean city else dirty city

print("----------TASK 1----------")

#Initializing Clean city List
Clean_Cities = ["lahore","rawalpindi","multan","gujrat","islamabad"]

#User Input
City_Name = input("Enter your City Name : ")

#Logic 1
# if(City_Name in Clean_Cities):
#         print("Your City is Clean")
# else:
#         print("Your City is Dirty")

#Logic 2
# Result = "Your City is Dirty"
# for City in Clean_Cities:
#         if(City == City_Name):
#                 Result = "Your City is Clean"
# print(Result)

#Logic 3
Result = "Your City is Dirty"
C = 0
while(C < len(Clean_Cities)):
    if(Clean_Cities[C] == City_Name):       
        Result = "Your City is Clean"
    C+=1
print(Result)

#---------------------------------------------------------------------------------------
#Task 2 Taking any integer input from user and
#display it's table

print("\n----------TASK 2----------")

#Taking Input from User
Num = int(input("Enter the Number to See it's Table : "))

#Displaying Table Logic
print("\nTable of {0} is :".format(Num))
for N in range(1,11):
    print("{0} x {1} = {2}".format(Num,N,(Num*N)))


