from os import urandom
from Cryptodome.Util.number import getPrime, bytes_to_long

FLAG = b'tqlCTF{????????????????????}'

def Blackley_scheme(s, t, n):
    p = getPrime(1025)
    s = s + urandom(t - len(s))
    A = [0] * n
    Y = [0] * n
    for i in range(n):
        A[i] = [bytes_to_long(urandom(128)) for _ in range(t)]
        Y[i] = sum([(A[i][j]*s[j]) % p for j in range(t)]) % p
    return A, Y, p

def main():
    t = 40
    n = 50
    A, Y, p = Blackley_scheme(FLAG, t, n)
    for i in range(n):
        with open(f'key{i}.txt', 'w') as file:
            file.write(f'A{i} = {A[i]}\nY{i} = {Y[i]}\np = {p}')
    
if __name__ == "__main__":
    main()
