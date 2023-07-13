import fitz
import webcolors
from scipy.spatial import KDTree


class Annotation:
    def __init__(self):
        pass

    def extract(self, this_page, this_annotation):
        (red, green, blue) = this_annotation.colors["stroke"]
        anno_color = (int(red * 255), int(green * 255), int(blue * 255))
        anno_color_hex = "".join(f"{i:02x}" for i in anno_color)

        rectangle = this_annotation.rect
        all_words = this_page.get_text("words")
        annot_words = [w for w in all_words if fitz.Rect(w[:4]).intersects(rectangle)]

        entry = {
            "type": this_annotation.type,
            "color": anno_color_hex,
            "text": self.make_text(annot_words),
        }
        return entry

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

        # add code to clean newlines
