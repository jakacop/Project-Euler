#def harm_sum(n):
#  if n < 2:
#    return 1
#  else:
#    return (1 / n) + (harm_sum(n - 1))
#x = 1
#while True:
#    print(x, harm_sum(x))
#    x += 1

#n = 1
#while True:
#  print(n, (1 / n))
#  n += 1

vsota = 0
n = 1
while True:
  vsota += 1 / n
  n += 1
  if n % 1000 == 0:
    (print(n, vsota))
