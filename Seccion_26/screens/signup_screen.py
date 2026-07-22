from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen

from db import create_user, validate_password_strength


class SignUpScreen(Screen):
    # Se llama después de que se haya cargado el archivo KV y se hayan creado los widgets
    def on_kv_post(self, base_widget): 
        self.ids.go_login_button.bind(on_press=self.on_go_login_pressed)
        self.ids.signup_button.bind(on_press=self.on_signup_pressed)

    # Se llama cuando se presiona el botón "Go to Login"
    def on_go_login_pressed(self, instance):  
        self.manager.current = "login_screen"

    def clear_error_messages(self):
        self.ids.password_error_label.text = ""
        self.ids.confirm_password_error_label.text = ""

    # Se llama cuando se presiona el botón "Sign Up"
    def on_signup_pressed(self, instance):
        # Obtiene los valores ingresados por el usuario en los campos de texto
        username = self.ids.signup_username.text.strip()
        password = self.ids.signup_password.text            
        confirm_password = self.ids.signup_confirm_password.text

        # Limpia los mensajes de error antes de validar los campos
        self.clear_error_messages()

        # Valida que los campos no estén vacíos
        if not username or not password or not confirm_password:
            # Si el campo de contraseña está vacío, muestra un mensaje de error
            if not password:
                self.ids.password_error_label.text = "La contraseña es obligatoria"
            # Si el campo de confirmación de contraseña está vacío, muestra un mensaje de error
            if not confirm_password:
                self.ids.confirm_password_error_label.text = "Repite la contraseña"
            return

        # Valida la fortaleza de la contraseña utilizando la función validate_password_strength del módulo db
        if not validate_password_strength(password):
            self.ids.password_error_label.text = "Debe tener 6-12 caracteres, 1 mayúscula y 1 número"
            return

        # Valida que la contraseña y la confirmación de contraseña coincidan
        if password != confirm_password:
            self.ids.confirm_password_error_label.text = "Las contraseñas no coinciden"
            return

        # Si todas las validaciones son correctas, intenta crear el usuario utilizando la función create_user del módulo db
        try:
            created = create_user(username, password)
            if created:
                self.ids.signup_username.text = ""
                self.ids.signup_password.text = ""
                self.ids.signup_confirm_password.text = ""
                self.manager.current = "signup_success_screen"
                return

            self.show_signup_error_popup("intenta con otra contraseña o nombre de usuario")
        except Exception as error:
            print("Database sign up error.")
            print(f"Error type: {type(error).__name__}")
            self.show_signup_error_popup("intenta con otra contraseña o nombre de usuario")

    def show_signup_error_popup(self, message):
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
            title="Error de registro",
            content=content,
            size_hint=(None, None),
            size=(420, 220),
            auto_dismiss=False,
        )
        close_button.bind(on_press=popup.dismiss)
        popup.open()
