from PIL import ImageGrab

poss = [
    (202, 251),
    (356, 255),
    (519, 249),
    (676, 248),
]

image = ImageGrab.grab(all_screens=True, bbox=(1920, 0, 3840, 300))
ignore_color = image.getpixel(poss[0])

colors = [
    [],
    [],
    [],
    [],
]

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
        (227, 232, 246)],
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


while True:
    image = ImageGrab.grab(all_screens=True, bbox=(1920, 0, 3840, 300))
    if image.getpixel(poss[0]) != ignore_color:
        print(f"pos 1: {image.getpixel(poss[0])}")
        if image.getpixel(poss[0]) not in colors[0]:
            colors[0].append(image.getpixel(poss[0]))
    if image.getpixel(poss[1]) != ignore_color:
        print(f"pos 2: {image.getpixel(poss[1])}")
        if image.getpixel(poss[1]) not in colors[1]:
            colors[1].append(image.getpixel(poss[1]))
    if image.getpixel(poss[2]) != ignore_color:
        print(f"pos 3: {image.getpixel(poss[2])}")
        if image.getpixel(poss[2]) not in colors[2]:
            colors[2].append(image.getpixel(poss[2]))
    if image.getpixel(poss[3]) != ignore_color:
        print(f"pos 4: {image.getpixel(poss[3])}")
        if image.getpixel(poss[3]) not in colors[3]:
            colors[3].append(image.getpixel(poss[3]))
    print(colors)