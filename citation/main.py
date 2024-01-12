import tkinter as tk
import random
from tkinter import font


citations = [
    "La vie est ce qui arrive quand on a d'autres projets. - John Lennon",
    "Soyez le changement que vous voulez voir dans le monde. - Mahatma Gandhi",
    "Le seul vrai échec est de ne pas essayer. - George Clooney",
    "L'informatique est la science du compliqué. - Donald Knuth, informaticien américain",
    "L'informatique n'est qu'un outil, comme un pinceau ou un crayon. "
    "Ce que nous en faisons est ce qui compte. - Alan Kay, informaticien américain,"
    "L'informatique est l'art de faire tourner des machines pour faire des choses que l'on ne sait pas faire."
    " - Edsger W. Dijkstra, informaticien néerlandais",
    "L'informatique est la science de l'information, de son traitement et de sa communication. "
    "- Jean-Claude Laprie, informaticien français",
    "Un code supprimé est un code débogué. - Bill Gates, informaticien américain",
    "Les logiciels et les cathédrales, c'est un peu la même chose - d'abord on les construit, ensuite on prie."
    " - Frederick Brooks, informaticien américain",
    "UNIX n'a pas été conçu pour empêcher les gens de faire des choses stupides, "
    "car cela les empêcherait aussi de faire des choses intelligentes.- Ken Thompson, informaticien américain",
    "Le matériel est fait pour durer. Le logiciel est fait pour être mis à jour. - Bill Gates, informaticien américain",
    "La meilleure défense contre les pirates est une bonne éducation des utilisateurs."
    " - Steve Gibson, informaticien américain",
    "La sécurité informatique est une question de comportement, pas de technologie."
    " - Bruce Schneier, informaticien américain"
]


def afficher_citation_aleatoire():
    citation = random.choice(citations)
    label_citation.config(text=citation)


root = tk.Tk()
root.title("Decouvrez Notre Repertoire  de Citations Aléatoires")

root.geometry("500x200")
root.resizable(False, False)
root.configure(bg="gray")

font_label = font.Font(family="Helvetica", size=12, weight="bold")
font_bouton = font.Font(family="Helvetica", size=10)

label_citation = tk.Label(root, text="", wraplength=400, justify="center", bg="gray", font=font_label)
label_citation.pack(pady=20)

bouton = tk.Button(root, text="Générer une Citation", command=afficher_citation_aleatoire, font=font_bouton)
bouton.pack(pady=20)

root.mainloop()
