from Cryptodome.Util.number import getPrime, bytes_to_long
from math import gcd
from os import urandom

FLAG = b'tqlCTF{???????????????????????????????????}'

def main():
    d = 3
    while True:
        p = getPrime(2048)
        if gcd(p-1, d) != 1:
            break
    flag = FLAG + urandom(64)
    print(f'sig = {pow(bytes_to_long(flag), d, p)}')
    print(f'p = {p}')

if __name__ == "__main__":
    main()
