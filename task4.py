#Create a program that asks the user for a number and then prints out a list of all the divisors of that number

user_num=int(input("Please enter your number (int)..."))
def number_divisors(number):
    divisors_list=[]
    for i in range (1,number+1):
        if (number%i==0):
            divisors_list.append(i)
    return divisors_list

usernum_divisors_list=number_divisors(user_num)
print("The divisors of your number are :")
print(usernum_divisors_list)