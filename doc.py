from page import Page
import fitz


class Doc:
    def __init__(self, config, document):
        self.config = config
        self.document = document

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

        doc_meta = dict(
            title=self.document.metadata["title"],
            author=self.document.metadata["author"],
            annotations=doc_contents,
        )
        return doc_meta

    def extract(self):
        doc_contents = dict(
            Title=self.document.metadata["title"],
            Author=self.document.metadata["author"],
            Citekey="",
            Highlight=[],
            Underline=[],
            StrikeOut=[],
        )
        for each_page in self.document:
            page = Page(self.config)
            page_contents = page.extract(each_page)
            doc_contents["Highlight"].extend(page_contents["Highlight"])
            doc_contents["Underline"].extend(page_contents["Underline"])
            doc_contents["StrikeOut"].extend(page_contents["StrikeOut"])
        print(doc_contents)
