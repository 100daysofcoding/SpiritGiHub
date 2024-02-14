import requests

def rechercher_recettes_par_ingredients(ingredients):
    url = 'https://www.themealdb.com/api/json/v1/1/filter.php'
    params = {'i': ingredients}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        meals = response.json().get('meals')
        if meals:
            for meal in meals:
                meal_id = meal['idMeal']
                obtenir_details_du_plat(meal_id)
        else:
            print("Aucun plat trouvé pour les ingrédients donnés.")
    else:
        print("Erreur lors de la recherche des plats.")

def obtenir_details_du_plat(meal_id):
    detail_url = f'https://www.themealdb.com/api/json/v1/1/lookup.php?i={meal_id}'
    response = requests.get(detail_url)

    if response.status_code == 200:
        meal_details = response.json().get('meals', [])[0]  # Prend le premier élément de la liste
        print(f"Nom du Plat: {meal_details['strMeal']}")
        print(f"Catégorie: {meal_details['strCategory']}")
        print(f"Zone: {meal_details['strArea']}")
        print(f"Instructions: {meal_details['strInstructions']}")
        print(f"Image: {meal_details['strMealThumb']}\n")
    else:
        print("Erreur lors de l'obtention des détails du plat.")

if __name__ == "__main__":
    ingredients = input("Entrez les ingrédients (par exemple, chicken, tomato): ")
    rechercher_recettes_par_ingredients(ingredients)
