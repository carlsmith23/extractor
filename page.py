import fitz

from annotation import Annotation


class Page:
    def __init__(self, config):
        self.config = config
        self.annotation = Annotation()

    def scan(self, this_page):
        page_contents = dict(
            Highlight=[], Underline=[], StrikeOut=[]
        )  # capitalized because that's what is in the PDF data
        for each_annotation in this_page.annots():
            (red, green, blue) = each_annotation.colors["stroke"]
            anno_color = (int(red * 255), int(green * 255), int(blue * 255))
            anno_color_hex = "".join(f"{i:02x}" for i in anno_color)
            page_contents[each_annotation.type[1]].append(anno_color_hex)
        return page_contents

    def extract(self, this_page):
        page_contents = dict(Highlight=[], Underline=[], StrikeOut=[])
        for each_annotation in this_page.annots():
            # if each_annotation.type == "Highlight" & self.doc.
            text = this_page.get_text().encode("utf8")  # get plain text (is in UTF-8)

            annotation_contents = self.annotation.extract(this_page, each_annotation)
            if (
                annotation_contents["type"] == "Highlight"
                and self.config.settings["highlight_enable"]
            ):
                page_contents["Highlight"].append(
                    [annotation_contents["color"], annotation_contents["text"]]
                )
            elif (
                annotation_contents["type"] == "Underline"
                and self.config.settings["underline_enable"]
            ):
                page_contents["Underline"].append(
                    [annotation_contents["color"], annotation_contents["text"]]
                )
            elif (
                annotation_contents["type"] == "StrikeOut"
                and self.config.settings["strikeout_enable"]
            ):
                page_contents["StrikeOut"].append(
                    [annotation_contents["color"], annotation_contents["text"]]
                )
        return page_contents
