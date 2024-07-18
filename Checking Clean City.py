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


