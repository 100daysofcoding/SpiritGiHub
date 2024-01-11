import random
import string
import hashlib


def generate_random_password(length):
    if length < 4:
        raise ValueError("La longueur doit être d'au moins 4 caractères pour la diversité")

    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    password = [random.choice(letters), random.choice(digits), random.choice(symbols)]
    for _ in range(length - 3):
        password.append(random.choice(letters + digits + symbols))

    random.shuffle(password)
    return ''.join(password)


def generate_personalized_password(name, birthdate, length=12):
    if length < 4:
        raise ValueError("La longueur doit être d'au moins 4 caractères pour la diversité")

    base = name + birthdate
    hashed_base = hashlib.sha256(base.encode()).hexdigest()

    # Récupération d'une partie du hash pour le mot de passe
    password = hashed_base[:length]
    return password


# Exemple d'utilisation
mode = input("Choisissez le mode de génération (aléatoire/personnalisé): ").strip().lower()

if mode == "aléatoire":
    password_length = int(input("Entrez la longueur du mot de passe: "))
    password = generate_random_password(password_length)
elif mode == "personnalisé":
    name = input("Entrez votre nom: ")
    birthdate = input("Entrez votre date d'anniversaire (JJMMAAAA): ")
    password_length = 12
    password = generate_personalized_password(name, birthdate, password_length)
else:
    raise ValueError("Mode non reconnu")

print(f"Votre mot de passe généré est: {password}")
