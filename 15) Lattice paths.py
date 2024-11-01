# Po assez de mémoire...
"""from itertools import permutations
from sys import stdin, stdout
input, print = stdin.readline, stdout.write
def path(cote):
    prec, carte, bordel = 0, [], sorted(list(permutations("rd"*cote)))
    for chemin in bordel:
        if chemin != prec: carte.append(chemin)
        prec = chemin
    return str(len(carte))
print(path(int(input())))"""

# Plus simple avec les maths :)
u, m, t = 2, 2, 0
for n in range(1, int(input())):
    t += n
    m += 1/t
    u = round(u*m)
print(u)
