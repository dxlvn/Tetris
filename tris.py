############# imports #############
from qtido import *
import random
import jeu


############# fonctions ######################


        
def piece_au_hasard():
    pieces = jeu.creer_les_pieces()
    nombre = random.randrange(7)
    return pieces[nombre]

def score(score_piece):
        if (score_piece<10):
            print("Vous avez perdu au niveau 0")
        elif (score_piece<20):
            print("Vous avez perdu au niveau 1")
        elif (score_piece<30):
            print("Vous avez perdu au niveau 2")
        elif (score_piece<40):
            print("Vous avez perdu au niveau 3")
        elif (score_piece<50):
            print("Vous avez perdu au niveau 4")
        elif (score_piece<60):
            print("Vous avez perdu au niveau 5")
        elif (score_piece<70):
            print("Vous avez perdu au niveau 6")
        elif (score_piece<80):
            print("Vous avez perdu au niveau 7")
        elif (score_piece<90):
            print("Vous avez perdu au niveau 8")
        elif (score_piece<100):
            print("Vous avez perdu au niveau 9")

        


def jeu_tetris():

    W = 10 # cases de large
    H = 20 # cases de haut
    px = 30 # pixels par cases
    f = creer(W*px, H*px)

    nv = jeu.grille_vide(H, W)

    piece = piece_au_hasard()
    piece_pos = [H-3, W/2 - 2]

    piece2 = piece_au_hasard()
    piece_pos2 = [H-3, W/2 - 2]

    piece3 = piece
    piece_pos3 = [piece_pos[0], W/2 - 2]

    score_piece = 1


    ############# Boucle Principale #############
    while not est_fermee(f):

        ############# AFFICHAGE #############
        effacer(f)
        jeu.afficher(f, nv, px)
        jeu.afficher_piece(f, px, H, piece, piece_pos)
        jeu.afficher_piece(f, px, H, piece2, piece_pos2)
        jeu.afficher_piece(f, px, H, piece3, piece_pos3)
        

        if (score_piece<10):
            attendre_evenement(f, 1000)
        elif (score_piece<20):
            attendre_evenement(f, 800)
        elif (score_piece<30):
            attendre_evenement(f, 600)
        elif (score_piece<40):
            attendre_evenement(f, 500)
        elif (score_piece<50):
            attendre_evenement(f, 400)
        elif (score_piece<60):
            attendre_evenement(f, 350)
        elif (score_piece<70):
            attendre_evenement(f, 300)
        elif (score_piece<80):
            attendre_evenement(f, 250)
        elif (score_piece<90):
            attendre_evenement(f, 200)
        elif (score_piece<10):
            attendre_evenement(f, 150)
        else :
            print(" ")
            print("Vous avez gagné, vous avez passé tous les niveaux")
            print("Votre score est de ", score_piece, " points")
            rep=input("Voulez vous retenter votre chance [o/n]")
            print(" ")
            exit()
            if rep == 'o':
                jeu_tetris()
            else:
                exit()
            
        
        
        e = dernier_evenement(f)

        while (jeu.probleme(nv, piece3, piece_pos3)==False):
            piece_pos3 = [piece_pos3[0]-1, piece_pos3[1]]
        piece_pos3 = [piece_pos3[0]+1, piece_pos3[1]]
    
        if e is not None:
            ############# EVENEMENTS (clavier etc) #############
            if e == 16777216: # touche ECHAP
                exit()
            elif e == 16777234: # gauche
                piece_pos = [piece_pos[0], piece_pos[1]-1]
                piece_pos3 = [piece_pos[0], piece_pos[1]]
                while (jeu.probleme(nv, piece3, piece_pos3)==False):
                    piece_pos3 = [piece_pos3[0]-1, piece_pos3[1]]
                piece_pos3 = [piece_pos3[0]+1, piece_pos3[1]]
                if jeu.probleme(nv, piece, piece_pos):
                    piece_pos = [piece_pos[0], piece_pos[1]+1]
                    piece_pos3 = [piece_pos3[0], piece_pos[1]]
            elif e == 16777235: # haut
                piece = jeu.tourner_piece_droite(piece)
                piece3 =  jeu.tourner_piece_droite(piece3)
                if jeu.probleme(nv, piece, piece_pos):
                    piece = jeu.tourner_piece_gauche(piece)
                    piece3 =  jeu.tourner_piece_gauche(piece3)
            elif e == 16777237: # bas
                piece = jeu.tourner_piece_gauche(piece)
                piece3 =  jeu.tourner_piece_gauche(piece3)
                if jeu.probleme(nv, piece, piece_pos):
                    piece =jeu.tourner_piece_droite(piece)
                    piece3 =  jeu.tourner_piece_droite(piece3)
            elif e == 16777236: # droite
                piece_pos = [piece_pos[0], piece_pos[1]+1]
                piece_pos3 = [piece_pos[0], piece_pos[1]]
                while (jeu.probleme(nv, piece3, piece_pos3)==False):
                    piece_pos3 = [piece_pos3[0]-1, piece_pos3[1]]
                piece_pos3 = [piece_pos3[0]+1, piece_pos3[1]]
                if jeu.probleme(nv, piece, piece_pos):
                    piece_pos = [piece_pos[0], piece_pos[1]-1]
                    piece_pos3 = [piece_pos3[0], piece_pos[1]]
            elif e == 65: # A
                piece_pos = [piece_pos[0]-1, piece_pos[1]]
                piece_pos3 = [piece_pos[0], piece_pos[1]]
                while (jeu.probleme(nv, piece3, piece_pos3)==False):
                    piece_pos3 = [piece_pos3[0]-1, piece_pos3[1]]
                piece_pos3 = [piece_pos3[0]+1, piece_pos3[1]]
                if jeu.probleme(nv, piece, piece_pos):
                    piece_pos = [piece_pos[0]+1, piece_pos[1]]
            elif e == 32: # espace
                while (jeu.probleme(nv, piece, piece_pos)==False):
                    piece_pos = [piece_pos[0]-1, piece_pos[1]]
                piece_pos = [piece_pos[0]+1, piece_pos[1]]
            
            pass # ne fait rien
        else:
            ############# SIMULATION (temps qui passe) #############
            piece_pos = [piece_pos[0]-1, piece_pos[1]]
            if jeu.probleme(nv, piece, piece_pos):
                score_piece = score_piece + 1
                piece_pos = [piece_pos[0]+1, piece_pos[1]]
                if piece_pos[0] == piece_pos2[0]:
                    print(" ")
                    score(score_piece)
                    print("Votre score est de ", score_piece, " points")
                    rep=input("Voulez vous retenter votre chance [o/n]")
                    print(" ")
                    if rep == 'o':
                        jeu_tetris()
                    else:
                        exit()
                jeu.integrer_piece(nv, piece, piece_pos)
                jeu.retirer_lignes_pleines(nv)
                piece = piece2
                piece2 = piece_au_hasard()
                piece3 = piece        
                piece_pos = [H-3, W/2-2]
                piece_pos3 = [piece_pos[0], piece_pos[1]]
            pass # ne fait rien

        
def instruction():
    print(" ")
    print("Vous vous apprêtez à jouer au jeu Tétris, avant tout veuillez lire les instructions/commandes : ")
    print(" ")
    print("Il existe differentes commandes :")
    print("   - La touche A : faire descendre la pièce")
    print("   - La touche fleche_du_bas : faire pivoter la pièce à gauche")
    print("   - La touche fleche_du_haut : faire pivoter la pièce à droite")
    print("   - La touche fleche_gauche : déplacer la pièce à gauche")
    print("   - La touche fleche_droite : déplacer le pièce à  droite")
    print("   - La touche espace : placer la pièce le plus bas possible directement")
    print(" ")
    print("Sachez que vous connaîtrez votre résultat seulement à la fin ( en cas de victoire ou de défaite ) et une demande si vous voulez rejouer ou non à Tétris.")
    print("Bon jeu!")
    print(" ")
    rep=input("Voulez vous jouer ? [o/n]")
    if rep == 'o':
       jeu_tetris()
    else:
       exit()

        
instruction()
