# Take a list and write a program that prints out all the elements of the list that are less than 250.
import random

my_random_list=[]
new_list=[]
for i in range (20):
    i=random.randint(0,500)
    my_random_list.append(i)
    if(i<250):
        new_list.append(i)



print("My random list is :")
print(my_random_list)


print("The elements lower than 250 are :")
print(new_list)
