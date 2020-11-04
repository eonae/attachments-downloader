from draw_functions import move, print_at, relative, clear, hide_cursor, show_cursor
from time import sleep

class Label:
    def __init__(self, width, borders=True):
        self.text = ''
        self.width = width
        self.borders = borders
        self.text_width = width - 2 if borders else width
        self.current_position = (1, 1)

    def current_text_position (self):
        x, y = self.current_position
        return (x, y) if not self.borders else (x + 1, y + 1)

    def set_text(self, value):
        self.clear()
        text = str(value)
        stripped_text = text[:self.text_width] if len(text) > self.text_width else text
        print_at(self.current_text_position(), stripped_text.center(self.text_width))


    def draw_at(self, point):
        self.current_position = point
        if self.borders:
            print_at(point, '+' + '-' * self.text_width + '+')
            print_at(relative(point, 0, 1), '|' + ' ' * self.text_width + '|')
            print_at(relative(point, 0, 2), '+' + '-' * self.text_width + '+')
        else:
            pass

    def clear(self):
        print_at(self.current_text_position(), ' ' * self.text_width)

def test():
    hide_cursor()
    clear()
    label1 = Label(4, borders=False)
    label2 = Label(4, borders=False)

    label1.draw_at((1, 1))
    label2.draw_at((1, 2))
    sleep(0.5)
    label1.set_text('OK')
    sleep(0.5)
    label2.set_text('DONE')
    move((1, 6))
    show_cursor()

if __name__ == '__main__':
    test()