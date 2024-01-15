import json


class GestionnaireListeCourses:
    def __init__(self):
        self.liste_courses = []
        self.charger_liste()

    def sauvegarder(self):
        with open('liste_courses.json', 'w') as file:
            json.dump(self.liste_courses, file)

    def charger_liste(self):
        try:
            with open('liste_courses.json', 'r') as file:
                self.liste_courses = json.load(file)
        except FileNotFoundError:
            pass

    def ajouter(self, article):
        self.liste_courses.append(article)
        print(f'Article "{article}" ajouté avec succès à la liste de courses.')
        self.sauvegarder()

    def visualiser(self):
        if not self.liste_courses:
            print('La liste de courses est vide.')
        else:
            print('Liste de courses:')
            for index, article in enumerate(self.liste_courses, start=1):
                print(f'{index}. {article}')

    def marquer(self, index_article):
        if 1 <= index_article <= len(self.liste_courses):
            article_achete = self.liste_courses.pop(index_article - 1)
            print(f'Article "{article_achete}" marqué comme acheté.')
            self.sauvegarder()
        else:
            print('Indice d\'article invalide.')

    def supprimer(self, index_article):
        if 1 <= index_article <= len(self.liste_courses):
            article_supprime = self.liste_courses.pop(index_article - 1)
            print(f'Article "{article_supprime}" supprimé de la liste de courses.')
            self.sauvegarder()
        else:
            print('Indice d\'article invalide.')


def main():
    gestionnaire_courses = GestionnaireListeCourses()

    while True:
        print('\nMenu Gestionnaire de Listes de Courses:')
        print('1. Ajouter un Article')
        print('2. Visualiser la Liste de Courses')
        print('3. Marquer un Article comme Acheté')
        print('4. Supprimer un Article de la Liste')
        print('5. Quitter')

        choix = input('Entrez votre choix (1-5) : ')

        if choix == '1':
            article = input('Entrez le nom de l\'article : ')
            gestionnaire_courses.ajouter(article)
        elif choix == '2':
            gestionnaire_courses.visualiser()
        elif choix == '3':
            gestionnaire_courses.visualiser()
            indice_article = int(input('Entrez l\'indice de l\'article à marquer comme acheté : '))
            gestionnaire_courses.marquer(indice_article)
        elif choix == '4':
            gestionnaire_courses.visualiser()
            indice_article = int(input('Entrez l\'indice de l\'article à supprimer de la liste : '))
            gestionnaire_courses.supprimer(indice_article)
        elif choix == '5':
            print('Fermeture du Gestionnaire de Listes de Courses. Au revoir !')
            gestionnaire_courses.sauvegarder()
            break
        else:
            print('Choix invalide. Veuillez entrer un nombre entre 1 et 5.')


if __name__ == "__main__":
    main()
