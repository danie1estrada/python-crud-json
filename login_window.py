import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from login_controller import LoginController
from admin_window import AdminWindow
import subprocess

class LoginWindow:
    def __init__(self):
        self.username = ''
        self.password = ''

        self.controller = LoginController()
        
        self.builder = Gtk.Builder()
        self.builder.add_from_file('login_window.glade')

        self.builder.connect_signals(self)

        self.window = self.builder.get_object('window')
        self.window.show()

    def on_username_changed(self, entry):
        self.username = entry.get_text()

    def on_password_changed(self, entry):
        self.password = entry.get_text()

    def on_login_submited(self, button):
        try:
            self.controller.login(self.username, self.password)
            AdminWindow()
            self.window.hide()
        except Exception as e:
            self.show_wrong_credentials_dialog(str(e))

    def show_wrong_credentials_dialog(self, message):
        dialog = Gtk.MessageDialog(
            transient_for=self.window,
            flags=0,
            message_type=Gtk.MessageType.ERROR,
            buttons=Gtk.ButtonsType.OK,
            text='Error de inicio de sesión'
        )
        dialog.format_secondary_text(message)
        dialog.run()
        dialog.destroy()

    def on_destroy(self, *args):
        Gtk.main_quit()
        
    def main(self):
        Gtk.main()

if __name__ == "__main__":
    LoginWindow().main()