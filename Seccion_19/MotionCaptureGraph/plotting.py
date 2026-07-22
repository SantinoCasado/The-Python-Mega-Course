import pandas as pd
import subprocess
import sys
import os
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource

# Ejecutar captureAll.py para obtener nuevos datos de movimiento
print("Ejecutando captura de movimiento...")
try:
    # Asegurar que estemos en el directorio correcto
    captureAll_path = os.path.join(os.path.dirname(__file__), "captureAll.py")
    result = subprocess.run([sys.executable, captureAll_path], 
                          capture_output=True, text=True, timeout=300, cwd=os.path.dirname(__file__))
    if result.returncode == 0:
        print("Captura completada exitosamente")
    else:
        print(f"Error en captura: {result.stderr}")
except subprocess.TimeoutExpired:
    print("Captura de movimiento tomó demasiado tiempo, usando datos existentes")
except Exception as e:
    print(f"Error ejecutando captura: {e}")

# Cargar datos desde el archivo CSV actualizado
try:
    df = pd.read_csv("Times.csv")
    df['Start'] = pd.to_datetime(df['Start'])
    df['End'] = pd.to_datetime(df['End'])
    
    # Crear columnas formateadas para el hover
    df['Start_formatted'] = df['Start'].dt.strftime('%Y-%m-%d %H:%M:%S')
    df['End_formatted'] = df['End'].dt.strftime('%Y-%m-%d %H:%M:%S')
    
    print(f"Datos cargados: {len(df)} intervalos de movimiento detectados")
except FileNotFoundError:
    print("Archivo Times.csv no encontrado después de la captura")
    exit()


p = figure(title="Motion Capture Graph", x_axis_type='datetime', height=500, sizing_mode='stretch_width')
p.yaxis.minor_tick_line_color = None

# Configurar la grilla Y de forma más segura
if hasattr(p, 'ygrid') and len(p.ygrid) > 0 and hasattr(p.ygrid[0], 'ticker') and p.ygrid[0].ticker is not None:
    p.ygrid[0].ticker.desired_num_ticks = 1

# Crear ColumnDataSource para tener mejor control sobre los datos
source = ColumnDataSource(data=dict(
    start=df["Start"],
    end=df["End"],
    start_formatted=df["Start_formatted"],
    end_formatted=df["End_formatted"],
    bottom=[0] * len(df),
    top=[1] * len(df)
))

hover = HoverTool(tooltips=[
    ("Inicio", "@start_formatted"), 
    ("Fin", "@end_formatted"),
    ("Duración", "@start_formatted - @end_formatted")
])
p.add_tools(hover)

q = p.quad(left='start', right='end', bottom='bottom', top='top', color="green", source=source)

output_file("../Seccion_19/MotionCaptureGraph/motion_capture.html")
show(p)