import webcolors
from scipy.spatial import KDTree


class Color:
    def __init__(self):
        pass

    def name(self, rgb):
        # a dictionary of all the hex and their respective names in css3
        css3_db = webcolors.HTML4_HEX_TO_NAMES
        names = []
        rgb_values = []
        for color_hex, color_name in css3_db.items():
            names.append(color_name)
            rgb_values.append(webcolors.hex_to_rgb(color_hex))

        kdt_db = KDTree(rgb_values)

        distance, index = kdt_db.query(rgb)
        return f"{names[index]}"
