#Displaying Table Task

#Taking Input from User
Num = int(input("Enter the Number to See it's Table : "))

#Displaying Table Logic
print("\nTable of {0} is :".format(Num))
for N in range(1,11):
    print("{0} x {1} = {2}".format(Num,N,(Num*N)))