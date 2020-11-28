def generator(n):
    return [i for i in range(2, n + 1)]

def combinations(m, n):
    lst = generator(m)
    new_lst = []
    for i in range(2, n + 1):
        for x in lst:
            new_lst.append(x ** i)
    return set(new_lst)
    
print(len(combinations(100, 100)))