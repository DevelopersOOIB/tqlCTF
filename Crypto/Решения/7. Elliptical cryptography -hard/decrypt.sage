
p = 4650808549
A = 325035285
B = 4054551112
F = GF(p)
E = EllipticCurve(F, [A, B])
G = E(1454217392, 462276932)
D = E(4475944596, 408442178)
e1, R1 = (567472967, E(3674218596, 1183842324))
e2, R2 = (4490099936, E(3989192736, 876200754))
e3, R3 = (3635967805, E(1645303056, 2776795690))
e4, R4 = (3617222044, E(4389916313, 2528662825))

def main():
    a = G.discrete_log(D)
    print(a)
    P = R1*a
    m = (e1 * pow(P.xy()[0], -1, p)) % p
    flag = int(m).to_bytes(4, byteorder = 'big')
    P = R2*a
    m = (e2 * pow(P.xy()[0], -1, p)) % p
    flag += int(m).to_bytes(4, byteorder = 'big')
    P = R3*a
    m = (e3 * pow(P.xy()[0], -1, p)) % p
    flag += int(m).to_bytes(4, byteorder = 'big')
    P = R4*a
    m = (e4 * pow(P.xy()[0], -1, p)) % p
    flag += int(m).to_bytes(4, byteorder = 'big')
    print(flag)
    
if __name__ == "__main__":
    main()