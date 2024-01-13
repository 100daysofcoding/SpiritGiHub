questions = [
    {
        "question": "Quelle est la principale différence entre un système d'exploitation "
                    "32 bits et un système d'exploitation 64 bits ?",
        "options": ["La vitesse du processeur", "Le type de logiciel qu'il peut exécuter",
                    "La quantité de mémoire RAM qu'il peut gérer", "La taille de l'écran"],
        "reponse": "La quantité de mémoire RAM qu'il peut gérer"
    },
    {
        "question": "Qu'est-ce qu'un algorithme ?",
        "options": ["Un problème dans un programme", "Un type de langage de programmation",
                    "Une procédure ou formule pour résoudre un problème",
                    "Un outil pour mesurer la performance du processeur"],
        "reponse": "Une procédure ou formule pour résoudre un problème"
    },
    {
        "Question": "Qui est considéré comme le père de l'informatique ?",
        "Options": ["Charles Babbage", "Alan Turing", "John von Neumann", "Ada Lovelace"],
        "Réponse": "Charles Babbage"
    },
    {
        "question": "Dans quel langage de programmation le système d'exploitation Linux est-il principalement écrit ?",
        "options": ["C++", "Python", "C", "Java"],
        "reponse": "C"
    },
    {
        "question":  "Quel langage de programmation est connu pour son utilisation "
                     "dans le développement Web côté serveur ?",
        "options": ["Python", "JavaScript", "C#", "PHP"],
        "reponse": "PHP"
    },
    {
        "question": "Quel est le terme utilisé pour décrire une erreur, un défaut ou un "
                    "défaut de conception dans un programme informatique ou un système d'exploitation ?",
        "options": ["Virus", "Bug", "Malware", "Ransomware"],
        "reponse": "Bug"
    },
    {
        "question": "Qui a inventé le World Wide Web ?",
        "options": ["Tim Berners-Lee", "Bill Gates", "Steve Jobs", "Mark Zuckerberg"],
        "reponse": "Tim Berners-Lee"
    },
    {
        "question": "Dans quel langage HTML est-il principalement écrit ?",
        "options": ["HyperText Markup Language", "Cascading Style Sheets", "JavaScript", "Python"],
        "reponse": "HyperText Markup Language"
    },
    {
        "question": "Quel protocole est utilisé pour sécuriser les communications sur un réseau informatique ?",
        "options": ["HTTP", "SSL/TLS", "FTP", "SSH"],
        "reponse": "SSL/TLS"
    },
    {
        "question": "Quel est le terme utilisé pour décrire un programme informatique malveillant "
                    "conçu pour endommager ou perturber les systèmes ?",
        "options": ["Virus", "Firewall", "Algorithme", "Database"],
        "reponse": "Virus"
    },
    {
        "question": "Dans le contexte des logiciels, que signifie 'SaaS' (Software as a Service) ?",
        "options": ["Un logiciel vendu en tant que produit complet", "Un logiciel offert en tant que "
                    "service via Internet", "Un logiciel open source", "Un standard de codage de logiciels"],
        "reponse": "Un logiciel offert en tant que service via Internet"
    },
    {
        "question": "Quelle est la principale différence entre une application web et une application de bureau ?",
        "options": ["La plateforme d'exécution", "Le langage de programmation utilisé", "Le coût de développement",
                    "Le type de licence"],
        "reponse": "La plateforme d'exécution"
    },
]


def lancer_quiz():
    score = 0
    for question in questions:
        print(question["question"])
        for i, option in enumerate(question["options"], start=1):
            print(f"{i}. {option}")
        reponse = input("Entrez le numéro de votre réponse : ")
        if question["options"][int(reponse) - 1] == question["reponse"]:
            score += 1
    print(f"Votre score est : {score} sur {len(questions)}")


lancer_quiz()
