from draw_functions import relative, print_at, clear, erase_line, hide_cursor, show_cursor, move
import time

class TextArea:
    def __init__(self, width, height, borders=True):
        self.text = ''
        self.width = width
        self.height = height
        self.borders = borders
        self.text_width = width - 2 if not borders else width
        self.text_height = height - 2 if not borders else height
        self.current_position = (1, 1)

    def text_start_position (self):
        x, y = self.current_position
        return (x, y) if not self.borders else (x + 1, y + 1)

    def set_text(self, text):
        prepared_text = ''
        lines = text.splitlines()
        for line in lines:
            if len(line) <= self.text_width:
                prepared_text += (line + '\n')
            else:
                i = 0
                while i + self.text_width <= len(line):
                    subline = line[i:self.text_width + i]
                    prepared_text += (subline + '\n')
                    i += self.text_width
                prepared_text += (line[i: -1])
        prepared_lines = prepared_text.splitlines()
        if len(prepared_lines) > self.text_height:
            prepared_lines = prepared_lines[:self.text_height]
        point = self.text_start_position()
        for i, line in enumerate(prepared_lines):
            print_at(relative(point, 0, i), line)

    def draw_at(self, point):
        self.current_position = point
        if self.borders:
            print_at(point, '+' + '-' * self.text_width + '+')
            for i in range(self.text_height):
                print_at(relative(point, 0, i + 1), '|' + ' ' * self.text_width + '|')
            print_at(relative(point, 0, self.height + 1), '+' + '-' * self.text_width + '+')
        else:
            pass

    def clear(self):
        line = ' ' * self.text_width
        start = self.text_start_position() 
        for i in range(self.text_height):
            print_at(relative(start, 0, i), line)
