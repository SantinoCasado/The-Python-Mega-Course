from kivy.uix.screenmanager import Screen


class SignUpSuccessScreen(Screen):
    def on_kv_post(self, base_widget):
        self.ids.go_login_button.bind(on_press=self.on_go_login_pressed)

    def on_go_login_pressed(self, instance):
        self.manager.current = "login_screen"
