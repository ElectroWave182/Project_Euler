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

    limite = 10 ** 4
    amicables = list ()
    
    for number in range (limite):
        dNumber = properDivisorsSum (number)
        
        if number != dNumber and properDivisorsSum (dNumber) == number:
            amicables.append (number)
            
    print (str (sum (amicables)))


main ()