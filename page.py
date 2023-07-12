import fitz
from annotation import Annotation


class Page:
    def __init__(self):
        self.annotation = Annotation()

    def scan(self, this_page):
        anno_list = []
        for each_annotation in this_page.annots():
            (red, green, blue) = each_annotation.colors["stroke"]
            anno_color = (int(red * 255), int(green * 255), int(blue * 255))
            anno_color_hex = "".join(f"{i:02x}" for i in anno_color)
            entry = dict(type=each_annotation.type[1], color=anno_color_hex)
            anno_list.append(entry)
        print(anno_list)

    def process(self, this_page):
        for each_annotation in this_page.annots():
            text = this_page.get_text().encode("utf8")  # get plain text (is in UTF-8)
            print(each_annotation.type)
            entry = self.annotation.process(this_page, each_annotation)
            print(entry)
