from flag import flag
from itertools import cycle

key = "THESUPERSECRETKEY"

def encrypt(value, key):
    message = ''.join(chr(ord(c)^ord(k)) for c,k in zip(value, cycle(key)))
    cipher = ":".join("{:02x}".format(ord(c)) for c in message)
    return cipher

def decrypt(value, key):
    values = value.split(":")
    enValues = []

    for v in values:
        byte_array = bytearray.fromhex(v)
        enValues.append(byte_array.decode())
    
    message = ''.join(chr(ord(c)^ord(k)) for c,k in zip(enValues, cycle(key)))
    return message

if __name__ == "__main__":

    encrypted = encrypt(flag, key)
    decrypted = decrypt(encrypted, key)

    print (encrypted)
    print (decrypted)
