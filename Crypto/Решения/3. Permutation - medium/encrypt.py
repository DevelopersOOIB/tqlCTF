from random import sample

def getKey(L):
    return sample(range(L), L)

def encrypt(path):
    L = 40
    with open(path, 'rb') as file:
        text = file.read()
    n = int.from_bytes(text[10:14], byteorder = "little")
    
    cipher = text[:n]
    text_pixel = [text[i: i+3] for i in range(n, len(text), 3)]
    len_pixel = len(text_pixel)
    
    text_table = [[text_pixel[i + j] for j in range(0, len_pixel, L)] for i in range(L)]
    key = getKey(L)
    cipher_table = [text_table[k] for k in key]
    c = b''.join([b''.join([cipher_table[i][j] for i in range(L)]) for j in range(len(text_table[0]))])
    cipher += c
    with open('cipher.bmp', 'wb') as file:
        file.write(cipher)

def main():
    encrypt('flag.bmp')

if __name__ == "__main__":
    main()
