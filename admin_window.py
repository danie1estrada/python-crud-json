import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from user_controller import UserController
from user_window import UserWindow

class AdminWindow:
    def __init__(self):
        self.selected_user = ''
        self.controller = UserController()

        self.builder = Gtk.Builder()
        self.builder.add_from_file('admin_window.glade')
        self.builder.connect_signals(self)

        self.liststore = self.builder.get_object('liststore_users')
        self.window = self.builder.get_object('window')
        self.window.show()
        self.__build()

    def __build(self):
        for user in self.controller.get_users():
            self.liststore.append([user.username, user.name, user.role])

    def __update(self):
        self.liststore.clear()
        for user in self.controller.get_users():
            self.liststore.append([user.username, user.name, user.role])

    def on_create_user(self, widget):
        UserWindow().run()
        self.__update()

    def on_edit_user(self, widget):
        UserWindow(self.controller.find(self.selected_user)).run()
        self.__update()

    def on_delete_user(self, widget):
        dialog = Gtk.Dialog(
            'Confirmar eliminar usuario',
            self.window,
            flags=1,
            message_type=Gtk.MessageType.WARNING,
            buttons=(Gtk.ButtonsType.OK, Gtk.ButtonsType.CANCEL),
            text='Error de inicio de sesión'
        )

    def on_cursor_changed(self, widget):
        model, tree_iter = widget.get_selection().get_selected()
        self.selected_user = model.get_value(tree_iter, 0)

    def on_destroy(self, *args):
        Gtk.main_quit()
        
    def main(self):
        Gtk.main()



if __name__ == "__main__":
    c = AdminWindow()
    c.main()