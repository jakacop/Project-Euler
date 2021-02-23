meseci = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def stetje_nedelj():
    dan = 0
    nedelja = 0
    for leto in range(1901, 2001):
        for i in meseci:
            dan += i
            if leto == 2000:
                None
            elif leto % 4 == 0 and i == 28:
                dan += 1
            if dan % 7 == 0:
                nedelja += 1
    return nedelja

print(stetje_nedelj())