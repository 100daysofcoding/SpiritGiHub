def addition(x, y):
    return x + y


def soustraction(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    if y == 0:
        return "Erreur: Division par zéro"
    else:
        return x / y


while True:
    print("Options:")
    print("Entrez 'add' pour additionner deux nombres")
    print("Entrez 'sub' pour soustraire deux nombres")
    print("Entrez 'mul' pour multiplier deux nombres")
    print("Entrez 'div' pour diviser deux nombres")
    print("Entrez 'quit' pour quitter le programme")
    user_input = input(": ")

    if user_input == "quit":
        break
    elif user_input in ('add', 'sub', 'mul', 'div'):
        num1 = float(input("Entrez le premier nombre: "))
        num2 = float(input("Entrez le deuxième nombre: "))

        if user_input == 'add':
            print("Le résultat est", addition(num1, num2))

        elif user_input == 'sub':
            print("Le résultat est", soustraction(num1, num2))

        elif user_input == 'mul':
            print("Le résultat est", multiplication(num1, num2))

        elif user_input == 'div':
            print("Le résultat est", division(num1, num2))
    else:
        print("Entrée non valide")
