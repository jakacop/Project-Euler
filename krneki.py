#import math
#def obseg_kroga(r):
#    return(math.pi * 2 * r)

#print(obseg_kroga(2))  
#s = ((((d - f) ** 2) + ((e - g) ** 2)) ** 0.5) + ((((f - h) ** 2) + ((g - i) ** 2)) ** 0.5) + ((((d - h) ** 2) + ((e - i) ** 2)) ** 0.5)
def ploscina_trikotnika(x1, y1, x2, y2, x3, y3):
    a = (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5
    b = (((x1 - x3) ** 2) + ((y1 - y3) ** 2)) ** 0.5
    c = (((x2 - x3) ** 2) + ((y2 - y3) ** 2)) ** 0.5
    s = 0.5 * (a + b + c)    
    return(((s * (s-a) * (s-b) * (s-c)) ** 0.5))

def kolinearne(x1, y1, x2, y2, x3, y3):
    if ploscina_trikotnika == 0:
        return True
    else:
        return False

print(ploscina_trikotnika(0, 0, 1, 1, 2, 2))
print(kolinearne(0, 0, 1, 1, 2, 2))
