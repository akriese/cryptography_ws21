from shift_cipher import str2ord, ord2str
from itertools import cycle

class VigenereCipher():
    def __init__(self, key=None):
        self.generate(key)

    def generate(self, key):
        if key is None:
            key = input("Enter a key phrase here (lower case only): ")
        self.key = str2ord(key.lower())

    def encode(self, message):
        return [(c+x)%26 for c, x in zip(message, cycle(self.key))]


    def decode(self, message):
        return [(c-x)%26 for c, x in zip(message, cycle(self.key))]


