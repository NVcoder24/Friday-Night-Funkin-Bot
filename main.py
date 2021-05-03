from PIL import ImageGrab
from pynput.keyboard import Key, Controller
from threading import Thread

keyboard = Controller()

ignore_color = (135, 163, 173)

btns = [
    Key.left,
    Key.down,
    Key.up,
    Key.right,
]

poss = [
    (1105, 190),
    (1263, 213),
    (1425, 220),
    (1585, 201),
]

"""colors = [
    [
        (194, 75, 153),
        (154, 140, 169),
        (255, 234, 255),
        (170, 110, 161),
        (250, 242, 248),
        (207, 218, 222),
    ],
    [
        (21, 66, 183),
        (0, 255, 255),
        (55, 255, 255),
        (54, 218, 222),
        (74, 204, 210),
        (67, 105, 179),
    ],
    [
        (18, 250, 5),
        (158, 255, 195),
        (176, 255, 200),
        (10, 68, 71),
        (65, 215, 72),
    ],
    [
        (101, 16, 56),
        (249, 57, 63),
        (203, 99, 107),
        (255, 218, 237),
        (170, 188, 195),
    ]
]"""

output = [
    [
        (255, 254, 255),
        (211, 127, 183),
        (194, 75, 153),
        (60, 31, 86),
        (231, 236, 238),
        (136, 164, 174),
        (156, 179, 187),
        (170, 110, 161),
        (207, 218, 222),
        (253, 253, 254),
        (216, 142, 191),
        (152, 136, 165),
        (214, 135, 187),
        (208, 116, 176),
        (233, 207, 226),
        (167, 124, 165),
        (158, 141, 170),
        (255, 255, 255),
        (182, 92, 157)
    ],
    [
        (255, 255, 255),
        (0, 255, 255),
        (54, 218, 222),
        (21, 66, 183),
        (227, 232, 246)
    ],
    [
        (18, 250, 5),
        (141, 168, 170),
        (65, 215, 72),
        (10, 68, 71),
        (60, 106, 112),
        (56, 223, 60)
    ],
    [
        (249, 57, 63),
        (101, 16, 56),
        (250, 100, 105),
        (106, 39, 73),
        (253, 203, 205),
        (203, 99, 107),
        (102, 18, 58),
        (204, 127, 134),
        (251, 124, 128),
        (255, 255, 255),
        (250, 84, 89),
        (249, 73, 79),
        (249, 60, 66),
        (254, 230, 231),
        (207, 218, 222)
    ]
]

colors = output

def start_cheat_part():
    while True:
        image = ImageGrab.grab(all_screens=True, bbox=(1920, 0, 3840, 300))

        if image.getpixel(poss[0]) in colors[0]:
            keyboard.press(btns[0])
        else:
            keyboard.release(btns[0])
        if image.getpixel(poss[1]) in colors[1]:
            keyboard.press(btns[1])
        else:
            keyboard.release(btns[1])
        if image.getpixel(poss[2]) in colors[2]:
            keyboard.press(btns[2])
        else:
            keyboard.release(btns[2])
        if image.getpixel(poss[3]) in colors[3]:
            keyboard.press(btns[3])
        else:
            keyboard.release(btns[3])


def start():
    Thread(target=start_cheat_part).start()


start()
