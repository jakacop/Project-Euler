def je_deljiv(n, i):
    return n % i == 0

def je_deljiv_z_vsemi(n):
    for i in range(2, n):
        j = 2 
        if not(je_deljiv(j, i)):
            j += 1
        else:
            return j
        

print(je_deljiv_z_vsemi(10))