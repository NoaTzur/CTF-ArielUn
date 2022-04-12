import string
import base64

"""
def encryption(msg):
    ct = []
    for char in msg:
        ct.append((123 * char + 18) % 256)
    return bytes(ct)
"""


# 179 is the inverse of 123 mod 256
def decription(msg):
    de = []
    for char in msg:
        char = char - 18
        char = (char * 179) % 256
        de.append(char)
    print(bytes(de))


if __name__ == '__main__':
    with open("msg.enc") as f:
        b = bytes.fromhex(f.read())
        decription(b)
