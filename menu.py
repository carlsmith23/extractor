import fitz

from config import Config
from doc import Doc


class Menu:
    def __init__(self):
        self.config = Config()
        self.document = fitz.open(self.config.settings["pdf_file"])
        self.doc = Doc(self.config, self.document)

    def run(self):
        run = True
        while run == True:
            self.header()
            print("(S)can the currently loaded document")
            print("(E)xtract Annotations")
            print("(W)rite to file")
            print("(Q)uit")
            i = input("?: ")
            if i == "q" or i == "Q":
                run = False
            elif i == "s" or i == "S":
                doc_meta = self.doc.scan()
                print(doc_meta)
            elif i == "e" or i == "E":
                doc_annotations = self.doc.extract()
                print(doc_annotations)
            elif i == "w" or i == "W":
                # write to file
                print(doc_meta)
            else:
                pass

    def header(self):
        print("")
        print("******************************************************")
        print("PDF EXTRACTOR")
        print("")
