from sys import stdin, stdout
input, print = stdin.readline, stdout.write
def pyt():
    for a in range(1, 1000):
        for b in range(1, 1000):
            c = (a**2 + b**2)**0.5
            if a + b + c == 1000: return str(int(a*b*c))
print(pyt())
