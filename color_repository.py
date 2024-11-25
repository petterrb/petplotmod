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
    _get_color(col, COLOR_DICT_PRIMARY)

def get_color_secondary(col):
    _get_color(col, COLOR_DICT_SECONDARY)

def _get_color(col, color_dict):
    if type(col) == str:
        return color_dict[col] if col in color_dict else color_dict["error"]
    elif type(col) == int:
        keys = ["blue", "red", "yellow", "green"]
        if col < 4:
            return color_dict[keys[col]]
        else:
            return color_dict["error"]