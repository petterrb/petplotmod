import colorcet as cc
import numpy as np

COLOR_DICT_PRIMARY = {
    "blue": "#004488",      # dark blue
    "yellow": "#997700",    # dark yellow
    "green": "#117733",     # dark green
    "red": "#994455",       # dark red
    "gray": "#696969",      # dark gray
    "grey": "#696969",      # dark gray
    "black": "#000000",     # black
    "white": "#ffffff",     # white
    "error": "#ff00ff"      # purple (error color)
}

COLOR_DICT_SECONDARY = {
    "blue": "#6699cc",      # light blue
    "yellow": "#eecc66",    # light yellow
    "green": "#66cc88",     # light green
    "red": "#ee99aa",       # light red
    "gray": "#d3d3d3",      # light gray
    "grey": "#d3d3d3",      # dark gray
    "error": "#ff00ff"      # purple (error color)
}

def get_color_primary(col):
    return _get_color(col, COLOR_DICT_PRIMARY)

def get_color_secondary(col):
    return _get_color(col, COLOR_DICT_SECONDARY)

def _get_color(col, color_dict):
    if type(col) == str:
        return color_dict[col] if col in color_dict else color_dict["error"]
    elif type(col) == int:
        keys = ["blue", "red", "yellow", "green"]
        if col < 4:
            return color_dict[keys[col]]
        else:
            return color_dict["error"]

def _hex_to_rgb(hex_str):
    return [int(hex_str[i:i + 2], 16) for i in range(1, 6, 2)]

def _rgb_to_hex(rgb_list):
    return "#" + "".join([format(int(round(val * 255)), "02x") for val in rgb_list])

def interpolate_colors(col1, col2, w):
    if not (0 <= w and w <= 1):
        raise ValueError("w must be between 0 and 1")

    c1_rgb = np.array(_hex_to_rgb(col1)) / 255
    c2_rgb = np.array(_hex_to_rgb(col2)) / 255
    return _rgb_to_hex(c1_rgb * w + c2_rgb * (1 - w))

def get_color_gradient(col1, col2, n):
    """
    Given two hex colors, returns a color gradient
    with n colors.
    """
    if not n > 2:
        raise ValueError("n must be larger than 2 to create a gradient")

    weights = np.linspace(0, 1, n)
    return [interpolate_colors(col1, col2, weight) for weight in weights]

