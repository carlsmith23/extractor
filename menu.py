import fitz

from config import Config
from doc import Doc


class Menu:
    def __init__(self):
        self.config = Config()
        self.doc = Doc()

    def run(self):
        doc_meta = self.doc.scan()
        print(doc_meta)
