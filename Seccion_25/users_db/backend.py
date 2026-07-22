import sqlite3
import os
import sys

class Database:
    # __init__ = Constructor para establecer la conexión a la base de datos y crear la tabla de usuarios automaticamente cuando se instancia la clase.
    def __init__(self, db_name):    # self = puede asumir cualquier nombre, pero por convención se usa self para referirse a la instancia actual de la clase. 
        self.connection = sqlite3.connect(self.get_db_path(db_name))
        self.cursor = self.connection.cursor()
        self.create_users_table()
    
    def get_db_path(self):
        if hasattr(sys, '_MEIPASS'):
            # Cuando está ejecutándose desde PyInstaller
            return os.path.join(os.path.dirname(sys.executable), "users.db")
        else:
            # Cuando se ejecuta normalmente
            return os.path.join(os.path.dirname(__file__), "users.db")
    
    # CRUD Operations
    def create_user(self, name, email):
        self.connection = sqlite3.connect(self.get_db_path())
        self.cursor = self.connection.cursor()
        self.cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        self.connection.commit()
        self.connection.close()
    
    def read_users(self):
        self.connection = sqlite3.connect(self.get_db_path())
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM users")
        users = self.cursor.fetchall()
        self.connection.close()
        return users

    def update_user(self, user_id, name, email):
        self.connection = sqlite3.connect(self.get_db_path())
        self.cursor = self.connection.cursor()
        self.cursor.execute("UPDATE users SET name = ?, email = ? WHERE id = ?", (name, email, user_id))
        self.connection.commit()
        self.connection.close()
    
    def delete_user(self, user_id):
        self.connection = sqlite3.connect(self.get_db_path())
        self.cursor = self.connection.cursor()
        self.cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        self.connection.commit()
        self.connection.close()
    
    def create_users_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT NOT NULL,
                                email TEXT NOT NULL UNIQUE)''')
        self.connection.commit()
        self.connection.close()
    
    # __del__ = Destructor para cerrar la conexión a la base de datos cuando la instancia de la clase se destruye.
    def __del__(self):
        if self.connection:
            self.connection.close()


# Ejemplo de uso
# if __name__ == "__main__": es una construcción común en Python que se utiliza para ejecutar código solo cuando el script se ejecuta directamente, y no cuando se importa como un módulo en otro script. Esto permite que el código de prueba o de ejemplo se ejecute solo en el contexto adecuado.

"""
if __name__ == "__main__":
    db = Database('users.db')
    db.create_user('Alice', 'alice@example.com')
    db.create_user('Bob', 'bob@example.com')
    print(db.read_users())
    db.update_user(1, 'Alice Smith', 'alice.smith@example.com')
    print(db.read_users())
    db.delete_user(2)
    print(db.read_users())
"""