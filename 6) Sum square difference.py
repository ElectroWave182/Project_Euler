from sys import stdin,stdout
input,print = stdin.readline,stdout.write
print(str(sum(range(101))**2 - sum([a**2 for a in range(101)])))