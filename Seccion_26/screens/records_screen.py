from kivy.app import App
from kivy.uix.screenmanager import Screen

from db import list_health_logs


class RecordsScreen(Screen):
    def on_kv_post(self, base_widget):
        self.ids.back_home_button.bind(on_press=self.on_back_home_pressed)

    def on_pre_enter(self, *args):
        self.load_logs()

    def on_back_home_pressed(self, instance):
        self.manager.current = "home_screen"

    def load_logs(self):
        app = App.get_running_app()
        user_id = app.current_user_id
        if not user_id:
            self.ids.records_list_label.text = "Sesión inválida. Inicia sesión nuevamente."
            return

        try:
            logs = list_health_logs(user_id, 40)
        except Exception as error:
            self.ids.records_list_label.text = "No se pudieron cargar los registros."
            print("Database list health logs error.")
            print(f"Error type: {type(error).__name__}")
            return

        if not logs:
            self.ids.records_list_label.text = "No hay registros guardados aún."
            return

        lines = []
        for log in logs:
            weight_text = "-" if log["weight"] is None else f"{log['weight']} kg"
            mood_text = log["mood"] if log["mood"] else "-"
            meals_text = log["meals"] if log["meals"] else "-"
            notes_text = log["notes"] if log["notes"] else "-"
            lines.append(
                f"Fecha: {log['log_date']}\n"
                f"Peso: {weight_text}\n"
                f"Estado: {mood_text}\n"
                f"Comidas: {meals_text}\n"
                f"Notas: {notes_text}\n"
                "---------------------------"
            )

        self.ids.records_list_label.text = "\n".join(lines)
