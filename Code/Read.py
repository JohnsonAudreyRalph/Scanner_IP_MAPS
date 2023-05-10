import csv
import folium

quantity_list = []
address_list = ['[21.549124, 105.844724]', '[21.548935, 105.841657]', '[21.549833, 105.850400]']
color_list = []

# Đọc thông tin từ file CSV
with open('Info.txt', 'r') as file:
    csv_reader = csv.reader(file, delimiter=',')
    next(csv_reader)
    for row in csv_reader:
        quantity = row[0].strip()
        quantity_list.append(quantity)
        color = row[3].strip()
        color_list.append(color)

# Tạo bản đồ
myMap = folium.Map(location=[21.0368, 105.8342], zoom_start=12)
# print(address_list)

# Thêm các địa điểm vào bản đồ
for address, quantity, color in zip(address_list, quantity_list, color_list):
    lat, long = address.split(', ')
    lat = float(lat.strip('[]'))
    long = float(long.strip(']'))
    address = [lat, long, "Phát hiện có " + quantity + " rác"]
    # Thêm vòng tròn đại diện cho bán kính
    folium.CircleMarker(location=address[:2], radius=20, color=color, popup='Radius: 50 meters').add_to(myMap)
    # Thay đổi popup_html tùy thuộc vào địa chỉ
    popup_html = '<span style="font-size: 20px;">{}</span>'.format(address[2])
    # Thêm đánh dấu và popup cho địa điểm
    folium.Marker(location=address[:2], popup=popup_html, auto_open=True).add_to(myMap)

# Lưu bản đồ vào tệp HTML
myMap.save("../HTML/IP.html")
