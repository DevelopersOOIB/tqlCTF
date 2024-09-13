import random
'''
def decode(c, b, g, q, n, z, p, d):
    for j in d:
        c += a.get(j)
        for _ in range(1, q, 1):
            s = random.choice(f)
            x.append(s)
            c += s
    for i in c:
       b.append(i)
    g = " ".join(b)
    g = g.split(" ", (len(b) - q + 1))
    del g[-1]
    b.clear()
    for m in g:
        b.append(i)
    g = " ".join(g)
    g = g.split(" ", (len(b) - 3))
    p.append(g[-1])
    del g[-1]
    b.clear()
    for _ in range(len(d) - 1):
        for i in g:
            b.append(i)
        g = " ".join(b)
        g = g.split(" ", (len(b) - q + 1))
        del g[-1]
        b.clear()
        for i in g:
            b.append(i)
        g = " ".join(g)
        g = g.split(" ", (len(b) - 3))
        p.append(g[-1])
        del g[-1]
        b.clear()
    for j in range(len(d)):
        n += z.get(p[j])
    n.reverse()
    n = "".join(n)
    return n
'''
def decode_2_dot_0(d, l, wtf, m, giveakey):
    for i in d:
        m.append(i)
    m.reverse()
    l = " ".join(m)
    l = l.split(" ", (len(m) - 3))
    wtf.append(l[-1])
    del l[-1]
    m.clear()
    for i in range(len(l)):
        m.append(l[i])
    
    while True:
        if len(l) <= 1:
            break
        m.clear()
        for i in range(len(l)):
            m.append(l[i])
        l = " ".join(l)
        l = l.split((" "),(len(m) - giveakey))
        del l[-1]
        m.clear()
        for i in range(len(l)):
            m.append(l[i])
        l = " ".join(l)
        l = l.split(" ", (len(m) - 3))
        wtf.append(l[-1])
        del l[-1]
    return wtf

def code(d, a, c, s, f, q): # cypher
    for j in d:
        c += a.get(j)
        for _ in range(1, q, 1):
            s = random.choice(f)
            x.append(s)
            c += s
    return c    
q = random.randint(2, 9) # random
print(q)
q = 5 
d = input("flag: ").lower() # input
c = "" # result
s = "" # random_char
g = [] # dcode
b = [] # dcode
x = [] # padding
h = 0 # 
f = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] # паддинг
p = [] # dcode
n = [] # de_result
z = {'e w g': '0' ,'n g e': ' ' ,'b g f': '?' ,'r b h': '_' ,'j u i': '%' ,'p o u': '}' ,'j u y': '{' ,'r v j': ']' ,'r e r': '[' ,'t g r':')' ,'q w e':'(' ,'a e w':'=' ,'g r q' :'!' ,'v f g': ',' ,'q v z' :'.' ,'l f r' :'<' ,'p o i' :'>' ,'l h y' :':' ,'t b n' :';' ,'s w e' :'*' ,'l g t' :'/' ,'t f q' :'-' ,'g h r' :'+' ,'n t r' :'9' ,'d c r' :'8' ,'k j h' :'7' ,'s c d' :'6' ,'c v d' :'5' ,'x b r' :'4' ,'r d f' :'3' ,'f d s' :'2' ,'h f s' :'1','v f s' :'z' ,'b t r' :'y' ,'j y d' :'x' ,'v t e' :'w' ,'f r e' :'v' ,'t g h' :'u' ,'k j g' :'t' ,'h g s' :'s' ,'r d c' :'r' ,'d e v' :'q' ,'t v r' :'p' ,'r w c' :'o' ,'b e w' :'n' ,'b s d' :'m' ,'n h t' :'l' ,'x d e' :'k' ,'c w d' :'j' ,'u u g' :'i' ,'r g b' :'h' ,'u r v' :'g' ,'b g b' :'f' ,'m v h' :'e' ,'t g d' :'d' ,'n h g' :'c' ,'r s d' :'b' ,'d g f' :'a'} #обратный алфавит
a = {'0': 'ewg', 'a': 'dgf', 'b': 'rsd', 'c': 'nhg', 'd': 'tgd', 'e': 'mvh', 'f': 'bgb', 'g': 'urv', 'h': 'rgb', 'i': 'uug', 'j': 'cwd', 'k': 'xde', 'l': 'nht', 'm': 'bsd', 'n': 'bew', 'o': 'rwc', 'p': 'tvr', 'q': 'dev', 'r': 'rdc', 's': 'hgs', 't': 'kjg', 'u': 'tgh', 'v': 'fre', 'w': 'vte', 'x': 'jyd', 'y': 'btr', 'z': 'vfs','1': 'hfs', '2': 'fds', '3': 'rdf', '4': 'xbr', '5': 'cvd', '6': 'scd', '7': 'kjh', '8': 'dcr', '9': 'ntr', '+': 'ghr', '-': 'tfq', '/': 'lgt', '*': 'swe', ';': 'tbn', ':': 'lhy', '>': 'poi', '<': 'lfr', '.': 'qvz', ',': 'vfg', '!': 'grq', '=': 'aew', '(': 'qwe', ')': 'tgr', '[': 'rer', ']': 'rvj', '{': 'juy', '}': 'pou', '%': 'jui', '_': 'rbh', '?': 'bgf', ' ': 'nge'} #алфавит
m = []
l = []
wtf = []
whatisit = []
lol = []
aaaaa = []
sos = []
byebye = []

for i in d:
    whatisit.append(i)
whatisit.reverse()
whatisit = " ".join(whatisit)
whatisit = whatisit.split(" ", (len(d) - 3))
lol.append(whatisit[-1])
lol = " ".join(lol)
lol = lol.split(" ")
lol.reverse()
lol = " ".join(lol)
if lol in z:
    giveakey = int(input("Введите ключ:"))
    wtf = decode_2_dot_0(d, l, wtf, m, giveakey)
    for i in range(len(wtf)):
        if wtf[i] == '':
            del wtf[i]
    for _ in range(1, len(wtf) + 1, 1):
        aaaaa.append(wtf[0])
        
        del wtf[0]
        
        aaaaa = " ".join(aaaaa)
        aaaaa = aaaaa.split(" ")
        aaaaa = aaaaa[::-1]
        aaaaa = " ".join(aaaaa)
        aaaaa = aaaaa.split("-")
        sos += aaaaa
        aaaaa.clear()
    for i in range(len(sos)):
        if sos[i] in z:
            byebye += z.get(sos[i])

    byebye = "".join(byebye)
    print("Анти-шифр 2.0:", byebye)
else:
    print("Шифр:", code(d, a, c, s, f, q))
print("Текст:", d)
#Пример rgbHDluugVHz
