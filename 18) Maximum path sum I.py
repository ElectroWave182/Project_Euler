from sys import stdin, stdout
input, print = stdin.readline, stdout.write


def main ():


    # Entrées

    triangle = []
    while True:
    
        entree = list (map (int, input ().rstrip ('\n').split ()))
        if entree == []:
            break
            
        triangle.append (entree)
    
    
    # Traitement
    
    taille = len (triangle)
    for ligne in range (1, taille):
    
        # Remplacement de l'intérieur
        for colonne in range (1, ligne):
            triangle[ligne][colonne] += max (triangle[ligne - 1][colonne - 1: colonne + 1])
            
        # Remplacement des bords
        triangle[ligne][0] += triangle[ligne - 1][0]
        triangle[ligne][ligne] += triangle[ligne - 1][ligne - 1]
        
    
    # Sortie
    
    meilleur = max (triangle[-1])
    print (str (meilleur))


main ()