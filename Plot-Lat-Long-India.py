import folium

map = folium.Map(location=[22.00, 78.00], tiles="cartodbpositron", zoom_start=6)

for i in range(len(data)):
    folium.Circle(
        location=[data.iloc[i]["LONGITUDE"], data.iloc[i]["LATITUDE"]],
        radius=100,
        color="blue",
    ).add_to(map)

map
