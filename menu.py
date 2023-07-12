import fitz

from config import Config
from doc import Doc


class Menu:
    def __init__(self):
        self.config = Config()
        self.doc = Doc()

    def run(self):
        run = True
        while run == True:
            self.header()
            print("(S)can the currently loaded document")
            print("(Q)uit")
            i = input("?: ")
            if i == "q" or i == "Q":
                run = False
            elif i == "s" or i == "S":
                doc_meta = self.doc.scan()
                print(doc_meta)

    def header(self):
        print("")
        print("******************************************************")
        print("PDF EXTRACTOR")
        print("")
