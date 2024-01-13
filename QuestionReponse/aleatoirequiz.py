import requests

API_KEY = "6sn5IgbAuowSaexxUFkXoweWBmzagnkkpQblNEVi"


def obtenir_questions_api(categorie, nb_questions=10):
    url = f"https://quizapi.io/api/v1/questions?apiKey={API_KEY}&limit={nb_questions}&tags={categorie}"
    params = {
        "apiKey": API_KEY,
        "limit": nb_questions,
        "tags": categorie
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("Erreur lors de la récupération des questions:", response.status_code, response.text)
        return []


def lancer_quiz():
    print("Choisissez une catégorie : MySQL, HTML, JavaScript, Linux, PHP, Python")
    categorie = input("Votre choix : ")

    questions = obtenir_questions_api(categorie)
    if not questions:
        return

    score = 0

    for question in questions:
        print(question["question"])
        options = [question["answers"][key] for key in question["answers"] if question["answers"][key]]
        correct_answer = question["correct_answers"][0]  # Vérifiez cette partie selon la structure de l'API

        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")
        reponse = int(input("Entrez le numéro de votre réponse : "))

        if options[reponse - 1] == correct_answer:
            score += 1

    print(f"Votre score est : {score} sur {len(questions)}")


lancer_quiz()
