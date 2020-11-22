def je_deljiv_z_vsemi(n, i):
    for j in range(2, i + 1):
        if n % j != 0:
            return False
    return True
        
n = 2520
while not(je_deljiv_z_vsemi(n, 20)):
    n += 2520

print(n)