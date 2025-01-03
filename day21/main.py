# will see class inheritance, slicing and finishing the snake game


# CLASS INHERITANCE: classes can inherit methods, attributes from other class
# will also see slicing of lists and dictionaries
# and then acquiring all these skill, we'll see how to create the Snake Game completing last 4 stages
# todo: detect collision with food
# todo: create a scoreboard
# todo: detect collision with wall
# todo: detect collision with tail

# e.g. chef and pastry chef. Pastry chef knows the things of chef(methods) but also knows certain extra things(methods)
# here pastry chef can inherit some of the methods and attributes of the chef.
# this feature or thing is called inheritance
# what we have to inherit??
# e.g. class Fish(Animal  # name of class from which you want to inherit all attribute and methods
# e.g. :
# class Fish(Animal):
#     def __init__(self):
#         super().__init__()  # here super represent animal class for fish class

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")


class Fish(Animal):
    def __init__(self):
        super().__init__()  # it allows all the objects created with fish class inherit the attributes and methods of
        # animal class

    def breathe(self):  # for the methods which we want to redefine in our child class (called subclass here)
        super().breathe()  # will do everything of animal class (which is the superclass in this case)
        print('doing this underwater.')  # and then it will do rest things, i.e. will pile up next things on the top of
        # what have already been defined or done in the parent class
        # i.e., we can also extend the functionality of the methods of some previous classes

    def swim(self):
        print("Moving in water.")


nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)

# will see the application of the same while inheriting from the turtle class in our remaining part of the project
# turtle.distance(x,y)
# turtle.write(arg, move, align, etc)


# so project is almost done now we'll see slicing and will try to implement it in our project to see how it can make our
# project improved
# the problem in our looping is how wordy it is
# PYTHON SLICING:
# let's say we want to cut list and get a sublist(like sub-arrays)
# we can get part of an array by slicing e.g. list[2:5] let 0 position is before the start of the list and position 1
# between the 0th and 1st element of the list
# other things which we can do with slicing:
# list[2:] : will get all elements from position 2 to end
# similarly, list[:5] will get us all elements before position 5 of the list
# list[2:5:2] will give us every second element from position 2 to position 5
# similarly list[::-1] will give list from end to start


# similarly, we can also use this method of slicing with tuples
# print(list_1[2:5:]), etc.
# challenge: improve main.py of project: solution: see line 45, or without slicing, would have done using our old index
# method

# can customize the snake game: change color/shape of food/snake,etc.
# learnt concept of inheritance in oop and slicing list and tuples in the project


# on the point where have to bring your self motivation. it is a marathon and not a sprint.
# what do you want at the end of the path? think.....!
