
FLAG = b'tqlCTF{Gu3sS1nG_gAm3_1S_n0t_crYpt0grAphY}'
KEY = b'admin'

def XOR(text, key):
    ct = bytes([text[i] ^ key[i % len(key)] for i in range(len(text))])
    return ct

def main():
    with open('ciphertext', 'wb') as file:
        file.write(XOR(FLAG, KEY))

if __name__ == "__main__":
    main()
