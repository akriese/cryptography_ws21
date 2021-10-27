import random

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
        return "".join([ascii_mod_shift(c, self.key, 26) for c in message])

    def decode(self, message):
        return "".join([ascii_mod_shift(c, -self.key, 26) for c in message])



if __name__ == "__main__":
    print(f"Welcome to this shift cipher program!")
    m = input("Enter a message to encrypt: ")
    k = int(input("Now enter a key for the shifting: [3]") or "3")
    sc = ShiftCipher(k)
    en_message = sc.encode(m)
    print(f"The encoded message is: {en_message}")
    print("To clarify that the algorithm works,")
    print(f"here is the decoded secret: {sc.decode(en_message)}")

