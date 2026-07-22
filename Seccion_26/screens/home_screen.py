from datetime import date

from kivy.app import App
from kivy.uix.screenmanager import Screen

from db import upsert_health_log


class HomeScreen(Screen):
    def on_kv_post(self, base_widget):
        self.ids.save_health_button.bind(on_press=self.on_save_health_pressed)
        self.ids.go_records_button.bind(on_press=self.on_go_records_pressed)
        self.ids.logout_button.bind(on_press=self.on_logout_pressed)

    def on_pre_enter(self, *args):
        today = date.today().isoformat()
        self.ids.date_label.text = f"Fecha: {today}"
        self.clear_form_fields()
        self.ids.status_label.color = (0.82, 0.82, 0.82, 1)
        self.ids.status_label.text = "Completa tu registro de hoy."

    def on_save_health_pressed(self, instance):
        today = date.today().isoformat()
        weight_text = self.ids.weight_input.text.strip()
        meals = self.ids.meals_input.text.strip()
        notes = self.ids.notes_input.text.strip()
        mood = self.ids.mood_spinner.text.strip()

        weight = None
        if weight_text:
            try:
                weight = float(weight_text)
            except ValueError:
                self.ids.status_label.color = (1, 0.25, 0.25, 1)
                self.ids.status_label.text = "El peso debe ser un número válido."
                return

        if mood == "Selecciona":
            mood = ""

        app = App.get_running_app()
        user_id = app.current_user_id
        if not user_id:
            self.ids.status_label.color = (1, 0.25, 0.25, 1)
            self.ids.status_label.text = "Sesión inválida. Vuelve a iniciar sesión."
            self.manager.current = "login_screen"
            return

        try:
            upsert_health_log(user_id, today, weight, meals, notes, mood)
            self.ids.status_label.color = (0.45, 0.85, 0.45, 1)
            self.ids.status_label.text = "Registro guardado correctamente."
            self.clear_form_fields()
        except Exception as error:
            self.ids.status_label.color = (1, 0.25, 0.25, 1)
            self.ids.status_label.text = "No se pudo guardar el registro."
            print("Database save health log error.")
            print(f"Error type: {type(error).__name__}")

    def on_go_records_pressed(self, instance):
        self.manager.current = "records_screen"

    def on_logout_pressed(self, instance):
        app = App.get_running_app()
        app.current_user_id = None
        app.current_username = ""
        self.manager.current = "login_screen"

    def clear_form_fields(self):
        self.ids.weight_input.text = ""
        self.ids.meals_input.text = ""
        self.ids.notes_input.text = ""
        self.ids.mood_spinner.text = "Selecciona"
