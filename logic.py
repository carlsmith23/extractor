import fitz

from config import Config
from doc import Doc


class Logic:
    def __init__(self):
        self.config = Config()
        self.doc = Doc(self)

    def run(self):
        Doc(self).scan()
