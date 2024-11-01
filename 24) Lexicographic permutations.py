def primeNumbers (limit):

    global primeFactors
    primeFactors = [2]

    for nb in range (3, limit):
        center = nb ** 0.5

        for prime in primeFactors:

            if prime > center:
                primeFactors.append (nb)
                break
            if nb % prime == 0:
                break


def decomposition (nb):

    factors = list ()

    while True:
        if nb == 1:
            return factors

        for prime in primeFactors:

            if nb % prime == 0:
                factors.append (prime)
                nb //= prime
                break


primeNumbers (100000)
print (decomposition (100000))