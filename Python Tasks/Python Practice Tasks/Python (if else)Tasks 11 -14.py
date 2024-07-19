#Python Task 11
#This task is to understand if statment

print("----------TASK 11----------")
i = 10
if(i > 15):
    print("10 is less than 15")
print("I am not in if")

#----------------------------------------------------------------------------
#Python Task 12
#This task is to understand if and else statments

print("----------TASK 12----------")
i = 20
if(i < 15):
    print("i is smaller than 15")
    print("i am in if block")
else:
    print("i is greater than 15")
    print("i am in else block")
print("I am not in if and not in else block")

#----------------------------------------------------------------------------
#Python Task 12
#This task is to understand Nested if and else statments

print("----------TASK 13----------")
i = 10
#First if statment
if(i == 10):
    #Nested if statment only executed if above if is true
    if(i < 15):
        print("i is smaller than 15")
    if(i < 12):
        print("i is smaller than 12 too")
    else:
        print("i is greater than 15")

#----------------------------------------------------------------------------
#Python Task 14
#This task is to understand if, elif and else statments

print("----------TASK 14----------")

i =20
if(i ==10):
    print("i is 10")
elif(i == 15):
    print("i is 15")
elif(i ==20):
    print("i is 20")
else:
    print("i is not present")