import random

P_ENGLISH = [ 8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015, 6.094, 6.966, 0.153,
        0.772, 4.025, 2.406, 6.749, 7.507, 1.929, 0.095, 5.987, 6.327, 9.056,
        2.758, 0.978, 2.360, 0.150, 1.974, 0.074
        ] # taken from https://gist.github.com/evilpacket/5973230
P_ENGLISH = [x / 100 for x in P_ENGLISH]


def ascii_mod_shift(c, k, mod=26):
    if c.islower():
        return chr(ord('a') + (ord(c) + k - ord('a')) % mod)
    elif c.isupper():
        return chr(ord('A') + (ord(c) + k - ord('A')) % mod)
    return c

class ShiftCipher():
    def __init__(self, key=None):
        self.key = key

    def generate(self):
        if self.key is None:
            self.key = random.randint(0, 25)
        return self.key

    def encode(self, message):
        return "".join([ascii_mod_shift(c, self.key) for c in message])

    def decode(self, message):
        return "".join([ascii_mod_shift(c, -self.key) for c in message])

def bruteforce_decode(message):
    for key in range(26):
        cipher = ShiftCipher(key)
        decoded_message = cipher.decode(message)
        print(f"Key {key:02} (Score: {index_of_correlation(P_ENGLISH, message, key):.4f}): {decoded_message}")

def index_of_correlation(p, m, k):
    return sum([p[i] * m.count(ascii_mod_shift(chr(ord('a')+i), k)) / len(m) for i in range(26)])


if __name__ == "__main__":
    print(f"Welcome to this shift cipher program!")
    m = input("Enter a message to encrypt: ")
    k = int(input("Now enter a key for the shifting: [3]") or "3")
    sc = ShiftCipher(k)
    en_message = sc.encode(m)
    print(f"The encoded message is: {en_message}")
    print("To clarify that the algorithm works,")
    print(f"here is the decoded secret: {sc.decode(en_message)}")

