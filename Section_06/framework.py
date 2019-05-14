import tkinter as tk

class Framework():

    menu_items = None

    def __init__(self, root):
        self.root = root

    def build_menu(self, menu_definitions):
        menu_bar = tk.Menu(self.root)
        for definition in menu_definitions:
            menu = tk.Menu(menu_bar, tearoff=0)
            top_level_menu, pull_down_menus = definition.split('-')
            menu_items = map(str.strip, pull_down_menus.split(','))
            for item in menu_items:
                self._add_menu_command(menu, item)
            menu_bar.add_cascade(label=top_level_menu, menu=menu)
        self.root.config(menu=menu_bar)

    def _add_menu_command(self, menu, item):
        if item == 'sep':
            menu.add_separator()
        else:
            menu_label, accelrator_key, command_callback = item.split('/')
            try:
                underline = menu_label.index('&')
                menu_label = menu_label.replace('&', '', 1)
            except ValueError:
                underline = None
            menu.add_command(label=menu_label, underline=underline,
                             accelerator=accelrator_key, command=eval(command_callback))


class TestThisFramework(Framework):

    def new_file(self):
        print('new tested OK')

    def open_file(self):
        print ('open tested OK')

    def undo(self):
        print ('undo tested OK')

    def options(self):
        print ('options tested OK')

    def about(self):
        print ('about tested OK')

if __name__ == '__main__':

    root = tk.Tk()
    menu_items = (
        'File- &New/Ctrl+N/self.new_file, &Open/Ctrl+O/self.open_file',
        'Edit- Undo/Ctrl+Z/self.undo, sep, Options/Ctrl+T/self.options',
        'About- About//self.about'
    )
    app = TestThisFramework(root)
    app.build_menu(menu_items)
    root.mainloop()
