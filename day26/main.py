# we gonna learn list and dictionary comprehensions today
# this will help us in shortening our code


# LIST COMPREHENSION: a special feature of python
# it is where we create a new list from previous list
# else we would have to use loops
numbers = [1, 2, 3]
# new_list = [new_item for item in list]  keyword method
new_list = [n+1 for n in numbers]  # n just represents each item

# doesn't means we just have to work with list only, but it can be string too
name = 'neha'
letters_list = [letter for letter in name]
print(letters_list)

# list, range, string and tuple are sequences here, and list comprehension go through the sequence here
# e.g.
range_list = [2 * number for number in range(1, 5)]
print(range_list)


# CONDITIONAL LIST COMPREHENSION
# new_list = [new_item for item in list if test]
# e.g.
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# we want list with names of length 4
short_names = [name for name in names if len(name) <= 4]
print(short_names)
# this goes through each name in the list, then checks and then append the name in the new list if condition is
# satisfied
# e.g. >5 turn to uppercase
long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)


# learnt just now that
# with open('file1.txt') as file1:
#   list1 = file1.readlines()
# with open("file2.txt") as file2:
#   list2 = file2.readlines()
# result = [int(n) for n in list1 if n in list2]
#
#
#
#
# # Write your code above 👆
# print(result)

# the above stuff will actually work, here with open just closes the thing after the identation but the created
# variables under them are actually not destroyed


# here then we edited our usStates Game
# list compreshensions are quite popular among the python developers, see how much code can they actually cut out


# DICTIONARY COMPREHENSION: helps us creating a new dictionary from values from a list or dictionary
# new_dict = {new_key : new_value for item in list}  # list here can be any iterable
# this was simplest way, here can be : (dictionary comprehension is basically making dictionary using short syntax)
# new_dic = {new_key : new_value for (key,value) in dict.items())  # looping through each key and value in dictionary
# lets create random student score i.e.
# students_score = {
#     'Alex': 89,
#     etc
# }
import random
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
students_scores = {student:random.randint(0,100) for student in names}
print(students_scores)

# let's loop through a dictionary
passed_students = {student:marks for (student,marks) in students_scores.items() if marks >= 60}
print(passed_students)

# there are then exercises on dictionary comprehension


# string.split() 

