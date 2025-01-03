import pandas
data = pandas.read_csv('2018squirrelDataCentralPark.csv')
# grey = data[data['Primary Fur Color'] == 'Gray']
# red = data[data['Primary Fur Color'] == 'Cinnamon']
# black = data[data['Primary Fur Color'] == 'Black']
#
# grey_count = grey['Primary Fu'].count()
# red_count = red.count()
# black_count = black.count()
# print(red_count)
# dictionary = {
#     "Gray": [grey_count],
#     "Black": [black_count],
#     "Red": [red_count]
# }
# data_frame = pandas.DataFrame(dictionary)
# print(data_frame)

gray_squirrels_count = len(data[data['Primary Fur Color'] == 'Gray'])
red_squirrels_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirrels_count = len(data[data['Primary Fur Color'] == 'Black'])
data_dictionary = {
    'Fur Color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dictionary)
df.to_csv("squirrel_count.csv")

