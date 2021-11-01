import random
from utils import str2ord, ord2str, P_ENGLISH, index_of_correlation


class ShiftCipher():
    def __init__(self, key=None):
        self.generate(key)

    def generate(self, key):
        self.key = key or random.randint(0, 25)

    def encode(self, message):
        return [(c + self.key) % 26 for c in message]

    def decode(self, message):
        return [(c - self.key) % 26 for c in message]


def bruteforce_decode(message):
    ord_m = str2ord(message)
    for key in range(26):
        cipher = ShiftCipher(key)
        decoded_message = cipher.decode(ord_m)
        print(f"Key {key:02} (Score: {index_of_correlation(P_ENGLISH, ord_m, key):.4f}): {ord2str(decoded_message)}")


if __name__ == "__main__":
    print(f"Welcome to this shift cipher program!")
    m = input("Enter a message to encrypt: ")
    k = int(input("Now enter a key for the shifting: [3]") or "3")
    sc = ShiftCipher(k)
    en_message = sc.encode(str2ord(m))
    print(f"The encoded message is: {ord2str(en_message).upper()}")
    print("To clarify that the algorithm works,")
    print(f"here is the decoded secret: {ord2str(sc.decode(en_message))}")

