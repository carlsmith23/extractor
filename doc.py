from page import Page

import fitz
import pandas as pd


class Doc:
    def __init__(self, config, document):
        self.config = config
        self.document = document
        self.doc_page_offset = 0
        self.metadata = dict(
            title=self.document.metadata["title"],
            author=self.document.metadata["author"],
            citekey=self.config.settings["citekey"],
        )

    def get_metadata(self):
        self.show_metadata()
        print("Any to accept, (E) to edit)")
        i = input("?: ")

        if i == "E" or i == "e":
            self.show_metadata()
            e = input("Edit what? ")

            if e == "T" or e == "t":
                print(self.metadata["title"])
                t = input("Change to: ")
                self.metadata["title"] = t

            elif e == "A" or e == "a":
                print(self.metadata["author"])
                a = input("Change to: ")
                self.metadata["author"] = a

            elif e == "C" or e == "c":
                print(self.metadata["citekey"])
                c = input("Change to: ")
                self.metadata["citekey"] = c
            else:
                pass

        else:
            pass

    def show_metadata(self):
        print("")
        print("")
        print("Document metadata:")
        print("(T)itle: {}".format(self.metadata["title"]))
        print("(A)uthor: {}".format(self.metadata["author"]))
        print("(C)itekey: {}".format(self.metadata["citekey"]))
        print("")

    def scan(self):
        doc_contents = dict(
            Highlight=[], Underline=[], StrikeOut=[]
        )  # capitalized because that's what is in the PDF data
        for each_page in self.document:
            page = Page(self.config)
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

        doc_scan = dict(
            title=self.metadata["title"],
            author=self.metadata["author"],
            citekey=self.metadata["citekey"],
            annotations=doc_contents,
        )
        return doc_scan

    def extract(self):
        doc_contents = []
        page_number = 1 + self.doc_page_offset
        for each_page in self.document:
            page = Page(self.config)
            page_contents = page.extract(each_page, page_number)
            doc_contents.extend(page_contents)
            page_number += 1

        doc_df = pd.DataFrame(doc_contents)

        # author = [self.document.metadata["author"] for i in range(len(df.index))]
        # title = [self.document.metadata["title"] for i in range(len(df.index))]
        doc_df.insert(0, "citekey", self.metadata["citekey"])
        doc_df.insert(0, "author", self.metadata["author"])
        doc_df.insert(0, "title", self.metadata["title"])
        print(doc_df)
