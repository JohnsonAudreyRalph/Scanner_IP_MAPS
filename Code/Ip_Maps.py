import folium

# Tạo một danh sách chứa nhiều địa chỉ và thông tin popup tương ứng
addresses = [[21.569491, 105.869574, "Phát hiện có 250 rác"], [21.570920, 105.871301, "Phát hiện có 10 rác"]]

# Tạo bản đồ
myMap = folium.Map(location=addresses[0][:2], zoom_start=12)

# Thêm các địa điểm vào bản đồ bằng vòng lặp
for address in addresses:
    # Thêm vòng tròn đại diện cho bán kính
    folium.CircleMarker(location=address[:2], radius=50, fill_color='#3186cc', popup='Radius: 50 meters').add_to(myMap)
    # Thay đổi popup_html tùy thuộc vào địa chỉ
    popup_html = '<span style="font-size: 20px;">{}</span>'.format(address[2])
    # Thêm đánh dấu và popup cho địa điểm
    folium.Marker(location=address[:2], popup=popup_html, auto_open=True).add_to(myMap)

# Lưu bản đồ vào tệp HTML
myMap.save("../HTML/IP_2.html")
