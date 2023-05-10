from django.shortcuts import render
import random, csv
from django.http import JsonResponse
from .models import Save_Info


# Create your views here.
def Read(req):
    # Đọc file dữ liệu
    with open('../Code/Quantity.txt', 'r') as file:
        number_list = file.read().split(', ')

    with open("temp.txt", "w") as f:
        f.write("Quantity, Color, Address\n")
        for number in number_list:
            if int(number) >= 500:
                color = '#FF1105'
            elif int(number) >= 200 and int(number) < 500:
                color = '#F0ED1E'
            else:
                color = '#1EF013'
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
        id = 0
        for row in csv_reader:
            quantity = row[0].strip()
            quantity_list.append(quantity)
            color = row[1].strip()
            color_list.append(color)
            address = row[2].strip() + ", " + row[3].strip()
            address_list.append(address)
            lats = row[2].strip()
            lon = row[3].strip()
            save = Save_Info(id=id, quantity=quantity, color=color, Address=address, lat=0, lon=0)
            print(save)
            save.save()
            id += 1

    # Tạo đối tượng JSON chứa dữ liệu đã đọc từ file
    data = {
        'quantity': quantity_list,
        'color': color_list,
        'address': address_list
    }
    return JsonResponse(data)


def Index(req):
    Read(req)
    # data = Save_Info.objects.all()
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
            string = str(address)
            address = string[1:-1]
            # print(address)
        data = {
            'quantity': quantity,
            'color': color,
            'address': address
        }
        print(data)
    return render(req, 'index_2.html', data)
