import csv, folium
import time


def Index():
    # Mở file ra để đọc thông tin
    with open('Quantity.txt', 'r') as file:
        number = file.read() # ==> Nhận được 1 số
    print(number)
    color = ''
    # Kiểm tra điều kiện để tạo mã màu tương ứng với số vừa nhận được
    if int(number) >= 500:
        color = '#FF1105'
    elif int(number) >= 200 and int(number) < 500:
        color = '#F0ED1E'
    else:
        color = '#1EF013'
    # print(color)
    with open('Quantity.txt', 'r') as file:
        number = file.read() # ==> Nhận được 1 số
    print(number)
    color = ''
    # Kiểm tra điều kiện để tạo mã màu tương ứng với số vừa nhận được
    if int(number) >= 500:
        color = '#FF1105'
    elif int(number) >= 200 and int(number) < 500:
        color = '#F0ED1E'
    else:
        color = '#1EF013'
    # print(color)
    with open("temp.txt", "w") as f:
        f.write("Quantity, Color\n")
        f.write(str(number) + ", " + color)

    quantity_list = []
    address_list = ['[21.549124, 105.844724]', '[21.548935, 105.841657]', '[21.549833, 105.850400]']
    color_list = []

    with open('temp.txt', 'r') as file:
        csv_reader = csv.reader(file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            quantity = row[0].strip()
            quantity_list.append(quantity)
            color = row[1].strip()
            color_list.append(color)

    myMap = folium.Map(location=[21.0368, 105.8342], zoom_start=12)

    for address, quantity, color in zip(address_list, quantity_list, color_list):
        lat, long = address.split(', ')
        lat = float(lat.strip('[]'))
        long = float(long.strip(']'))
        address = [lat, long, "Phát hiện có " + quantity + " rác"]
        folium.CircleMarker(location=address[:2], radius=20, color=color, popup='Radius: 50 meters').add_to(myMap)
        # Thay đổi popup_html tùy thuộc vào địa chỉ
        popup_html = '<span style="font-size: 20px;">{}</span>'.format(address[2])
        folium.Marker(location=address[:2], popup=popup_html, auto_open=True).add_to(myMap)

    myMap.save("../HTML/IP.html")

while True:
    Index()
    time.sleep(1)