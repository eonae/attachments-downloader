from sys import stdout

def clear():
    stdout.write("\u001b[2J")
    stdout.flush()

def hide_cursor():
    stdout.write('\033[?25l')
    stdout.flush()

def show_cursor():
    stdout.write('\033[?25h')
    stdout.flush()

def move(point):
    x, y = point
    sequence = '\033[' + str(y) + ';' + str(x) + 'H'
    stdout.write(sequence)

def erase_line():
    stdout.write('\33[2K')

def print_at(point, text):
    move(point)
    stdout.write(text)
    stdout.flush()

def relative(point, dx, dy):
    x, y = point
    return (x + dx, y + dy)