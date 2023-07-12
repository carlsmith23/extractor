import fitz
import json

from config import Config
from page import Page


class Doc:
    def __init__(self):
        self.config = Config()
        self.document = fitz.open(self.config.pdf_file)
        print(self.document.page_count)

    def scan(self):
        doc_contents = dict(
            Highlight=[], Underline=[], StrikeOut=[]
        )  # capitalized because that's what is in the PDF data
        for each_page in self.document:
            page = Page()
            page_contents = page.scan(
                each_page
            )  # returns dictionary listing types of annotations and their colors

            doc_contents["Highlight"].extend(page_contents["Highlight"])
            doc_contents["Underline"].extend(page_contents["Underline"])
            doc_contents["StrikeOut"].extend(page_contents["StrikeOut"])
            # remove duplicates
            doc_contents["Highlight"] = list(set(doc_contents["Highlight"]))
            doc_contents["Underline"] = list(set(doc_contents["Underline"]))
            doc_contents["StrikeOut"] = list(set(doc_contents["StrikeOut"]))

        doc_meta = dict(
            title=self.document.metadata["title"],
            author=self.document.metadata["author"],
            annotations=doc_contents,
        )
        return doc_meta

    def process(self):
        for each_page in document:  # iterate the document pages
            page = Page()
            page_contents = self.page.process(each_page)
