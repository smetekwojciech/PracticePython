#Collatz problem

def collatz(number):
    if number%2==0:
        return int(number//2)
    elif number%2!=0:
        return int((number*3)+1)
    else:
        print("It's not a number!")

user_number=int(input("Please enter your number(different than 1) :\n"))


while user_number!=1:
    print(str(collatz(user_number)))
    user_number=collatz(user_number)
