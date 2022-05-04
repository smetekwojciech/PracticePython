#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
user_Num=int(input("Please enter yout number : \n"))
if (user_Num%2==0):
    print("Your number is even.")
elif (user_Num%2!=0):
    print("Your number is odd.")