from label import Label
from draw_functions import relative
import time

class Column:
    def __init__(self, name, width):
        self.name = name
        self.width = width
    
class Table:
    def __init__(self, columns, borders=True, rows_count=0):
        self.columns = columns
        self.borders = borders
        self.row_height = 2 if borders else 1
        self.current_position = (1, 1)
        self.cells = []
        for i in range(rows_count + 1):
            self.cells.append([Label(col.width, self.borders) for col in columns])

    def draw_row(self, y, row, point=(1, 1)):
        x = 0
        for i, label in enumerate(row):
            label.draw_at(relative(point, x, y))
            x += self.columns[i].width + 1

    def draw_at(self, point):
        self.current_position = point
        for row_number, row in enumerate(self.cells):
            self.draw_row(row_number * self.row_height + 1, row, point)
        for i, column in enumerate(self.columns):
            self.cells[0][i].set_text(column.name)

    def append_row(self):
        row = [Label(col.width, self.borders) for col in self.columns]
        self.cells.append(row)
        self.draw_row((len(self.cells) - 1) * self.row_height + 1, row, self.current_position)

    def set_value(self, value, col, row):
        self.cells[row][col].set_text(value)


if __name__ == '__main__':
    table = Table([
        Column('id', 4),
        Column('name', 4)
    ], rows_count=4, borders=False)

    table.draw_at((1, 2))
    table.cells[1][1].set_text('hi')
