from turtle import color
import folium
import pandas
#this can change to input

def color_producer(elevation):
    if elevation<1000:
        return 'green'
    elif 1000<=elevation<3000:
        return 'orange'
    else:
        return 'red'
data=pandas.read_csv("Volcanoes.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])
map=folium.Map(location=[40.952867949238545, -74.47913250462051],zoom_start=6,titles="Stamen Terrain")
fg=folium.FeatureGroup(name="map")
#this loop will go through thelist same time, lt go to  lat, ln go to lon
for lt,ln,el in zip(lat,lon,elev):
    fg.add_child(folium.Marker(location=[lt,ln],popup=folium.Popup(str(el),parse_html=True),icon=folium.Icon(color=color_producer(el))))
#fg.add_child(folium.Marker(location=[36.2,-99.1],popup="A Marker",icon=folium.Icon(color='green')))
fg.add_child(folium.GeoJson(data=(open('world.json','r',encoding='utf-8-sig').read())))
map.add_child(fg)
map.save("New_York_map.html")
