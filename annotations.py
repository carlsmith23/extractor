class Annotations:
    __init__(self):


    def process(self, page, annot):
        (red, green, blue) = annot.colors["stroke"]
        red = int(red * 255)
        green = int(green * 255)
        blue = int(blue * 255)

        rect = annot.rect
        all_words = page.get_text("words")
        annot_words = [w for w in all_words if fitz.Rect(w[:4]).intersects(rect)]

        entry = {"type": annot.type, 
            "color": [red, green, blue],
            "body": self.make_text(annot_words)}
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


    





