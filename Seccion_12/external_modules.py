
"""
Third-party libraries can be installed from the terminal/command line:

Windows:
    pip install pandas or use python -m pip install pandas if that doesn't work.

Mac and Linux:
    pip3 install pandas or use python3 -m pip install pandas if that doesn't work.
"""
import pandas

# Pandas module
while True:
    if os.path.exists("Files/temps_today.csv"):
        data = pandas.read_csv("Files/temps_today.csv")  # Lee un archivo CSV
        print(data.mean())    # Muestra el contenido del archivo, en este caso la temperatura media
        print(data["st1"].max())  # Muestra la temperatura máxima de la columna 'st1'
        print(data["st1"].min())  # Muestra la temperatura mínima de la columna 'st1'
        print(data["st1"].std())  # Muestra la desviación estándar de la columna 'st1'
        print(data["st1"].count())    # Muestra el conteo de valores en la columna 'st1'
        print(data["st1"].sum())  # Muestra la suma de los valores en la columna 'st1'
        print(data["st1"].describe()) # Muestra un resumen estadístico de la columna 'st1'
        print("Temperature data processed successfully.")
        break
    else:
        print("The file does not exist.")
    time.sleep(10)  # Check every 10 seconds
# Si modificamos el contenido dentro de temps_today.csv en los 10 segundos, se reflejará aquí

#-------------------------------------------------------------------------------------------------------------------
# More pandas fuctions
# Crear un DataFrame desde un diccionario
data_dict = {
    "mean": data["st1"].mean(),
    "max": data["st1"].max(),
    "min": data["st1"].min(),
    "std": data["st1"].std(),
    "count": data["st1"].count(),
    "sum": data["st1"].sum(),
    "describe": data["st1"].describe()
}
data_df = pandas.DataFrame(data_dict, index=[0])
data_df.to_csv("Files/temps_summary.csv", index=False)  # Guarda el resumen estadístico en un nuevo archivo CSV
print("Summary statistics saved to temps_summary.csv")
#-------------------------------------------------------------------------------------------------------------------    
# Pandas with Excel files
# Asegúrate de tener openpyxl instalado: pip install openpyxl
excel_data = pandas.read_excel("Files/temps_today.xlsx", engine='openpyxl')  # Lee un archivo Excel
print(excel_data.head())  # Muestra las primeras filas del DataFrame
print(excel_data.describe())  # Muestra un resumen estadístico
excel_data.to_excel("Files/temps_today_copy.xlsx", index=False, engine='openpyxl')  # Guarda una copia del archivo Excel
print("Excel file copied to temps_today_copy.xlsx")

