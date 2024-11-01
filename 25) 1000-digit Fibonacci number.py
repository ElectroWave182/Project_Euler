from sys import stdin, stdout
input, print = stdin.readline, stdout.write


def main ():

    _index = 1
    fibonacci = [1, 1]
    
    while True:
        last = fibonacci[-1]
        _index += 1
        fibonacci.append (last + fibonacci[-2])
        
        if len (str (last)) == 1000:
            break

    print (str (_index))


main ()