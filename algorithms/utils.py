# relative letter frequencies in the english language
P_ENGLISH = [ 8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015, 6.094, 6.966, 0.153,
        0.772, 4.025, 2.406, 6.749, 7.507, 1.929, 0.095, 5.987, 6.327, 9.056,
        2.758, 0.978, 2.360, 0.150, 1.974, 0.074
        ] # taken from https://gist.github.com/evilpacket/5973230
P_ENGLISH = [x / 100 for x in P_ENGLISH]

def str2ord(s):
    return [ord(x)-ord('a') for x in s if x.islower()] # only take lower letters

def ord2str(s):
    return "".join([chr(x+ord('a')) for x in s])

def index_of_correlation(p, m, k):
    return sum([p[i] * m.count((i + k) % 26) / len(m) for i in range(26)])




