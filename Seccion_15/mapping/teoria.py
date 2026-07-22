import folium       # Importo la librería folium para trabajar con mapas

print(dir(folium))    # Listo los atributos y métodos disponibles en la librería folium

"""
Output:
['Choropleth', 'Circle', 'CircleMarker', 'ClickForLatLng', 'ClickForMarker', 'ColorLine', 'ColorMap', 'Control', 'CssLink', 'CustomIcon', 'Div', 'DivIcon', 'Element', 'FeatureGroup', 'Figure', 'FitBounds', 'FitOverlays', 'GeoJson', 'GeoJsonPopup', 'GeoJsonTooltip', 'Html', 'IFrame', 'Icon', 'JavascriptLink', 'JsCode', 'LatLngPopup', 'LayerControl', 'LinearColormap', 'Link', 'MacroElement', 'Map', 'Marker', 'PolyLine', 'Polygon', 'Popup', 'Rectangle', 'RegularPolygonMarker', 'StepColormap', 'TileLayer', 'Tooltip', 'TopoJson', 'Vega', 'VegaLite', 'WmsTileLayer', ...]

Principales clases y funciones de folium:
- Map: Clase principal para crear un mapa interactivo.
- Choropleth: Mapas temáticos coloreados según datos estadísticos.
- Circle: Agrega círculos al mapa.
- CircleMarker: Marcadores circulares.
- ClickForLatLng: Permite obtener lat/lon al hacer clic.
- ClickForMarker: Agrega marcador al hacer clic.
- ColorLine: Dibuja líneas de colores.
- ColorMap: Crea escalas de colores.
- Control: Base para controles de mapa.
- CssLink: Agrega enlaces CSS.
- CustomIcon: Iconos personalizados para marcadores.
- Div: Inserta elementos div.
- DivIcon: Iconos div personalizados.
- Element: Base para elementos HTML.
- FeatureGroup: Agrupa elementos en el mapa.
- Figure: Contenedor de mapas y elementos.
- FitBounds: Ajusta el mapa a ciertos límites.
- FitOverlays: Ajusta a superposiciones.
- GeoJson: Agrega datos GeoJSON.
- GeoJsonPopup: Popups en GeoJSON.
- GeoJsonTooltip: Tooltips en GeoJSON.
- Html: Inserta HTML personalizado.
- IFrame: Marcos en línea para popups.
- Icon: Iconos para marcadores.
- JavascriptLink: Agrega scripts JS externos.
- JsCode: Permite código JS personalizado.
- LatLngPopup: Muestra lat/lon en popup.
- LayerControl: Controla visibilidad de capas.
- LinearColormap: Escala de colores lineal.
- Link: Agrega enlaces HTML.
- MacroElement: Base para elementos avanzados.
- Marker: Agrega marcadores al mapa.
- PolyLine: Dibuja líneas poligonales.
- Polygon: Dibuja polígonos.
- Popup: Ventanas emergentes.
- Rectangle: Dibuja rectángulos.
- RegularPolygonMarker: Marcadores poligonales regulares.
- StepColormap: Escala de colores por pasos.
- TileLayer: Capas de teselas (mapas base).
- Tooltip: Mensajes emergentes al pasar el mouse.
- TopoJson: Agrega datos TopoJSON.
- Vega: Visualizaciones Vega.
- VegaLite: Visualizaciones Vega-Lite.
- WmsTileLayer: Capas WMS.

"""

