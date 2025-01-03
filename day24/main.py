# # # how to open, write and read file using python
# # file = open("my_file.txt")
# with open("my_file.txt") as file:
#     contents = file.read() # will return contents as string
#     print(contents)
# # file.close()  # it would have automatically done by the system to free up the resources that has been occupied
# # or can use with open() as file and do inside indent then it's gonna close the file itself


# what if wanna write also

# with open("my_file.txt", mode='w') as file:
#     file.write("New Text. ")  # will clear all the previous contents and write the new
#
# # NOTE: when you try to open a file in write mode that doesn't exist, it will create one for you
# with open("new_file.txt", mode='w') as file:
#     file.write("Hello there!!.")
# this only works in write mode


# # what if you wanna write in the previous
#
# with open('my_file.txt', mode='a') as file:
#     file.write("\nnew appended text.")


# PATH AND DIRECTORY
# files and folders live inside folders
# at the very root of the all folders is the root folder
# now this root maybe hard disk(C DRIVE in windows) for a computer
# this 'root' is represented by '/' : forward slash
# now a folder work in this c drive will be like : /work
# this is how we tell path (this is called absolute file path : it starts from origin, i.e. root)
# RELATIVE FILE PATH:
# suppose we are inside a directory working on our project : called work directory
# we may use relative path directory . eg. maybe a file talk.ppt in working directory:
# can just use "./talk.ppt" (or simply talk.ppt) or maybe agar work directory ke andar koi project name ka folder h and
# then usme talk.ppt h:
# then can do: "./Project/talk.ppt"


# note that here we are starting from a folder that is not necessarily our root folder

# here, we can go up too in the directory tree
# "../report.doc" : we'll go outside the current folder and search for report.doc

# same directory: can do 'file.txt' instead of './file.txt'
# if wrong path : file not found error


# let's play with the thing:


# # absolute path
#
# with open("C:/Users/Dell/OneDrive/Desktop/my_file.txt") as file:
#     contents = file.read()
#     print(contents)
#     # window: each directory separated by backward slash, while it is by forward slash in mac
#     # but it is done by forward slash in python

# # do using relative with main.py
# with open('../../../../C:/Users/Dell/OneDrive/Desktop/my_file.txt') as file:  # i am not getting the correct one
#     contents = file.read()
#     print(contents)


# you might use any depending on the situation


# mail merge project: learnt how we can use google and stackoverflow to use the things which we may not have used before
# there were three functions basically which i learnt here. file handling readlines(), string.replace(old,new,count) and
# string.strip(characters to strip/ by default spaces)


# there is no efficient code, rather focus should be on readability, made code as much readable as possible. Other coder
# s should understand your code by reading it.
# its not about making code short, but its about making your code readable to as much people as you can .
# at least at this stage
