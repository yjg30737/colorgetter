import random, re


class PythonColorGetter:
    @staticmethod
    def get_random_color():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        rgb_lst = [r, g, b]
        random.shuffle(rgb_lst)
        return tuple(rgb_lst)

    @staticmethod
    def get_color_from_stylesheet(code: str):
        w = re.search(r'\(([0-9,\s]+)\)', code)
        r, g, b = map(int, w.group(1).split(','))
        return r, g, b

    @staticmethod
    def get_complementary_color(r: int, g: int, b: int):
        r, g, b = r ^ 255, g ^ 255, b ^ 255
        return r, g, b

    @staticmethod
    def rgb_to_hex(r: int, g: int, b: int) -> str:
        return '#%02x%02x%02x' % (r, g, b)

    @staticmethod
    def hex_to_rgb(rgb: str) -> tuple:
        rgb = rgb[1:]
        return tuple(int(rgb[i:i+2], 16) for i in (0, 2, 4))
