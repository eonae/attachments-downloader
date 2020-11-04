from label import Label
from table import Table, Column
from draw_functions import hide_cursor, show_cursor
from time import sleep
import math



class UI:
    def __init__(self):
        self.table = Table([
            Column('Folder', 50),
            Column('Messages', 10),
            Column('Progress', 10),
            Column('Result', 8)
        ], borders=False)
        self.table.draw_at((1, 7))
        self.current = Label(100)
        self.current.draw_at((1, 3))
        self.label = Label(100)
        self.label.draw_at((1, 1))
        self.label.set_text('Downloading:')
        self.folders = []
        hide_cursor()

    def __del__(self):
        show_cursor()

    def add_folder(self, folder):
        self.table.append_row()
        self.folders.append(folder)
        self.set_folder_name(folder)

    def set_folder_name(self, folder):
        row = self.folders.index(folder)
        self.table.set_value(folder, 0, row + 1)

    def set_messages_count(self, folder, count):
        row = self.folders.index(folder)
        self.table.set_value(count, 1, row + 1)

    def set_progress(self, folder, value, of):
        row = self.folders.index(folder)
        percent = math.ceil((value / of) * 100)
        self.table.set_value(f'{percent}%', 2, row + 1)
        
    def set_result(self, folder, value):
        row = self.folders.index(folder)
        self.table.set_value(value, 3, row + 1)

    def update_current(self, value):
        self.current.set_text(value)

# ui = UI()
# sleep(1)
# ui.add_folder('folder-1')
# sleep(1)
# ui.add_folder('folder-2')
# sleep(1)
# ui.set_messages_count('folder-1', 10)
# sleep(1)
# ui.set_progress('folder-1', 5, 100)
# sleep(1)
# ui.set_result('folder-1', 'OK')
# sleep(1)
# ui.set_messages_count('folder-2', 50)
# sleep(1)
# ui.set_progress('folder-2', 100, 100)
# sleep(1)
# ui.set_result('folder-2', 'OK')

# sleep(5)