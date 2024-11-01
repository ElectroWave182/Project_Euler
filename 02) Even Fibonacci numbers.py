n1,n2,fib = 1,2,[2]
while n1 + n2 < 4*10**6:
    n3 = n1 + n2
    n1,n2 = n2,n3
    if n2 % 2 == 0: fib.append(n2)
print(sum(fib))
