from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen

from db import authenticate_user


class LoginScreen(Screen):
    # Se llama después de que se haya cargado el archivo KV y se hayan creado los widgets
    def on_kv_post(self, base_widget):
        self.ids.login_button.bind(on_press=self.on_login_pressed)
        self.ids.go_signup_button.bind(on_press=self.on_go_signup_pressed)

    # Se llama cuando se presiona el botón "Login"
    def on_login_pressed(self, instance):
        # Obtiene los valores ingresados por el usuario en los campos de texto
        username = self.ids.username.text.strip()
        password = self.ids.password.text

        # Si el nombre de usuario o la contraseña están vacíos, redirige al usuario a la pantalla de inicio de sesión
        if not username or not password:
            self.show_login_error_popup("Ingresa usuario y contraseña.")
            return

        # Intenta validar las credenciales del usuario utilizando la función validate_user del módulo db
        try:
            user = authenticate_user(username, password)
            if user:
                app = App.get_running_app()
                app.current_user_id = user["id"]
                app.current_username = user["username"]
                self.manager.current = "home_screen"
                return
        except Exception as error:
            print("Database login error.")
            print(f"Error type: {type(error).__name__}")
            self.show_login_error_popup("Ocurrió un error al iniciar sesión.")
            return

        self.show_login_error_popup("Usuario o contraseña incorrectos.")

    # Se llama cuando se presiona el botón "Go to Sign Up"
    def on_go_signup_pressed(self, instance):
        self.manager.current = "signup_screen"

    def show_login_error_popup(self, message):
        content = BoxLayout(orientation="vertical", spacing=12, padding=12)
        content.add_widget(
            Label(
                text=message,
                halign="center",
                valign="middle",
                text_size=(340, None),
            )
        )

        close_button = Button(
            text="Cerrar",
            size_hint_y=None,
            height="44dp",
            background_normal="",
            background_color=(0.85, 0.85, 0.85, 1),
            color=(0.08, 0.08, 0.08, 1),
            bold=True,
        )
        content.add_widget(close_button)

        popup = Popup(
            title="Error de inicio de sesión",
            content=content,
            size_hint=(None, None),
            size=(420, 220),
            auto_dismiss=False,
        )
        close_button.bind(on_press=popup.dismiss)
        popup.open()
