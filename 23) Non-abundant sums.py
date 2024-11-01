from sys import stdin, stdout
input, print = stdin.readline, stdout.write


def pairs (big, small):

    div = big // small
    
    if div == small:
        return small
    return div + small


def properDivisorsSum (big):
    
    return sum ([
        pairs (big, small)
        for small in range (2, int (big ** 0.5) + 1)
        if big % small == 0
    ]) + 1
            

def main ():

    limit = 28 * 1000 + 124
    abundants = {
        number
        for number in range (1, limit)
        if number < properDivisorsSum (number)
    }
    
    writable = {
        abA + abB
        for abA in abundants
        for abB in abundants
    }
    result = sum (set (range (limit)) - writable)
    
    print (str (result))


main ()