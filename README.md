# python-color-getter
Python color getter (including method to get random color or complementary color)

## Setup
`python -m pip install python-color-getter`

## Method Overview
* ```get_random_color() -> tuple```
* ```get_color_from_stylesheet(code: str) -> None```
* ```get_complementary_color(r: int, g: int, b: int) -> tuple```
* ```rgb_to_hex(r: int, g: int, b: int, digit_cnt: int = 6) -> str``` - Argument ```digit_cnt``` is digit count of hex color user want to get.  The value of ```digit_cnt``` should be 3 or 6. It is set to 6 by default.
* ```hex_to_rgb(hex: str) -> tuple``` - Argument ```hex``` should be 3 or 6 digit hex colors like #DDD, #ABABAB.
* ```lighter(r: int, g: int, b: int) -> tuple```
* ```darker(r: int, g: int, b: int) -> tuple```

## Example
Code Sample
```python
print(PythonColorGetter.get_random_color())
print(PythonColorGetter.get_complementary_color(255, 0, 0))
print(PythonColorGetter.hex_to_rgb('#2c2c2c'))
r, g, b = 44, 44, 44
print(PythonColorGetter.rgb_to_hex(r, g, b))
light_r, light_g, light_b = PythonColorGetter.lighter(r, g, b)
print(PythonColorGetter.rgb_to_hex(light_r, light_g, light_b))
dark_r, dark_g, dark_b = PythonColorGetter.darker(r, g, b)
print(PythonColorGetter.rgb_to_hex(dark_r, dark_g, dark_b))
```

Result
```
(211, 195, 123)
(0, 255, 255)
(44, 44, 44)
#2c2c2c
#3d3d3d
#1b1b1b
```
