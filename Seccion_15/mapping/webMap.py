import folium       # Importo la librería folium para trabajar con mapas}
import pandas
import json

data = pandas.read_csv("D:/Cursos/Python Mega Course/Seccion_15/data/Volcanoes.txt")  # Leo un archivo CSV que contiene datos de volcanes
lat = list(data["LAT"])  # Extraigo la columna de latitudes
lon = list(data["LON"])  # Extraigo la columna de longitudes
elev = list(data["ELEV"])  # Extraigo la columna de elevaciones
name = list(data["NAME"])  # Extraigo la columna de nombres de volcanes

html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

# Defino una función para crear un mapa con un marcador en una ubicación específica con cordendas dadas
map = folium.Map(location=[-15, -60], zoom_start=3)
map2 = folium.Map(location=[-15, -60], zoom_start=4, tiles="CartoDB positron") # CartoDB positron: Mapa claro y limpio
map3 = folium.Map(location=[-15, -60], zoom_start=4, tiles="CartoDB dark_matter") # CartoDB dark_matter: Mapa oscuro

# Creo un grupo de características para organizar los elementos del mapa
fgVolcanoes1 = folium.FeatureGroup(name="Volcanoes")    # Grupo de características para los volcanes
fgVolcanoes2 = folium.FeatureGroup(name="Volcanoes")  
fgVolcanoes3 = folium.FeatureGroup(name="Volcanoes")  

fgPopulation1 = folium.FeatureGroup(name="Population")  # Grupo de características para la población
fgPopulation2 = folium.FeatureGroup(name="Population")  
fgPopulation3 = folium.FeatureGroup(name="Population")  

fgBorders1 = folium.FeatureGroup(name="Country Borders")  # Grupo para las fronteras de países
fgBorders2 = folium.FeatureGroup(name="Country Borders")  
fgBorders3 = folium.FeatureGroup(name="Country Borders")  

fgDensity1 = folium.FeatureGroup(name="Population Density")  # Grupo para densidad poblacional
fgDensity2 = folium.FeatureGroup(name="Population Density")  
fgDensity3 = folium.FeatureGroup(name="Population Density")  

fgArea1 = folium.FeatureGroup(name="Country Size")  # Grupo para tamaño de países
fgArea2 = folium.FeatureGroup(name="Country Size")  
fgArea3 = folium.FeatureGroup(name="Country Size")  


# ------ Creo Multiples layers (markers, geojson, etc) en el mapa ------

# Creo múltiples marcadores en diferentes ubicaciones usando un bucle
for lt, ln, el, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    # Tipos de marcadores:
    # CircleMarker: Círculo con radio fijo en píxeles
    fgVolcanoes1.add_child(folium.CircleMarker(location=[lt, ln], popup=folium.Popup(iframe), color="grey", fill=True, fill_color=color_producer(el), radius=6, fill_opacity=0.7))
    # Marker: Marcador estándar con ícono
    fgVolcanoes2.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color=color_producer(el))))
    # Otro Marker en un mapa con diferente estilo
    fgVolcanoes3.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color=color_producer(el))))

# Creo un hijo GeoJson para agregar datos geográficos al mapa, lo abro desde un archivo JSON en lectura y codificación utf-8-sig
for fg in [fgPopulation1, fgPopulation2, fgPopulation3]:
    fg.add_child(folium.GeoJson(
    data=open("D:/Cursos/Python Mega Course/Seccion_15/data/world.json", "r", encoding="utf-8-sig").read(),
    style_function=lambda x: {
        'fillColor': 'green' if x['properties']['POP2005'] < 10000000                 # Población menor a 10 millones verde
        else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red' # Población entre 10 y 20 millones naranja, mayor a 20 millones rojo
    }
))

# Capa de fronteras de países con bordes destacados
for fg in [fgBorders1, fgBorders2, fgBorders3]:
    fg.add_child(folium.GeoJson(
        data=open("D:/Cursos/Python Mega Course/Seccion_15/data/world.json", "r", encoding="utf-8-sig").read(),
        style_function=lambda x: {
            'fillColor': 'none',
            'color': 'blue',       # Color de las fronteras
            'weight': 2,           # Grosor de la línea
            'fillOpacity': 0       # Sin relleno
        }
    ))

# Capa de densidad poblacional (colores más detallados)
for fg in [fgDensity1, fgDensity2, fgDensity3]:
    fg.add_child(folium.GeoJson(
        data=open("D:/Cursos/Python Mega Course/Seccion_15/data/world.json", "r", encoding="utf-8-sig").read(),
        style_function=lambda x: {
            'fillColor': '#00ff00' if x['properties']['POP2005'] < 5000000      # Muy baja: verde claro
            else '#90ee90' if x['properties']['POP2005'] < 10000000             # Baja: verde
            else '#ffff00' if x['properties']['POP2005'] < 30000000             # Media: amarillo
            else '#ffa500' if x['properties']['POP2005'] < 50000000             # Media-alta: naranja
            else '#ff4500' if x['properties']['POP2005'] < 100000000            # Alta: naranja rojizo
            else '#ff0000',                                                      # Muy alta: rojo
            'color': 'black',
            'weight': 0.5,
            'fillOpacity': 0.6
        }
    ))

# Capa de tamaño de países por área (estimación basada en población)
for fg in [fgArea1, fgArea2, fgArea3]:
    fg.add_child(folium.GeoJson(
        data=open("D:/Cursos/Python Mega Course/Seccion_15/data/world.json", "r", encoding="utf-8-sig").read(),
        style_function=lambda x: {
            'fillColor': '#87ceeb' if x['properties']['POP2005'] < 1000000      # Países muy pequeños: azul cielo
            else '#4682b4' if x['properties']['POP2005'] < 15000000             # Países pequeños: azul acero
            else '#daa520' if x['properties']['POP2005'] < 50000000             # Países medianos: dorado
            else '#8b4513',                                                      # Países grandes: café
            'color': 'white',
            'weight': 1,
            'fillOpacity': 0.7
        }
    ))

# Primero agrego los grupos de características al mapa
map.add_child(fgVolcanoes1)
map.add_child(fgPopulation1)
map.add_child(fgBorders1)
map.add_child(fgDensity1)
map.add_child(fgArea1)

map2.add_child(fgVolcanoes2)
map2.add_child(fgPopulation2)
map2.add_child(fgBorders2)
map2.add_child(fgDensity2)
map2.add_child(fgArea2)

map3.add_child(fgVolcanoes3)
map3.add_child(fgPopulation3)
map3.add_child(fgBorders3)
map3.add_child(fgDensity3)
map3.add_child(fgArea3)

# Luego se agrega un control de capas a cada mapa para poder activar/desactivar capas
map.add_child(folium.LayerControl())  # Agrego un control de capas al mapa principal
map2.add_child(folium.LayerControl()) # Agrego un control de capas al segundo mapa
map3.add_child(folium.LayerControl()) # Agrego un control de capas al tercer mapa

map.save("D:/Cursos/Python Mega Course/Seccion_15/maps/Map1.html")  # Guardo el mapa en un archivo HTML llamado "Map1.html"
map2.save("D:/Cursos/Python Mega Course/Seccion_15/maps/Map2.html") # Guardo el mapa en un archivo HTML llamado "Map2.html"
map3.save("D:/Cursos/Python Mega Course/Seccion_15/maps/Map3.html") # Guardo el mapa en un archivo HTML llamado "Map3.html"