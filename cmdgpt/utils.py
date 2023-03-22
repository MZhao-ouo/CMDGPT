import os

def process_file(filename):
    with open(filename, 'rb') as file:
        change = False
        output_data = bytearray()
        while (ch := file.read(1)):
            ch = ord(ch)
            if ch != 0x83:
                if change:
                    d = ch ^ 32
                else:
                    d = ch
                output_data.append(d)
                change = False
            else:
                change = True

        output_str = output_data.decode("utf-8")
        lines = output_str.splitlines(keepends=True)
        return lines

if os.name == 'nt':  # Windows
    import msvcrt

    def get_key():
        if msvcrt.kbhit():
            return msvcrt.getch().decode()
elif os.name == 'posix':  # Linux or macOS
    import sys
    import tty
    import termios

    def get_key():
        fd = sys.stdin.fileno()

        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

        return ch
