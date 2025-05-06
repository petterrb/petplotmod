import numpy as np

ERROR_COLOR = "#ff00ff"

COLOR_DICT_PRIMARY = {
    "blue": "#004488",      # dark blue
    "yellow": "#997700",    # dark yellow
    "green": "#117733",     # dark green
    "red": "#994455",       # dark red
    "gray": "#696969",      # dark gray
    "black": "#000000",     # black
    "white": "#ffffff",     # white
}

COLOR_DICT_SECONDARY = {
    "blue": "#6699cc",      # light blue
    "yellow": "#eecc66",    # light yellow
    "green": "#66cc88",     # light green
    "red": "#ee99aa",       # light red
    "gray": "#d3d3d3",      # light gray
}

COLOR_DICT_MUTED = {
    "pink": "#cc6677",
    "darkblue": "#332288",
    "beige": "#ddcc77",
    "green": "#117733",
    "lightblue": "#88ccee",
    "burgundy": "#882255",
    "cyan": "#44aa99",
    "darkyellow": "#999933",
    "purple": "#aa4499",
    "gray": "#aaaaaa"
}

def get_color_primary(col):
    return _get_color(col, COLOR_DICT_PRIMARY)

def get_color_secondary(col):
    return _get_color(col, COLOR_DICT_SECONDARY)

def get_color_muted(col):
    return _get_color(col, COLOR_DICT_MUTED)

def _get_color(col, color_dict):
    if type(col) == str:
        col = col.lower()
        if col == "grey":
            col = "gray"
        return color_dict[col] if col in color_dict else ERROR_COLOR

    elif type(col) == int:
        keys = list(color_dict.keys())
        if col < len(color_dict):
            return color_dict[keys[col]]
        elif len(color_dict) > 0:
            return color_dict[keys[col % len(color_dict)]]
        else:
            return ERROR_COLOR

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
