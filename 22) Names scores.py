from string import ascii_uppercase
from sys import stdin, stdout
input, print = stdin.readline, stdout.write


def trim (chain):

    return chain.strip ('"')


def worth (chain):

    return sum ([
        letterValues[letter]
        for letter in chain
    ])


def main ():

    global letterValues
    letterValues = {
        ascii_uppercase[value]: value + 1
        for value in range (len (ascii_uppercase))
    }

    fichier = open ("0022_names.txt", "r")
    names = list (map (trim, fichier.read ().split (",")))
    names.sort ()

    scores = [
        (index + 1) * worth (names[index])
        for index in range (len (names))
    ]

    print (str (sum (scores)))


main ()