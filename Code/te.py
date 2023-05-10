# import random
#
# color_list = []
# number_list = []
# address_list = []
# with open('Quantity.txt', 'r') as file:
#     number_list = file.read().split(', ')
#
# with open("temp.txt", "w") as f:
#     f.write("Quantity, Color, Address\n")  # chỉ ghi tiêu đề một lần
#     for number in number_list:
#         if int(number) >= 500:
#             color = '#FF1105'
#             color_list.append(color)
#         elif int(number) >= 200 and int(number) < 500:
#             color = '#F0ED1E'
#             color_list.append(color)
#         else:
#             color = '#1EF013'
#             color_list.append(color)
#         start_lat = 21.54
#         start_long = 105.84
#         add = ([start_lat + random.uniform(-0.01, 0.01), start_long + random.uniform(-0.01, 0.01)])
#         f.write(str(number) + ", " + color + ", " + add + "\n")  # ghi thông tin vào tệp

# import random
#
# # Read the number from file and create color_list
# with open('Quantity.txt', 'r') as file:
#     number = file.read()
# color_list = []
# number_list = number.split(', ')
# for number in number_list:
#     if int(number) >= 500:
#         color = '#FF1105'
#         color_list.append(color)
#     elif int(number) >= 200 and int(number) < 500:
#         color = '#F0ED1E'
#         color_list.append(color)
#     else:
#         color = '#1EF013'
#         color_list.append(color)
#
# # Write the color_list and address_lists to file
# with open('Data.txt', 'w') as file:
#     for i, color in enumerate(color_list):
#         file.write('Color: ' + color + '\n')
#         file.write('latitude,longitude\n')
#         start_lat = 21.54
#         start_long = 105.84
#         address_list = []
#         for j in range(len(color)):
#             address_list.append([start_lat + random.uniform(-0.01, 0.01), start_long + random.uniform(-0.01, 0.01)])
#         for address in address_list:
#             file.write(str(address[0]) + ',' + str(address[1]) + '\n')
#         if i < len(color_list) - 1:
#             file.write('\n')


import random, csv

list_COLOR = []
number_list = []
with open('Quantity.txt', 'r') as file:
    number_list = file.read().split(', ')

with open("temp.txt", "w") as f:
    f.write("Quantity, Color, Address\n")
    for number in number_list:
        if int(number) >= 500:
            color = '#FF1105'
            list_COLOR.append(color)
        elif int(number) >= 200 and int(number) < 500:
            color = '#F0ED1E'
            list_COLOR.append(color)
        else:
            color = '#1EF013'
            list_COLOR.append(color)
        start_lat = 21.54
        start_long = 105.84
        add = [start_lat + random.uniform(-0.1, 0.1), start_long + random.uniform(-0.1, 0.1)]
        add_str = ', '.join(str(x) for x in add)
        line = str(number) + ", " + color + ", [" + add_str + "]\n"
        f.write(line)

quantity_list = []
color_list = []
address_list = []

with open('temp.txt', 'r') as file:
    csv_reader = csv.reader(file, delimiter=',')
    next(csv_reader)
    for row in csv_reader:
        quantity = row[0].strip()
        quantity_list.append(quantity)
        color = row[1].strip()
        color_list.append(color)
        address = row[2].strip() + ", " + row[3].strip()
        address_list.append(address)


print(f"\nĐây là quantity_list: {quantity_list}")
print(f"\nĐây là color_list: {color_list}")
print(f"\nĐây là address_list: {address_list}")



