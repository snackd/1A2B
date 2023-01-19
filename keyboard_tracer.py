from pynput import keyboard
from termcolor import cprint

class KeyboardTracer:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.game_flag = 1

    def on_press(self, key):
        try:
            if key == keyboard.Key.esc:
                cprint("Press ESC", "red")
                self.game_flag = 0

        except AttributeError:
            print('special key pressed: {0}'.format(
                key))

    def on_release(self, key):
        if key == keyboard.Key.esc:
            cprint("Release ESC, Stop Listener", "red")
            # Stop listener
            return False

    def main(self):
        # ...or, in a non-blocking fashion:
        listener = keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release)
        listener.start()

if __name__ == "__main__":
    k = KeyboardTracer()
    k.main()