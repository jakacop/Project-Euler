from itertools import permutations 
def permutacije(m, n):
    return list(permutations(range(m + 1)))[n - 1]

print(permutacije(9, 1000000))