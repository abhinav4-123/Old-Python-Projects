# class Car:
#     def __init__(self,seats):
#         # print("New user being created...")
#         self.seats = seats
#         # initialise


    # def enter_race_mode(self):
    #     self.seats =2
# user_1=User()


#constructor allows us what will happen when an object will be created . or this is called initializer.
#we use init function

# eg.

# my_car=Car(5)
#same as creating a car object and then setting its seat

class User():
    def __init__(self,user_id,username):
        self.id=user_id #these names can be different too
        self.username=username #will see this self much when creating the class
        self.followers=0
        self.following=0

    def follow(self, user):
        user.followers+=1
        self.following+=1

user_1=User("001", 'abhinav')

# print(user_1.username)


# user_2=User() #this will throw error now , coz this class is defined with the init method, that means whenever an object is defined with this class, 2 values need to be passed.
# user_2.id='002'
# user_2.name='areliya'

user_2=User('002','areliya')

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
# now , there may be some default values , eg. initially instagram follower starting with 0
# e.g. self.followers=0

# attributes are the things object have and methods are the things object does
#quiz game .
