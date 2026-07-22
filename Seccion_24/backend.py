import sqlite3
import os
import sys

def get_db_path():
    if hasattr(sys, '_MEIPASS'):
        # Cuando está ejecutándose desde PyInstaller
        return os.path.join(os.path.dirname(sys.executable), "books.db")
    else:
        # Cuando está ejecutándose desde código fuente
        return os.path.join(os.path.dirname(__file__), "books.db")

def connect():
    conn = sqlite3.connect(get_db_path())
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)"
    )
    conn.commit()
    conn.close()

def insert(title, author, year, isbn):
    conn = sqlite3.connect(get_db_path())
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO book VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn)
    )
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect(get_db_path())
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    
    # Formatear los resultados
    formatted_rows = []
    for row in rows:
        formatted_row = f"{row[1]} - {row[2]} ({row[3]}) ISBN: {row[4]}"
        formatted_rows.append(formatted_row)
    
    return formatted_rows

def view_raw():
    """Devuelve los datos sin formatear para operaciones de update/delete"""
    conn = sqlite3.connect(get_db_path())
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows

def search_raw(title="", author="", year="", isbn=""):
    """Devuelve los resultados de búsqueda sin formatear para operaciones de update/delete"""
    conn = sqlite3.connect(get_db_path())
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",
        (title, author, year, isbn),
    )
    rows = cur.fetchall()
    conn.close()
    return rows

def search(title="", author="", year="", isbn=""):
    conn = sqlite3.connect(get_db_path())
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",
        (title, author, year, isbn),
    )
    rows = cur.fetchall()
    conn.close()
    
    # Formatear los resultados
    formatted_rows = []
    for row in rows:
        formatted_row = f"{row[1]} - {row[2]} ({row[3]}) ISBN: {row[4]}"
        formatted_rows.append(formatted_row)
    
    return formatted_rows

def delete(id):
    conn = sqlite3.connect(get_db_path())
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?", (id,))
    conn.commit()
    conn.close()

def update(id, title, author, year, isbn):
    conn = sqlite3.connect(get_db_path())
    cur = conn.cursor()
    cur.execute(
        "UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",
        (title, author, year, isbn, id),
    )
    conn.commit()
    conn.close()

# Comentadas las líneas de inicialización para evitar conflictos
#connect()
#insert("The Great Gatsby", "F. Scott Fitzgerald", 1925, 9780743273565)
#insert("To Kill a Mockingbird", "Harper Lee", 1960, 9780061120084)