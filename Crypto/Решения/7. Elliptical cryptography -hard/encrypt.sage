
FLAG = b'tqlCTF{????????}' 
p = 4650808549
A = randint(0, p)
B = randint(0, p)
F = GF(p)
E = EllipticCurve(F, [A, B])
 
def getKey():
    G = E.gen(0)
    a = randint(2, p-2)
    D = G*a
    return G, D, a
    
def encrypt(m, G, D):
    k = randint(2, p-2)
    R = G*k
    P = D*k
    e = (m*P.xy()[0]) % p
    return R, e

def main():
    G, D, a = getKey()
    m = int.from_bytes(FLAG[:4], byteorder = 'big')
    R1, e1 = encrypt(m, G, D)
    m = int.from_bytes(FLAG[4:8], byteorder = 'big')
    R2, e2 = encrypt(m, G, D)
    m = int.from_bytes(FLAG[8:12], byteorder = 'big')
    R3, e3 = encrypt(m, G, D)
    m = int.from_bytes(FLAG[12:16], byteorder = 'big')
    R4, e4 = encrypt(m, G, D)
    print(f'p = {p}')
    print(f'A = {A}')
    print(f'B = {B}')
    print(f'G = {G.xy()}')
    print(f'D = {D.xy()}')
    print(f'e1, R1 = {e1, R1.xy()}')
    print(f'e2, R2 = {e2, R2.xy()}')
    print(f'e3, R3 = {e3, R3.xy()}')
    print(f'e4, R4 = {e4, R4.xy()}')
    
if __name__ == "__main__":
    main()