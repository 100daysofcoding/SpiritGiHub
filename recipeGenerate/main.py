import requests


def trouver_recettes(ingredients, cle_api):
    url_api = "https://api.spoonacular.com/recipes/findByIngredients"
    params = {
        'apiKey': cle_api,
        'ingredients': ingredients,
        'number': 1,
    }
    try:
        reponse = requests.get(url_api, params=params)
        reponse.raise_for_status()
        return reponse.json()
    except requests.RequestException as e:
        print(f"Erreur lors de la requête à l'API Spoonacular: {e}")
        return None


def details_recette(id_recette, cle_api):
    url_details = f"https://api.spoonacular.com/recipes/{id_recette}/information"
    params = {'apiKey': cle_api}
    try:
        reponse = requests.get(url_details, params=params)
        reponse.raise_for_status()
        return reponse.json()
    except requests.RequestException as e:
        print(f"Erreur lors de la requête des détails de la recette: {e}")
        return None


cle_api = "ddb9de47d1494720b9b991bda9dc98fa"

ingredients_utilisateur = input("Entrez les ingrédients séparés par des virgules (ex. tomates, mozzarella, basilic): ")
recettes = trouver_recettes(ingredients_utilisateur, cle_api)

if recettes:
    for recette in recettes:
        details = details_recette(recette['id'], cle_api)
        if details:
            print(f"Recette: {details['title']}\nInstructions: {details.get('instructions', 'Pas d\'instructions disponibles.')}\n")
else:
    print("Aucune recette trouvée.")
