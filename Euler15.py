import math
def binomski(n, p):
    return math.factorial(n) // (math.factorial(p) * math.factorial(n - p))

print(binomski(40, 20))