def ajouter(a, b):
    """Retourne la somme de deux nombres."""
    return a + b


def soustraire(a, b):
    """Retourne la différence entre deux nombres."""
    return a - b


def multiplier(a, b):
    """Retourne le produit de deux nombres."""
    return a * b


def diviser(a, b):
    """Retourne le quotient de deux nombres. Renvoie None si division par zéro."""
    if b == 0:
        return None
    return a / b


def est_pair(n):
    """Retourne True si le nombre est pair."""
    return n % 2 == 0


def valeur_absolue(n):
    """Retourne la valeur absolue d'un nombre."""
    return n if n >= 0 else -n


def carre(n):
    """Retourne le carré d'un nombre."""
    return n * n


def palindrome_texte(texte):
    """Retourne True si le texte est un palindrome, sans tenir compte des espaces et de la casse."""
    nettoye = ''.join(ch.lower() for ch in texte if ch.isalnum())
    return nettoye == nettoye[::-1]


def compte_mots(texte):
    """Retourne le nombre de mots dans une chaîne de caractères."""
    return len(texte.split())


def moyenne(liste_nombres):
    """Retourne la moyenne d'une liste de nombres. Renvoie None si la liste est vide."""
    if not liste_nombres:
        return None
    return sum(liste_nombres) / len(liste_nombres)
