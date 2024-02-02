import tkinter as tk
from tkinter import messagebox, ttk
import json


class Contact:
    def __init__(self, nom, prenom, numero):
        self.nom = nom
        self.prenom = prenom
        self.numero = numero

    def to_dict(self):
        return {'nom': self.nom, 'prenom': self.prenom, 'numero': self.numero}

    @staticmethod
    def from_dict(data):
        return Contact(data['nom'], data['prenom'], data['numero'])


class GestionnaireContactsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestionnaire de Contacts")
        self.root.geometry("600x300")

        self.contacts = []
        self.charger_contacts()

        self.setup_ui()

    def setup_ui(self):
        self.configure_styles()

        # Cadre principal
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.pack(fill='both', expand=True)

        # Cadre pour l'ajout de contact
        self.frame_ajouter = ttk.LabelFrame(self.main_frame, text="Ajouter un Contact", padding="10")
        self.frame_ajouter.grid(row=0, column=0, padx=10, pady=5, sticky='ew')

        # Cadre pour la recherche et la suppression
        self.frame_actions = ttk.LabelFrame(self.main_frame, text="Rechercher et Supprimer", padding="10")
        self.frame_actions.grid(row=1, column=0, padx=10, pady=5, sticky='ew')

        self.ajouter_elements_interface()

    def configure_styles(self):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TButton', background="#0078D7", foreground="#ffffff")
        style.map('TButton', background=[('active', '#0053a0')])
        self.root.configure(bg="#f0f0f0")

    def ajouter_elements_interface(self):
        # Éléments pour ajouter un contact
        ttk.Label(self.frame_ajouter, text="Nom :").grid(row=0, column=0, sticky='w')
        self.entry_nom = ttk.Entry(self.frame_ajouter, width=30)
        self.entry_nom.grid(row=0, column=1, sticky='ew', padx=10, pady=4)

        ttk.Label(self.frame_ajouter, text="Prénom :").grid(row=1, column=0, sticky='w')
        self.entry_prenom = ttk.Entry(self.frame_ajouter, width=30)
        self.entry_prenom.grid(row=1, column=1, sticky='ew', padx=10, pady=4)

        ttk.Label(self.frame_ajouter, text="Numéro :").grid(row=2, column=0, sticky='w')
        self.entry_numero = ttk.Entry(self.frame_ajouter, width=30)
        self.entry_numero.grid(row=2, column=1, sticky='ew', padx=10, pady=4)

        ttk.Button(self.frame_ajouter, text="Ajouter", command=self.ajouter_contact).grid(row=3, column=0, columnspan=2,
                                                                                                pady=5)
        ttk.Button(self.frame_actions, text="Afficher Tous", command=self.afficher_tous_contacts).pack(side='left', pady=5)

        ttk.Label(self.frame_actions, text="Rechercher :").pack(side='left', padx=5)
        self.entry_recherche = ttk.Entry(self.frame_actions, width=30)
        self.entry_recherche.pack(side='left', padx=5)

        ttk.Button(self.frame_actions, text="Rechercher", command=self.rechercher_contact).pack(side='left', padx=5)
        ttk.Button(self.frame_actions, text="Supprimer", command=self.supprimer_contact).pack(side='left', padx=5)


    def ajouter_contact(self):
        nom = self.entry_nom.get()
        prenom = self.entry_prenom.get()
        numero = self.entry_numero.get()
        if nom and prenom and numero:
            self.contacts.append(Contact(nom, prenom, numero))
            self.sauvegarder_contacts()
            messagebox.showinfo("Succès", "Contact ajouté avec succès.")
        else:
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")

    def rechercher_contact(self):
        recherche = self.entry_recherche.get().lower()
        trouves = [c for c in self.contacts if recherche in c.nom.lower() or recherche in c.prenom.lower()
                   or recherche in c.numero]
        if trouves:
            message = "\n".join(f"Nom : {c.nom}, Prénom : {c.prenom}, Numéro : {c.numero}" for c in trouves)
            messagebox.showinfo("Résultats de recherche", message)
        else:
            messagebox.showinfo("Résultats de recherche", "Aucun contact trouvé.")

    def supprimer_contact(self):
        recherche = self.entry_recherche.get().lower()
        self.contacts = [c for c in self.contacts if recherche not in c.nom.lower() and recherche
                         not in c.prenom.lower() and recherche not in c.numero]
        self.sauvegarder_contacts()
        messagebox.showinfo("Succès", "Contact(s) supprimé(s) si présent(s).")

    def sauvegarder_contacts(self):
        with open("contacts.json", "w") as file:
            json.dump([contact.to_dict() for contact in self.contacts], file, indent=4)

    def charger_contacts(self):
        try:
            with open("contacts.json", "r") as file:
                self.contacts = [Contact.from_dict(data) for data in json.load(file)]
        except FileNotFoundError:
            self.contacts = []

    def afficher_tous_contacts(self):
        if self.contacts:
            message = "\n".join(f"Nom : {c.nom}, Prénom : {c.prenom}, Numéro : {c.numero}" for c in self.contacts)
            messagebox.showinfo("Tous les Contacts", message)
        else:
            messagebox.showinfo("Tous les Contacts", "Aucun contact enregistré.")


def main():
    root = tk.Tk()
    app = GestionnaireContactsGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
