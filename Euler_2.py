#def fibonacci(n):
#    if n == 0:
#        return 1
#    elif n == 1:
#        return 1
#    else:
#        return fibonacci(n - 1) + fibonacci(n - 2)

#def max_fibonacci(n):
#    if fibonacci(n) <= 4000000:
#        return 1
#    else:
#        return 0

#x = 1

#while True:
#    print(x, fibonacci(x))
#    x += 1
    
fibonaccijeva_stevila = [0, 1]
for i in range(2,35):
    fibonaccijeva_stevila.append(fibonaccijeva_stevila[i-1]+fibonaccijeva_stevila[i-2])

vsota = sum(fibonaccijeva_stevila[0::3])
print(vsota)

input()
