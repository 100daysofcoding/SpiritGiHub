import requests


def conversion_devises(montant, devise_source, devise_cible):
    url = f'https://api.exchangerate-api.com/v4/latest/{devise_source}'
    response = requests.get(url)

    if response.status_code == 200:
        taux_de_change = response.json()['rates'][devise_cible]
        montant_converti = montant * taux_de_change
        return montant_converti
    else:
        print("Erreur lors de la récupération des taux de change.")
        return None


def afficher_liste_devises():
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    response = requests.get(url)

    if response.status_code == 200:
        devises = response.json()['rates'].keys()
        print("Liste des devises disponibles :")
        for devise in devises:
            print(devise)
    else:
        print("Erreur lors de la récupération de la liste des devises.")


def main():
    print("Convertisseur de devises")

    afficher_liste_devises()

    montant = float(input("Entrez le montant à convertir : "))
    devise_source = input("Entrez la devise source : ").upper()
    devise_cible = input("Entrez la devise cible : ").upper()

    resultat = conversion_devises(montant, devise_source, devise_cible)

    if resultat is not None:
        print(f"{montant} {devise_source} équivaut à {resultat:.2f} {devise_cible}")


if __name__ == "__main__":
    main()
