import fitz
import webcolors
from scipy.spatial import KDTree


class Annotation:
    def __init__(self):
        pass

    def process(self, page, annotation):
        (red, green, blue) = annotation.colors["stroke"]
        red = int(red * 255)  # turn into webcolors
        green = int(green * 255)
        blue = int(blue * 255)

        rect = annotation.rect
        all_words = page.get_text("words")
        annot_words = [w for w in all_words if fitz.Rect(w[:4]).intersects(rect)]
        name = self.color_name((red, green, blue))
        entry = {
            "type": annotation.type,
            "color": name,
            "body": self.make_text(annot_words),
        }
        return entry

    def color_name(self, rgb):
        print(rgb)
        # a dictionary of all the hex and their respective names in css3

        # color_db = self.reversedict(self.color_names)
        names = []
        rgb_values = []
        for color_name, color_hex in self.color_names.items():
            names.append(color_name)
            rgb_values.append(webcolors.hex_to_rgb(color_hex))

        kdt_db = KDTree(rgb_values)

        distance, index = kdt_db.query(rgb)
        return f"{names[index]}"

    def reversedict(self, dict_to_reverse):
        """
        Internal helper for generating reverse mappings; given a
        dictionary, returns a new dictionary with keys and values swapped.

        """
        return {value: key for key, value in dict_to_reverse.items()}

    def make_text(self, words):
        line_dict = {}  # key: vertical coordinate, value: list of words
        words.sort(key=lambda w: w[0])  # sort by horizontal coordinate

        for w in words:  # fill the line dictionary
            y1 = round(w[3], 1)  # bottom of a word: don't be too picky!
            word = w[4]  # the text of the word
            line = line_dict.get(y1, [])  # read current line content
            line.append(word)  # append new word
            line_dict[y1] = line  # write back to dict

        lines = list(line_dict.items())
        lines.sort()  # sort vertically
        return "\n".join([" ".join(line[1]) for line in lines])
