keys="abcdefghijklmnopqrstuvwxyz"

def alphabet_position(char):
        return keys.index(char)


def rotate_character(char,rot):
    if char.isalpha():
        n= keys[(alphabet_position(char.lower()) + rot)% 26]
        return n.upper() if char.isupper() else n.lower()
    else:
        return char


def encrypt(text,rot):
    encrypted=""
    for s in text:
        if not s.isalpha():
            encrypted= encrypted + s
        else:
            encrypted= encrypted + rotate_character(s,rot)

    return encrypted
