from sys import stdin, stdout
input, print = stdin.readline, stdout.write
def prime(nb):
    for div in range(2, int(nb**0.5 + 1)):
        if nb % div == 0: return False
    return True
print(str(sum([nb for nb in range(3, 2000*1000, 2) if prime(nb)]) + 2))
