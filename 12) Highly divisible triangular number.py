from sys import stdin, stdout
input, print = stdin.readline, stdout.write
def prime(nb):
    liste = [str(div) + " " + str(nb // div) for div in range(1, int(nb**0.5 + 1)) if nb % div == 0]
    return list(" ".join(liste).split())
def divisors(somme):
    for n in range(2, 2**500):
        somme += n
        divs = prime(somme)
        if len(divs) > 500: return str(somme)
print(divisors(1))
