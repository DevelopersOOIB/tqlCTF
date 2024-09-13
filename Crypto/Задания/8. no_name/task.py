import random
def code(d, a, c, s, pad, q):
    x = []
    for j in d:
        c += a.get(j)
        for _ in range(1, q, 1):
            s = random.choice(pad)
            x.append(s)
            c += s
    return c    
q = random.randint(2, 9)
d = input("input string: ").lower() 
pad = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
a = {'l': 'nht', 'q': 'dev', 't': 'kjg','_': 'rbh'}
c = ""

