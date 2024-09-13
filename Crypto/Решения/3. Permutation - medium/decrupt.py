from collections import Counter

def Deviation(stat1, stat2):
    return sum([abs(stat1[k] - stat2[k]) if k in stat2.keys() else stat1[k] for k in stat1.keys()])

def main():
    L = 20
    with open('original.bmp', 'rb') as file:
        text = file.read()
    n = int.from_bytes(text[10:14], byteorder = "little")

    text_pixel = [text[i: i+3] for i in range(n, len(text), 3)]
    len_pixel = len(text_pixel)

    text_table = [[text_pixel[i + j] for j in range(0, len_pixel, L)] for i in range(L)]
    text_table_stat = [dict(Counter([text_table[i][j] + text_table[i+1][j] for j in range(len(text_table[0]))])) for i in range(L - 1)]

    with open('cipher.bmp', 'rb') as file:
        text = file.read()
    n = int.from_bytes(text[10:14], byteorder = "little")

    text_pixel = [text[i: i+3] for i in range(n, len(text), 3)]
    len_pixel = len(text_pixel)
    text_table = [[text_pixel[i + j] for j in range(0, len_pixel, L)] for i in range(L)]

    print(sum(text_table_stat[1].values()))
    key = [-1] * L
    for i in range(L):
        print(i)
        min_stat = sum(text_table_stat[0].values())
        mi, mj = 0, 0
        for j in range(L):
            if i == j:
                continue
            stat = dict(Counter([text_table[i][k] + text_table[j][k] for k in range(len(text_table[0]))]))
            for k in range(L-1):
                D = Deviation(stat, text_table_stat[k])
                if D < min_stat:
                    min_stat, mk, mi, mj = D, k, i, j
        print(min_stat, mk, mi, mj)
        key[mk] = mi
        key[mk+1] = mj
            
    cipher = text[:n]
    cipher_table = [text_table[k] for k in key]
    c = b''.join([b''.join([cipher_table[i][j] for i in range(L)]) for j in range(len(text_table[0]))])
    cipher += c
    with open('flag.bmp', 'wb') as file:
        file.write(cipher)

if __name__ == "__main__":
    main()
