def naslednji_clen(n):
    if n % 2 == 0:
        return n // 2
    return 3 * n + 1

def dolzina_verige(n):
    k = 1
    while n > 1:
        n = naslednji_clen(n)
        k += 1
    return k

def resitev(n):
    najdaljse = 1
    for i in range(1, n + 1):
        l = dolzina_verige(i)
        if l > najdaljse:
            najdaljse = l
    return najdaljse

def resitev_2(n):
    for i in range(1, n):
        if dolzina_verige(i) == 525:
            return i
    
print(resitev_2(1000000))