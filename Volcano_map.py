import folium
import pandas


data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

def color_markers(elevation):
        if elevation < 1500:
            return "green"
        elif 1500 <= elevation < 3000:
            return "orange"
        else: return "red"

map = folium.Map(location= [43.2669436869802, -118.35818964335239], zoom_start=5, tiles="Stamen Terrain")

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

fgv = folium.FeatureGroup(name="Volcanos")

for lt, ln, el, nm in zip(lat, lon, elev, name):
    #fg.add_child(folium.Marker(location=[lt, ln], popup=str(el)+"m", icon=folium.Icon(color=color_markers(el))))
    fgv.add_child(folium.CircleMarker(location=[lt, ln],radius=6, popup="Volcano\n\n" + "Name:" + nm + "\n\nElevation:" + str(el) + "m",
    fill_color=color_markers(el), color="grey", fill_opacity=0.7))


map.add_child(fgp)
map.add_child(fgv)
map.add_child(folium.LayerControl())
map.save("Map.html")
