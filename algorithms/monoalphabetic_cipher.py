from utils import str2ord, ord2str
import random

class PermutationCipher():
    def __init__(self):
        self.generate(random.random())

    def generate(self, key):
        alphabet = [chr(x) for x in range(ord('a'), ord('z')+1)]
        shuffle_alphabet = alphabet.copy()
        random.seed(key)
        random.shuffle(shuffle_alphabet)
        self.enc_dict = {c: e for c, e in zip(alphabet, shuffle_alphabet)}
        self.dec_dict = {e: c for c, e in zip(alphabet, shuffle_alphabet)}

    def encode(self, message):
        return [self.enc_dict[c] for c in message]

    def decode(self, message):
        return "".join([self.dec_dict[e] for e in message])
