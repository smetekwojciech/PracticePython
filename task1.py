#Program asks user for name and age and prints out the year in which he/she will turn 100.

name=input("What is yout name?")
age=input("How old are you?")

print("Your name is "+name+". You will turn 100 in "+str(100-int(age)+2022))