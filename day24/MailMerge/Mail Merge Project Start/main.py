#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


letter = []
with open('./Input/Letters/starting_letter.txt') as file:
    lines_as_list = file.readlines()
    for line in lines_as_list:
        letter.append(line)

names = []
with open("./Input/Names/invited_names.txt") as file:
    names_as_list = file.readlines()
    for name in names_as_list:
        names.append(name)
# how to modify the first line in order to change the name
i = 0
for name in names:
    stripped_name = name.strip('\n')  # even can use only strip()
    names[i] = stripped_name
    i += 1
# letter[0].replace("[name]", names[0] )
# print(letter)
for name in names:
    new_first_line = letter[0].replace('[name]', name)
    letter[0] = new_first_line
    with open(f"./Output/ReadyToSend/{name}.txt", mode='w') as file:
        for line in letter:
            file.write(line)

# can see the solution also, that is pretty small and direct
