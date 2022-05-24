import random, re


def get_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    rgb_lst = [r, g, b]
    random.shuffle(rgb_lst)
    return tuple(rgb_lst)

def get_color_from_stylesheet(code: str):
    w = re.search(r'\(([0-9,\s]+)\)', code)
    r, g, b = map(int, w.group(1).split(','))
    return r, g, b

def get_comp_color(r: int, g: int, b: int):
    r, g, b = r ^ 255, g ^ 255, b ^ 255
    return r, g, b

def rgb_to_hex(r: int, g: int, b: int, digit_cnt: int = 6) -> str:
    six_digit_hex_color = '#%02x%02x%02x' % (r, g, b)
    if digit_cnt == 6:
        return six_digit_hex_color
    else:
        three_digit_hex_color = ''.join([six_digit_hex_color[i] for i in range(0, len(six_digit_hex_color), 2)])
        return three_digit_hex_color

def hex_to_rgb(h: str) -> tuple:
    h = h[1:]
    if len(h) == 3:
        return tuple(int(h[i:i+1]*2, 16) for i in (0, 1, 2))
    else:
        return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def lighter(r: int, g: int, b: int) -> tuple:
    return tuple(map(lambda x: min(255, x+17), (r, g, b)))

def darker(r: int, g: int, b: int) -> tuple:
    return tuple(map(lambda x: max(0, x-17), (r, g, b)))
