import tkinter
from tkinter import messagebox


def afficher_gagnant(gagnant):
    messagebox.showinfo("Tic Tac Toe", f"Le joueur {gagnant} a gagné la partie!")
    mettre_a_jour_scores()
    reinitialiser_partie()


def changer_joueur():
    global joueur_actuel
    if joueur_actuel == 'X':
        joueur_actuel = 'O'
    else:
        joueur_actuel = 'X'


def mettre_a_jour_scores():
    global scores_joueurs
    scores_joueurs[joueur_actuel] += 1
    mettre_a_jour_label_score()


def mettre_a_jour_label_score():
    label_score.config(text=f"Score - Joueur X: {scores_joueurs['X']} | Joueur O: {scores_joueurs['O']}")


def verifier_victoire():
    # Vérification de la victoire horizontale, verticale et diagonale
    for i in range(3):
        # Vérification de la victoire horizontale
        if boutons[i][0]['text'] == boutons[i][1]['text'] == boutons[i][2]['text'] != "":
            afficher_gagnant(boutons[i][0]['text'])
            return

        # Vérification de la victoire verticale
        if boutons[0][i]['text'] == boutons[1][i]['text'] == boutons[2][i]['text'] != "":
            afficher_gagnant(boutons[0][i]['text'])
            return

        # Vérification de la victoire diagonale
        if boutons[0][0]['text'] == boutons[1][1]['text'] == boutons[2][2]['text'] != "":
            afficher_gagnant(boutons[0][0]['text'])
            return

        # Vérification de la victoire diagonale inversée
        if boutons[0][2]['text'] == boutons[1][1]['text'] == boutons[2][0]['text'] != "":
            afficher_gagnant(boutons[0][2]['text'])
            return

    # Vérification de match nul
    if all(bouton['text'] in ['X', 'O'] for ligne in boutons for bouton in ligne):
        messagebox.showinfo("Tic Tac Toe", "Match nul!")
        reinitialiser_partie()


def placer_symbole(ligne, colonne):
    bouton_clique = boutons[colonne][ligne]
    if bouton_clique['text'] == "":
        bouton_clique.config(text=joueur_actuel)
        verifier_victoire()
        changer_joueur()


def reinitialiser_partie():
    global boutons, joueur_actuel, partie_terminee
    for colonne in range(3):
        for ligne in range(3):
            boutons[colonne][ligne].config(text="")
    joueur_actuel = 'X'
    partie_terminee = False


def annuler_dernier_coup():
    global partie_terminee, joueur_actuel
    if not partie_terminee and historique_coups:
        colonne, ligne = historique_coups.pop()
        boutons[colonne][ligne].config(text="")
        joueur_actuel = 'X' if joueur_actuel == 'O' else 'O'


def dessiner_grille():
    for colonne in range(3):
        for ligne in range(3):
            bouton = tkinter.Button(
                root, font=("Arial", 50),
                width=5, height=3,
                command=lambda l=ligne, c=colonne: placer_symbole(l, c)
            )
            bouton.grid(row=ligne, column=colonne)
            boutons[colonne][ligne] = bouton


boutons = [[None, None, None], [None, None, None], [None, None, None]]

# Variables du jeu
joueur_actuel = 'X'
partie_terminee = False
scores_joueurs = {'X': 0, 'O': 0}
historique_coups = []


root = tkinter.Tk()
root.title("Morpion")
root.minsize(300, 200)

# Label des scores
label_score = tkinter.Label(root, text="Score - Joueur X: 0 | Joueur O: 0", font=("Arial", 12))
label_score.grid(row=3, column=0, columnspan=3)


dessiner_grille()


bouton_reinitialiser = tkinter.Button(root, text="Réinitialiser la partie", command=reinitialiser_partie)
bouton_reinitialiser.grid(row=4, column=0, columnspan=2)

bouton_annuler_coup = tkinter.Button(root, text="Annuler le dernier coup", command=annuler_dernier_coup)
bouton_annuler_coup.grid(row=4, column=2, columnspan=2)

root.mainloop()
