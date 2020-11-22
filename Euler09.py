import math
def pitagora(n):
    for a in range(2, n):
        for b in range(2, n): 
            for c in range(2, n):
                if a ** 2 + b ** 2 == c ** 2 and a + b + c == n:
                    return a, b, c

print(pitagora(1000))