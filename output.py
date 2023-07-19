from mdutils.mdutils import MdUtils
from mdutils import Html
import pandas
from datetime import date


class Output:
    def __init__(self, config):
        self.config = config

    def to_file(self, doc_contents):
        title = doc_contents["title"]
        author = doc_contents["author"]
        date_today = str(date.today())
        highlights = doc_contents["highlights"]

        mdFile = MdUtils(file_name="test", title=title)
        mdFile.new_header(level=1, title=title)
        mdFile.new_line(author)

        mdFile.new_line(date_today)
        mdFile.new_header(level=2, title="Highlights")
        mdFile.new_header(level=3, title="Important")
        for i in highlights:
            if i["function"] == "important":
                mdFile.write(i["text"])
                mdFile.write("[@{}]".format(doc_contents["citekey"]))
                mdFile.write("\n\n")

        mdFile.new_header(level=3, title="Definitions")
        for i in highlights:
            if i["function"] == "definition":
                mdFile.write(i["text"])
                mdFile.write("[@{}]".format(doc_contents["citekey"]))
                mdFile.write("\n\n")

        mdFile.new_header(level=3, title="Highlights")
        for i in highlights:
            if i["function"] == "default":
                mdFile.write(i["text"])
                mdFile.write("[@{}]".format(doc_contents["citekey"]))
                mdFile.write("\n\n")

        mdFile.new_header(level=3, title="Methodology")
        for i in highlights:
            if i["function"] == "definition":
                mdFile.write(i["text"])
                mdFile.write("[@{}]".format(doc_contents["citekey"]))
                mdFile.write("\n\n")

        mdFile.new_header(level=3, title="Follow-up")
        for i in highlights:
            if i["function"] == "follow_up":
                mdFile.write(i["text"])
                mdFile.write("[@{}]".format(doc_contents["citekey"]))
                mdFile.write("\n\n")

        mdFile.create_md_file()
