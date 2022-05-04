# Take two lists and write a program that returns a list that contains only the elements that are common between the lists without duplicates.
import random

list1,list2,list3=[],[],[]

for i in range (20):
    i=random.randint(0,20)
    list1.append(i)
for i in range (30):    
    i=random.randint(0,30)
    list2.append(i)
for i in range(len(list2)):
    if (list2[i] in list1):
        list3.append(list2[i])
        



print(list1)
print(list2)
print(set(list3))