from PIL import ImageGrab
from threading import Thread

ignore_color = (135, 163, 173)

poss = [
    (1105, 190),
    (1263, 213),
    (1425, 220),
    (1585, 201),
]

colors = [
    [
        (194, 75, 153),
        (154, 140, 169),
    ],
    [
        (21, 66, 183),
        (0, 255, 255),
    ],
    [
        (18, 250, 5),
    ],
    [
        (101, 16, 56),
        (249, 57, 63),
        (170, 188, 195),
    ]
]

def start_cheat_part():
    while True:
        image = ImageGrab.grab(all_screens=True, bbox=(1920, 0, 3840, 300))
        if image.getpixel(poss[0]) != ignore_color:
            print(f"pos 1: {image.getpixel(poss[0])}")
        if image.getpixel(poss[1]) != ignore_color:
            print(f"pos 2: {image.getpixel(poss[1])}")
        if image.getpixel(poss[2]) != ignore_color:
            print(f"pos 3: {image.getpixel(poss[2])}")
        if image.getpixel(poss[3]) != ignore_color:
            print(f"pos 4: {image.getpixel(poss[3])}")


def start():
    Thread(target=start_cheat_part).start()

start()
