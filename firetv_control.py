import subprocess
from enum import Enum
import sys


class Keycode(Enum):
    KEYCODE_MEDIA_PLAY_PAUSE = 0
    KEYCODE_BACK = 1
    KEYCODE_DPAD_CENTER = 2
    KEYCODE_DPAD_UP = 3
    KEYCODE_DPAD_RIGHT = 4
    KEYCODE_DPAD_LEFT = 5
    KEYCODE_DPAD_DOWN = 6


arguments = {
    "center" : Keycode.KEYCODE_DPAD_CENTER,
    "back" : Keycode.KEYCODE_BACK,
    "play" : Keycode.KEYCODE_MEDIA_PLAY_PAUSE,
    "pause": Keycode.KEYCODE_MEDIA_PLAY_PAUSE,
    "up": Keycode.KEYCODE_DPAD_UP,
    "down": Keycode.KEYCODE_DPAD_DOWN,
    "right": Keycode.KEYCODE_DPAD_RIGHT,
    "left": Keycode.KEYCODE_DPAD_LEFT
}


class FireTVController:

    address = "192.168.2.104:5555"
    adb_path = "/Users/steffengundermann/Library/Android/sdk/platform-tools/adb"
    #adb_path = "adb"
    _connected = False

    commands = []

    def __init__(self, commands=[]):
        for c in commands:
            if c.lower() in arguments.keys():
                self.commands.append(arguments[c.lower()])
            if c.lower() == "disconnect":
                self.commands.append(c.lower())

    def connect(self):
        subprocess.run([self.adb_path, "connect", self.address])
        print("Connected!")
        self._connected = True

    def keycode(self, keycode):
        if self._connected:
            subprocess.run([self.adb_path, "shell", "input", "keyevent", str(keycode.name)])
        else:
            print("Not connected!")

    def handle_commands(self):
        self.connect()
        for c in self.commands:
            if c == "disconnect":
                self.disconnect()
                return
            self.keycode(c)

    def disconnect(self):
        subprocess.run([self.adb_path, "disconnect"])
        print("Disconnected!")


if __name__ == '__main__':
    sys.argv.pop(0)
    fireTvController = FireTVController(sys.argv)
    fireTvController.handle_commands()
