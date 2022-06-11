from turtle import color
import folium
import pandas
#this can change to input 
data=pandas.read_csv("Volcanoes.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
map=folium.Map(location=[40.952867949238545, -74.47913250462051],zoom_start=6,titles="Stamen Terrain")
fg=folium.FeatureGroup(name="map")

#this loop will go through thelist same time, lt go to  lat, ln go to lon 
for lt,ln in zip(lat,lon):
    fg.add_child(folium.Marker(location=[lt,ln],popup="This is a Marker",icon=folium.Icon(color='blue')))
#fg.add_child(folium.Marker(location=[36.2,-99.1],popup="A Marker",icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("New_York_map.html")
