

file=open("instrukcje.txt",'r')

instruction_list=file.readlines()
file.close()
new_list=[]

for element in instruction_list:
    element=element.rstrip("\n")
    new_list.append(element)

instruction_list=new_list

def create_string(instructions):
    user_string=''
    for element in instructions:
        instruction=element.split(' ')
        if(instruction[0]=='DOPISZ'):
            user_string+=(instruction[1])
        elif(instruction[0]=='ZMIEN'):
            user_string=user_string[:-1]
            user_string+=instruction[1]
        elif(instruction[0]=='USUN'):
              user_string=user_string[:-1]
        elif((instruction[0]=='PRZESUN')) and (instruction[1] in user_string):
            char_code=ord(instruction[1])
            new_char=char_code+1
            if(new_char==91):
                new_char=65
            user_string=user_string.replace(instruction[1],chr(new_char),1)
    print(user_string)
    print(len(user_string))

def longest_same_instruction(instructions):
    counter=1
    max=0
    inst=''
    instruction_list=[]
    for element in instructions:
        instruction=element.split(' ')
        instruction_list.append(instruction)
    for i in range (len(instruction_list)-1):
            if instruction_list[i][0]==instruction_list[i+1][0]:
                counter+=1
                if counter>max:
                    max=counter
                    inst=instruction_list[i][0]
            elif instruction_list[i][0]!=instruction_list[i+1][0]:
                counter=1
    print(inst)
    return max

def longest_same_letter(instructions):
    counter=0
    max=0
    letter=[]
    instruction_list=[]
    letters_list=[]
    for element in instructions:
         instruction=element.split(' ')
         if instruction[0]=='DOPISZ':
             instruction_list.append(instruction)
    for i in range (len(instruction_list)):
        letters_list.append(instruction_list[i][1])
    for i in range (len(letters_list)):
        counter=letters_list.count(letters_list[i])
        if counter>max:
            max=counter
            letter=letters_list[i]
        counter=0           
    print(letter)
    return max

create_string(instruction_list)
print(longest_same_instruction(instruction_list))
print(longest_same_letter(instruction_list))
