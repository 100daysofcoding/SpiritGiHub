class Contact:
    def __init__(self, nom, prenom, numero):
        self.nom = nom
        self.prenom = prenom
        self.numero = numero

    def afficher(self):
        print(f"Nom : {self.nom}, Prénom : {self.prenom}, Numéro : {self.numero}")

class GestionnaireContacts:
    def __init__(self):
        self.contacts = []

    def ajouter_contact(self, contact):
        self.contacts.append(contact)
        print("Contact ajouté avec succès.")

    def afficher_contacts(self):
        if self.contacts:
            print("Liste des contacts :")
            for contact in self.contacts:
                contact.afficher()
        else:
            print("Aucun contact.")

    def rechercher_contact(self, nom):
        for contact in self.contacts:
            if contact.nom.lower() == nom.lower():
                contact.afficher()
                return
        print("Contact non trouvé.")

    def supprimer_contact(self, nom):
        for contact in self.contacts:
            if contact.nom.lower() == nom.lower():
                self.contacts.remove(contact)
                print("Contact supprimé avec succès.")
                return
        print("Contact non trouvé.")

def main():
    gestionnaire = GestionnaireContacts()

    while True:
        print("\nMenu :")
        print("1. Ajouter un contact")
        print("2. Afficher tous les contacts")
        print("3. Rechercher un contact")
        print("4. Supprimer un contact")
        print("5. Quitter")

        choix = input("Entrez votre choix (1-5) : ")

        if choix == "1":
            nom = input("Entrez le nom du contact : ")
            prenom = input("Entrez le prénom du contact : ")
            numero = input("Entrez le numéro de téléphone du contact : ")
            contact = Contact(nom, prenom, numero)
            gestionnaire.ajouter_contact(contact)
        elif choix == "2":
            gestionnaire.afficher_contacts()
        elif choix == "3":
            nom_recherche = input("Entrez le nom du contact à rechercher : ")
            gestionnaire.rechercher_contact(nom_recherche)
        elif choix == "4":
            nom_suppression = input("Entrez le nom du contact à supprimer : ")
            gestionnaire.supprimer_contact(nom_suppression)
        elif choix == "5":
            print("Programme terminé.")
            break
        else:
            print("Choix invalide. Veuillez entrer un nombre entre 1 et 5.")

if __name__ == "__main__":
    main()
