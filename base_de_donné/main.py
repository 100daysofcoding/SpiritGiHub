import sqlite3

class LivreDatabase:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.conn.execute('''CREATE TABLE IF NOT EXISTS livres
                             (id INTEGER PRIMARY KEY, titre TEXT, auteur TEXT, annee INT)''')

    def ajouter_livre(self, titre, auteur, annee):
        self.conn.execute("INSERT INTO livres (titre, auteur, annee) VALUES (?, ?, ?)",
                          (titre, auteur, annee))
        self.conn.commit()

    def supprimer_livre(self, livre_id):
        self.conn.execute("DELETE FROM livres WHERE id = ?", (livre_id,))
        self.conn.commit()

    def modifier_livre(self, livre_id, titre, auteur, annee):
        self.conn.execute("UPDATE livres SET titre = ?, auteur = ?, annee = ? WHERE id = ?",
                          (titre, auteur, annee, livre_id))
        self.conn.commit()

    def afficher_livres(self):
        cursor = self.conn.execute("SELECT id, titre, auteur, annee FROM livres")
        for row in cursor:
            print(f"ID: {row[0]}, Titre: {row[1]}, Auteur: {row[2]}, Année: {row[3]}")

    def __del__(self):
        self.conn.close()

def menu():
    db = LivreDatabase('ma_bibliotheque.db')
    while True:
        print("\nOptions:")
        print("1. Ajouter un livre")
        print("2. Supprimer un livre")
        print("3. Modifier un livre")
        print("4. Afficher les livres")
        print("5. Quitter")
        choix = input("Entrez votre choix: ")

        if choix == '1':
            titre = input("Entrez le titre: ")
            auteur = input("Entrez l'auteur: ")
            annee = int(input("Entrez l'année de publication: "))
            db.ajouter_livre(titre, auteur, annee)

        elif choix == '2':
            livre_id = int(input("Entrez l'ID du livre à supprimer: "))
            db.supprimer_livre(livre_id)

        elif choix == '3':
            livre_id = int(input("Entrez l'ID du livre à modifier: "))
            titre = input("Entrez le nouveau titre: ")
            auteur = input("Entrez le nouvel auteur: ")
            annee = int(input("Entrez la nouvelle année de publication: "))
            db.modifier_livre(livre_id, titre, auteur, annee)

        elif choix == '4':
            db.afficher_livres()

        elif choix == '5':
            print("Au revoir!")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    menu()
