import fitz

def make_text(words):
    """Return textstring output of get_text("words").
    Word items are sorted for reading sequence left to right,
    top to bottom.
    """
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


doc = fitz.open("test.pdf")

print(doc.page_count)

for page in doc:  # iterate the document pages
    #text = page.get_text().encode("utf8")  # get plain text (is in UTF-8)
    #print(text)

# list to store the co-ordinates of all highlights
    highlights = []
# loop till we have highlight annotation in the page
    annot = page.first_annot
    print(annot.type)
    color = annot.colors

    (red, green, blue) = color["stroke"]
    red = int(red * 255)
    green = int(green * 255)
    blue = int(blue * 255)
    print("{}, {}, {}" .format(red, green, blue))

    coord = annot.vertices
    print(coord)
    
    rect = annot.rect  # this annot has been prepared for us!
# Now we have the rectangle ---------------------------------------------------

    all_words = page.get_text("words")
    annot_words = [w for w in all_words if fitz.Rect(w[:4]).intersects(rect)]
    print(make_text(annot_words))

    {"type": annot.type, 
     "color": annot.colors,
     "body": make_text(annot_words)}