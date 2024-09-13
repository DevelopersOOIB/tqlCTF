
FLAG = b'tqlCTF{'

def XOR(text, key):
    ct = bytes([text[i] ^ key[i % len(key)] for i in range(len(text))])
    return ct

def main():
    with open('ciphertext', 'rb') as file:
        ct = file.read()
    key = XOR(ct[: len(FLAG)], FLAG)
    print(key)
    KEY = input("Введите ключ: ").encode()
    flag = XOR(ct, KEY)
    print(flag)

if __name__ == "__main__":
    main()
