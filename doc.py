import fitz
import json

from page import Page


class Doc:
    def __init__(self, logic):
        self.logic = logic
        self.document = fitz.open(self.logic.config.pdf_file)
        print(self.document.page_count)

    def scan(self):
        doc_contents = []
        for each_page in self.document:
            page = Page()
            page_contents = page.scan(each_page)  # page_contents will be a json object
            # append page_contents to doc_contents

        # return doc_contents and summary

    def process(self):
        for page in document:  # iterate the document pages
            self.pages.process(page)
