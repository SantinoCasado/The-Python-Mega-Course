from pathlib import Path

from kivy.app import App
from kivy.lang import Builder
from kivy.resources import resource_add_path
from db.sqlite_db import get_db_settings_masked, init_database, seed_default_users, test_connection
from screens import HomeScreen, LoginScreen, RecordsScreen, RootWidget, SignUpScreen, SignUpSuccessScreen

BASE_DIR = Path(__file__).resolve().parent

KV_DIR = BASE_DIR / "kv"

resource_add_path(str(BASE_DIR))

Builder.load_file(str(KV_DIR / "login_screen.kv"))
Builder.load_file(str(KV_DIR / "signup_screen.kv"))
Builder.load_file(str(KV_DIR / "signup_success_screen.kv"))
Builder.load_file(str(KV_DIR / "home_screen.kv"))
Builder.load_file(str(KV_DIR / "records_screen.kv"))
Builder.load_file(str(KV_DIR / "root_widget.kv"))

class MainApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.current_user_id = None
        self.current_username = ""

    def on_start(self):
        settings = get_db_settings_masked()
        ok, status = test_connection()
        settings_text = " ".join(f"{key}={value}" for key, value in settings.items())
        if not ok:
            print("Database connection test failed.")
            print(f"Status: {status}")
            print(f"Using {settings_text}")
            return

        print(f"Database connection ok: {settings_text}")

        try:
            init_database()
            seed_default_users()
        except Exception as error:
            print("Database initialization error. Verifica configuración y ruta del archivo SQLite.")
            print(f"Error type: {type(error).__name__}")

    def build(self):
        return RootWidget() # Devuelve una instancia de RootWidget, que es el ScreenManager que manejará las pantallas de la aplicación


if __name__ == '__main__':
    MainApp().run() # Ejecuta la aplicación 