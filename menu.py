import fitz

from config import Config
from doc import Doc
from output import Output


class Menu:
    def __init__(self):
        self.config = Config()
        self.document = fitz.open(self.config.settings["pdf_file"])
        self.doc = Doc(self.config, self.document)
        self.output = Output(self.config)

    def run(self):
        run = True
        while run == True:
            self.header()
            print("(G)et metadata")
            print("(S)can the currently loaded document")
            print("(E)xtract Annotations")
            print("(W)rite to file")
            print("(Q)uit")
            i = input("?: ")
            if i == "q" or i == "Q":
                run = False
            elif i == "g" or i == "G":
                self.doc.get_metadata()
            elif i == "s" or i == "S":
                doc_scan = self.doc.scan()
                print(doc_scan)
            elif i == "e" or i == "E":
                doc_contents = self.doc.extract()
            elif i == "w" or i == "W":
                self.output.to_file(doc_contents)
            else:
                pass

    def header(self):
        print("")
        print("")
        print("")
        print("")
        print("******************************************************")
        print("PDF EXTRACTOR")
        print("")
