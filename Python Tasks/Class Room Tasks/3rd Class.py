#Task 1: Use Nested Loop and add values of given lists to the third list by 
#combaining the values of list 1 and list 2

print("----------TASK 1----------")

#Initializing the two lists
FirstName = ["Aslam","Ali"]
LastName = ["Ali","Khan"]

#Declaring the third list
FullName = []

#Logic
for i in FirstName:
    for j in LastName:
        FullName.append(i + " " +j)

#Displaying the result
print(FullName)

#---------------------------------------------------------------------------------------
#Task 2: Deleting Last Index from FullName List

print("\n----------TASK 2----------")

# #Logic 1
# FullName.remove("Ali Khan")
# print(FullName)

#Logic 2
FullName.pop(-1)
print(FullName)

# #Logic 3
# del FullName[-1]
# print(FullName) 

#---------------------------------------------------------------------------------------
#Task 3: Using Nested Loop add in the third list but only combine the 1 index of list 1 
# with the 1 index of list 2 and vice versa

print("\n----------TASK 3----------")
#Initializing the two lists
FirstName_1 = ["Aslam","Ali"]
LastName_1 = ["Ali","Khan"]

#Declaring the third list
FullName_1 = []

#Logic
for i in range(len(FirstName_1)):
    for j in range(len(LastName_1)):
        if(i == j):
            FullName_1.append(FirstName_1[i] + " " +LastName_1[j])

#Displaying the result
print(FullName_1)