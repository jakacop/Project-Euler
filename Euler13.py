def vsota():
    datoteka = open("Euler13.txt", "r")

    vsota = 0
    for line in datoteka:
        vsota += int(line)
    return vsota

    datoteka.close

print(vsota())