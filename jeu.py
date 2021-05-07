from qtido import *

def ligne_vide(n):
    res = []
    for i in range(n):
        res.append(0)
    return res

def grille_vide(m, n):
    res = []
    for i in range(m):
        res.append(ligne_vide(n))
    return res
 
    
def creer_les_pieces():
    pieces = []  
    
    piece1 = grille_vide(4,4)
    piece1[0][1] = piece1[1][1] = piece1[1][2]= piece1[2][2] = 1
    pieces.append(piece1)

    piece2 = grille_vide(4,4)
    piece2[0][2] = piece2[1][1] = piece2[1][2]= piece2[2][1] = 2
    pieces.append(piece2)

    piece3 = grille_vide(4,4)
    piece3[1][1] = piece3[1][2] = piece3[2][1]= piece3[2][2] = 3
    pieces.append(piece3)

    piece4 = grille_vide(4,4)
    piece4[1][0] = piece4[1][1] = piece4[1][2]= piece4[2][2] = 4
    pieces.append(piece4)

    piece5 = grille_vide(4,4)
    piece5[2][0] = piece5[2][1] = piece5[2][2]= piece5[1][2] = 5
    pieces.append(piece5)

    piece6 = grille_vide(4,4)
    piece6[1][0] = piece6[1][1] = piece6[1][2]= piece6[1][3] = 6
    pieces.append(piece6)

    piece7 = grille_vide(4,4)
    piece7[1][0] = piece7[1][1] = piece7[1][2]= piece7[2][1] = 7
    pieces.append(piece7)

    return pieces

    
def afficher(f, gr, px):
    H = len(gr)
    for i in range(len(gr)):
        ligne = gr[i]
        for j in range(len(ligne)):
            v = ligne[j]
            if v == 0:
                continue
            elif v == 1: couleur(f, 0.99, 0.75, 0.72)
            elif v == 2: couleur(f, 0.91, 0.22, 0.25)
            elif v == 3: couleur(f, 0.59, 0.52, 0.92)
            elif v == 4: couleur(f, 0.44, 0.55, 0.14)
            elif v == 5: couleur(f, 0.43, 0.03, 0.11)
            elif v == 6: couleur(f, 0.97, 0.6, 0.33)
            elif v == 7: couleur(f, 1, 0.5, 0)
            rectangle(f, j*px+1, (H-i-1)*px+1, (j+1)*px-1, (H-i)*px-1)

def afficher_piece(f, px, H, p, pos):
    for ii in range(4):
        ligne = p[ii]
        i = ii + pos[0]
        for jj in range(4):
            v = ligne[jj]
            j = jj + pos[1]
            if v > 0:
                rectangle(f, j*px+1, (H-i-1)*px+1, (j+1)*px-1, (H-i)*px-1)
                

def tourner_piece_droite(p):
    res = grille_vide(4, 4)
    for ii in range(4):
        for jj in range(4):
            res[ii][jj] = p[jj][3-ii]
    return res

def tourner_piece_gauche(p):
    return tourner_piece_droite(tourner_piece_droite(tourner_piece_droite(p)))

    
def probleme(gr, p, pos):
    H = len(gr)
    W = len(gr[1])
    for ii in range(4):
        ligne = p[ii]
        i = ii + int(pos[0])
        for jj in range(4):
            v = ligne[jj]
            j = jj + int(pos[1])
            if v > 0:
                if (j < 0) or (j >=W) or (i < 0) :
                    return True
                elif (i < H) and (i > 0)and gr[i][j] >0:
                    return True
           
    return False

def integrer_piece(gr, p, pos):
    H = len(gr)
    W = len(gr[1])
    for ii in range(4):
        ligne = p[ii]
        i = ii + int(pos[0])
        for jj in range(4):
            v = ligne[jj]
            j = jj + int(pos[1])
            if v > 0 :
                gr[i][j] = v
          
    
def retirer_ligne(gr, m):
    W = len(gr[m])
    del gr[m]
    gr.append(ligne_vide(W))
    


def retirer_lignes_pleines(gr):
    H = len(gr)
    W = len(gr[1])
    for i in range (H-1, -1, -1):
            if gr[i][0] > 0 and gr[i][1] > 0 and gr[i][2] > 0 and gr[i][3] > 0 and gr[i][4] > 0 and gr[i][5] > 0 and gr[i][6] > 0 and gr[i][7] > 0 and gr[i][8] > 0 and gr[i][9] > 0:
                retirer_ligne(gr, i)
                
            


