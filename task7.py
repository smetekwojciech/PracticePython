#Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
import random

my_random_list=[]
for i in range (20):
    i=random.randint(0,500)
    my_random_list.append(i)
print(my_random_list)  

new_list=[number for number in my_random_list if number%2==0]
print(new_list)