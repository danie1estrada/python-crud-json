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
        user = self.controller.find(self.selected_user)
        UserWindow(user).run()
        self.__update()

    def on_delete_user(self, widget):
        dialog = Gtk.MessageDialog(
            transient_for=self.window,
            flags=0,
            message_type=Gtk.MessageType.WARNING,
            buttons=Gtk.ButtonsType.YES_NO,
            text='¿Desea eliminar este usuario?'
        )
        result = dialog.run()
        dialog.destroy()
        if result == -8:
            user = self.controller.find(self.selected_user)
            self.controller.delete(user)
            self.__update()

    def on_cursor_changed(self, widget):
        if self.selected_user == '':
            self.builder.get_object('button_edit_user').set_sensitive(True)
            self.builder.get_object('button_delete_user').set_sensitive(True)

        try:
            model, tree_iter = widget.get_selection().get_selected()
            self.selected_user = model.get_value(tree_iter, 0)
        except:
            self.selected_user = ''
            self.builder.get_object('button_edit_user').set_sensitive(False)
            self.builder.get_object('button_delete_user').set_sensitive(False)

    def on_destroy(self, *args):
        Gtk.main_quit()
        
    def main(self):
        Gtk.main()


if __name__ == "__main__":
    c = AdminWindow()
    c.main()