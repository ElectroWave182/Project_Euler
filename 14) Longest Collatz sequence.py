from sys import stdin, stdout
input, print = stdin.readline, stdout.write
def collatz(n):
    c = 0
    while n != 1:
        c += 1
        if n % 2 == 0: n //= 2
        else: n = 3*n + 1
    return c
long = [collatz(nb) for nb in range(2, 1000*1000)]
print(str(long.index(max(long)) + 2))
