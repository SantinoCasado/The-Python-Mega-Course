import sqlite3      # Importa el módulo sqlite3 para manejar bases de datos SQLite

def create_table():
    conn = sqlite3.connect('example.db')                                                                     # Crea una conexión a la base de datos SQLite llamada 'example.db'
    cur = conn.cursor()                                                                                      # Crea un cursor para ejecutar comandos SQL

    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")                # Crea una tabla llamada 'store, ' si no existe

    conn.commit()                                                                                            # Guarda los cambios realizados en la base de datos
    conn.close()                                                                                             # Cierra la conexión a la base de datos

def insert_item(item, quantity, price):
    conn = sqlite3.connect('example.db')                                                                     # Crea una conexión a la base de datos SQLite llamada 'example.db'
    cur = conn.cursor()                                                                                      # Crea un cursor para ejecutar comandos SQL

    cur.execute("INSERT INTO store VALUES (?, ?, ?)", (item, quantity, price))                               # Inserta un registro en la tabla 'store'

    conn.commit()                                                                                            # Guarda los cambios realizados en la base de datos
    conn.close()                                                                                             # Cierra la conexión a la base de datos

def delete_item(index, item):                                                                                # Elimina un artículo de la tabla 'store' basado en el nombre del artículo y index
    conn = sqlite3.connect('example.db')                                                                     # Crea una conexión a la base de datos SQLite llamada 'example.db'
    cur = conn.cursor()                                                                                      # Crea un cursor para ejecutar comandos SQL

    cur.execute("DELETE FROM store WHERE item=? AND rowid=?", (item, index))                                 # Elimina el registro de la tabla 'store' donde el artículo coincide

    conn.commit()                                                                                            # Guarda los cambios realizados en la base de datos
    conn.close()                                                                                             # Cierra la conexión a la base de datos

def update_item(index, item, quantity, price):                                                               # Actualiza un artículo en la tabla 'store' basado en el nombre del artículo y index
    conn = sqlite3.connect('example.db')                                                                     # Crea una conexión a la base de datos SQLite llamada 'example.db'
    cur = conn.cursor()                                                                                      # Crea un cursor para ejecutar comandos SQL

    cur.execute("UPDATE store SET item=?, quantity=?, price=? WHERE rowid=?", (item, quantity, price, index))# Actualiza el registro de la tabla 'store' donde el artículo coincide item

    conn.commit()                                                                                            # Guarda los cambios realizados en la base de datos
    conn.close()                                                                                             # Cierra la conexión a la base de datos

def view():
    conn = sqlite3.connect('example.db')                                                                     # Crea una conexión a la base de datos SQLite llamada 'example.db'
    cur = conn.cursor()                                                                                      # Crea un cursor para ejecutar comandos SQL

    cur.execute("SELECT * FROM store")                                                                       # Selecciona todos los registros de la tabla 'store'
    rows = cur.fetchall()                                                                                    # Obtiene todos los resultados de la consulta

    conn.close()                                                                                             # Cierra la conexión a la base de datos
    return rows                                                                                              # Devuelve los registros obtenidos

create_table()                                                                                               # Llama a la función para crear la tabla si no existe

# insert_item('Apple', 10, 0.5)                                                                              # Llama a la función para insertar un artículo en la tabla
# insert_item('Banana', 20, 0.2)                                                                             # Llama a la función para insertar otro artículo en la tabla
# insert_item('Orange', 15, 0.3)                                                                             # Llama a la función para insertar otro artículo en la tabla

# update_item(2, 'Banana', 25, 0.25)                                                                         # Llama a la función para actualizar el artículo con rowid 2
# delete_item(1, 'Apple')                                                                                    # Llama a la función para eliminar el artículo con rowid 1

print(view())                                                                                                # Llama a la función para ver los registros y los imprime en la consola