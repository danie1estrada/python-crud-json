import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from user_controller import UserController
from user import User

class UserWindow:
    def __init__(self, user=None):
        self.is_editing_mode = True if user else False
        self.user = user or User()
        self.controller = UserController()

        self.builder = Gtk.Builder()
        self.builder.add_from_file('user_window.glade')
        self.builder.connect_signals(self)

        self.window = self.builder.get_object('window')
        self.window.set_title('Crear usuario' if not self.is_editing_mode else 'Editar usuario')
        self.__build()

    def __build(self):
        self.builder.get_object('entry_username').set_text(self.user.username)
        self.builder.get_object('entry_name').set_text(self.user.name)
        self.builder.get_object('entry_role').set_text(self.user.role)

    def run(self):
        self.window.show()
        Gtk.main()
        self.window.destroy()
        return self.user

    def on_destroy(self, *args):
        Gtk.main_quit()

    def on_username_changed(self, entry):
        self.user.username = entry.get_text()

    def on_name_changed(self, entry):
        self.user.name = entry.get_text()

    def on_role_changed(self, entry):
        self.user.role = entry.get_text()

    def on_password_changed(self, entry):
        self.user.password = entry.get_text()

    def validate(self):
        user = self.user
        return not user.username and not user.name and not user.role and not user.password
        
    def on_saved(self, button):
        if self.validate():
            return self.show_dialog(
                'Advertencia',
                'Debe llenar todos los campos no sea imbécil',
                Gtk.MessageType.WARNING
            )
        
        self.user.encrypt_password()
        try:
            if self.is_editing_mode:
                self.controller.update(self.user)
            else:
                self.controller.create(self.user)
            Gtk.main_quit()
        except Exception as e:
            self.show_dialog('Ha ocurrido un error', str(e), Gtk.MessageType.ERROR)

    def show_dialog(self, title, message, message_type):
        dialog = Gtk.MessageDialog(
            transient_for=self.window,
            flags=0,
            message_type=message_type,
            buttons=Gtk.ButtonsType.OK,
            text=title,
        )
        dialog.format_secondary_text(message)
        dialog.run()
        dialog.destroy()