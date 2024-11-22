import evdev
from time import sleep
from string import ascii_uppercase, ascii_lowercase, digits

KEYMAP = {}
KEYMAP.update({l: (evdev.ecodes.KEY_LEFTSHIFT, eval(f"evdev.ecodes.KEY_{l}")) for l in ascii_uppercase})
KEYMAP.update({l: eval(f"evdev.ecodes.KEY_{l.upper()}") for l in ascii_lowercase})
KEYMAP.update({d: eval(f"evdev.ecodes.KEY_{d}") for d in digits})
KEYMAP.update({
    ".": evdev.ecodes.KEY_DOT,
    ",": evdev.ecodes.KEY_COMMA,
    ";": evdev.ecodes.KEY_SEMICOLON,
    ":": (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_SEMICOLON),
    "/": evdev.ecodes.KEY_SLASH,
    "?": (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_SLASH),
    "\\": evdev.ecodes.KEY_BACKSLASH,
    "'": evdev.ecodes.KEY_APOSTROPHE,
    "\"": (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_APOSTROPHE),
    "-": evdev.ecodes.KEY_MINUS,
    "_": (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_MINUS),
    "=": evdev.ecodes.KEY_EQUAL,
    "+": (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_EQUAL),
    "!": (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_1),
    "@": (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_2),
    "#": (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_3),
    "$": (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_4),
    "%": (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_5),
    "^": (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_6),
    "&": (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_7),
    "*": (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_8),
    "(": (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_9),
    ")": (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_0),
    "~": (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_GRAVE),
    "`": evdev.ecodes.KEY_GRAVE,
    "[": evdev.ecodes.KEY_LEFTBRACE,
    "]": evdev.ecodes.KEY_RIGHTBRACE,
    "{": (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_LEFTBRACE),
    "}": (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_RIGHTBRACE),
    " ": evdev.ecodes.KEY_SPACE,
})

ui = evdev.UInput()


def keywrite(text):
    for char in text:
        key = KEYMAP[char]
        if type(key) is tuple:
            ui.write(evdev.ecodes.EV_KEY, key[0], 1)  # key down
            ui.write(evdev.ecodes.EV_KEY, key[1], 1)  # key down
            ui.write(evdev.ecodes.EV_KEY, key[0], 0)  # key up
            ui.write(evdev.ecodes.EV_KEY, key[1], 0)  # key up
        else:
            ui.write(evdev.ecodes.EV_KEY, key, 1)  # key down
            ui.write(evdev.ecodes.EV_KEY, key, 0)  # key up
        ui.syn()
        sleep(0.01)  # slight delay between keypresses

# Evdev device discovery testing code
# for device in evdev.list_devices():
#     device = evdev.InputDevice(device)
#     if device.name == "keyd virtual keyboard":
#         break
# if type(device) is not evdev.InputDevice:
#     raise Exception("Could not find keyd virtual keyboard")
# # device = evdev.InputDevice('/dev/input/event21')
# print(device)

#
# for event in device.read_loop():
#     if event.type == evdev.ecodes.EV_KEY:
#         print(evdev.categorize(event))

# import evdev
#
# for device in evdev.list_devices():
#     device = evdev.InputDevice(device)
#     print(device)
#     try:
#         for event in device.read_loop():
#             if event.type == evdev.ecodes.KEY_SPACE:
#                 print(evdev.categorize(event))
#     except KeyboardInterrupt:
#         pass

if __name__ == "__main__":
    keywrite("Hello world!")
    ui.close()
