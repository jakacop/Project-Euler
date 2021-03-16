def pridobi_trikotnik(datoteka):
    with open(datoteka, 'r', encoding='utf8') as dat:
        trikotnik = [[int(stevilo) for stevilo in vrstica.split(' ')] for vrstica in dat]
    return trikotnik

matrika = pridobi_trikotnik("Euler67.txt")
def najvecja_pot():
    for i in range(len(matrika) - 2, -1, -1):
        for j in range(i + 1):
            matrika[i][j] = max(matrika[i][j] + matrika[i + 1][j], matrika[i][j] + matrika[i + 1][j + 1]) 
    return matrika[0][0]

print(najvecja_pot())