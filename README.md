# python-color-getter
Color getter (including method to get random color or complementary color) made out of Python

## Setup
```pip3 install git+https://github.com/yjg30737/python-color-getter.git --upgrade```

## Method Overview
* ```get_random_color() -> tuple```
* ```get_color_from_stylesheet(code: str) -> None```
* ```get_complementary_color(r: int, g: int, b: int) -> tuple```
* ```rgb_to_hex(r: int, g: int, b: int) -> str```
* ```hex_to_rgb(hex: str) -> tuple``` - only 3-digit or 6-digit hex colors enabled.
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
