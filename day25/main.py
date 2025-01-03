# # will se working with csv files
# # will be analysing data using pandas library. Pandas is one of the most popular Python data analysis libraries
# # will see how to use it to get insights into our data
# # project: an interactive and educational game
#
#
# # Coding is about shortcuts in life (maybe in case of python)
# # CSV stands for comma separated values, and any excel file can be converted to csv data file version of it
#
#
# # # reading data from csv file:
# #
# # with open("weather_data.csv") as file:
# #     data = file.readlines()
# #     print(data)
#
# # it will need a lot of cleaning before using this data
# # here is when the python data analysis libraries comes into the picture
# # python is widely used for data analysis
#
# # # there is a library csv library for this holy purpose
# #
# # import csv
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)  # this will create a csv reader object, that can be used, e.g. can be looped through
# #     # for example
# #     # for row in data:
# #     #     print(row)  # each row will be retrieved as a list of strings here
# #     # lets extract temperature
# #     temperatures = []
# #     for row in data:
# #         if row[0] != "day":
# #             temperatures.append(int(row[1]))
# #     print(temperatures)
#
# # csv is inbuilt library for csv file handling
# # see, so much faff(bhasad) is involved in even this basic operation
# # wb when having many columns and rows?
# # here is when pandas: a python data analysis library comes into picture
# # it is super-powerful and super-helpful for handling tabular data
# # will need to install it to the project
# import pandas
# # can read getting started guide of the documentation while working with new library( if they have one).
# data = pandas.read_csv("weather_data.csv")  # there are many optional attributes of this method too.
# # print(data)  # this will print the data in tabular form without commas
# # print(data['temp'])  # this is what we have done in csv with lill bit fuss
# # print(type(data))  # class: pandas dataframe
# # that is why most python developers use pandas as soon as they counter with csv files, no matter how small the task
# # is
#
# # there are 2 types of basic data structures: series(1D)- a single column and Dataframe(2D)- whole table
# # there are many functionalities(methods and attributes) associated with these 2 classes
# #e.g.:
# # data_dict = data.to_dict()
# # print(data_dict)
# # similarly, series can be converted to a list
# temp_list = data["temp"].to_list()
# # print(temp_list)
# avg = sum(temp_list) / len(temp_list)
# # print(avg)
#
# # this can also be done using computation and statistics on pandas series (basically there are many methods for this
# # part in pandas
# # print(data['temp'].mean())  # median, etc methods are also there
# # # find max of a column:
# # print(data['temp'].max())
#
# # see, its also easy to get hold of data or basically access data here
# # print(data['condition'])  # take care of spellings(case sensitive)
# # or
# # print(data.condition)  # dataframe basically holds each heading as an attribute
#
# # Get Data in row
# # print(data[data.day == 'Monday'])  # or data['day'] == 'Monday'
# # e.g.: getting the row where temperature was maximum
# # print(data[data.temp == data.temp.max()])  ## i.e. we are filtering rows by some condition
#
# # we also get hold of the particular value in a particular column
# monday = data[data.day == 'Monday']
# # print(monday.condition)
# monday_temp = monday.temp[0]  # monday.temp[0] will give a numerical value, and not an attribute of series
# # print(f"{monday_temp * 1.8 + 32}F")
#
#
# # create a dataframe from scratch
# data_dict = {
#     "students": ['Amy', 'James', 'Angela'],
#     "scores": [76, 56, 65]
# }
# data_new = pandas.DataFrame(data_dict)
# # print(data_new)
# data.to_csv("new_data.csv")
#
# # this clearly shows how powerful this pandas library could be, while dealing with csv data
# # will see other many libraries which similarly makes our work easy of dealing with large chunks of data
# # e.g. Numpy, matpotlib, etc
#
#
#


# turtle works with gif images only
