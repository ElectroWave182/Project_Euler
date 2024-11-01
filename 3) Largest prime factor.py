nombre,noPrime = int(input()),True
while noPrime:
    noPrime = False
    for fac in range(2,nombre):
        if nombre % fac == 0:
            nombre //= fac
            noPrime = True
            break
print(nombre)