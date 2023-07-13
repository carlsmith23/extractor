import fitz

from config import Config
from doc import Doc


class Menu:
    def __init__(self):
        self.config = Config()
        self.doc = Doc(self.config)

    def run(self):
        run = True
        while run == True:
            self.header()
            print("(S)can the currently loaded document")
            print("(E)xtract Annotations")
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
            else:
                pass

    def header(self):
        print("")
        print("******************************************************")
        print("PDF EXTRACTOR")
        print("")
