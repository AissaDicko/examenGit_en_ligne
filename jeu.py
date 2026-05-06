import random
import sys

# Couleurs pour un design fun et girly
PINK = "\033[95m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
BOLD = "\033[1m"
END = "\033[0m"


def display_title():
    print(f"{PINK}{BOLD}")
    print("  🌟✨ BIENVENUE DANS GLAM BRAIN PARTY ✨🌟")
    print("  Un jeu girly, fun et un peu smart... juste pour toi !")
    print(f"{END}")
    print(f"{BLUE}Prépare-toi à briller avec des quiz, des énigmes et du style !{END}\n")


def question_quiz():
    questions = [
        {
            "question": "Quel accessoire est généralement associé à un look girly ?",
            "choices": ["A) Un sac pailleté", "B) Des bottes de pluie", "C) Un casque de vélo"],
            "answer": "A"
        },
        {
            "question": "Quelle couleur est souvent appelée "rose poupée" ?",
            "choices": ["A) Émeraude", "B) Fuchsia", "C) Indigo"],
            "answer": "B"
        },
        {
            "question": "Quel animal est souvent utilisé comme symbole de féminité et de douceur ?",
            "choices": ["A) Licorne", "B) Chèvre", "C) Crocodile"],
            "answer": "A"
        }
    ]
    random.shuffle(questions)
    score = 0

    print(f"{YELLOW}{BOLD}Mode Quiz Glam :{END}")
    for item in questions[:3]:
        print(f"\n{item['question']}")
        for choice in item['choices']:
            print(choice)
        answer = input("Ton choix (A/B/C) : ").strip().upper()
        if answer == item['answer']:
            print(f"{GREEN}Bravo ! C'est la bonne réponse.{END}")
            score += 1
        else:
            print(f"{PINK}Oups... la bonne réponse était {item['answer']}.{END}")
    return score


def pattern_puzzle():
    puzzles = [
        {
            "question": "Trouve la prochaine couleur dans cette séquence : rose, fuchsia, ... ?",
            "choices": ["A) Bleu ciel", "B) Lavande", "C) Or"],
            "answer": "B"
        },
        {
            "question": "Complète le mot mystère : _ELLE (indice : féminité)",
            "choices": ["A) BELLE", "B) POLLE", "C) SELLE"],
            "answer": "A"
        },
        {
            "question": "Si 1 sac = 2 paillettes et 2 rouge à lèvres = 1 sac, combien de paillettes pour 1 rouge à lèvres ?",
            "choices": ["A) 1", "B) 0.5", "C) 4"],
            "answer": "B"
        }
    ]
    random.shuffle(puzzles)
    score = 0

    print(f"{YELLOW}{BOLD}Mode Puzzle Sparkle :{END}")
    for item in puzzles[:3]:
        print(f"\n{item['question']}")
        for choice in item['choices']:
            print(choice)
        answer = input("Ton choix (A/B/C) : ").strip().upper()
        if answer == item['answer']:
            print(f"{GREEN}Ouiii, super flair !{END}")
            score += 1
        else:
            print(f"{PINK}Non, la bonne réponse était {item['answer']}.{END}")
    return score


def smart_riddle():
    riddles = [
        {
            "question": "Je suis légère comme une plume, mais même la plus forte des filles ne peut me tenir plus de quelques secondes. Qui suis-je ?",
            "answer": "LE SOUFFLE"
        },
        {
            "question": "Je peux être cassée sans être touchée, je peux être partagée sans être donnée. Qui suis-je ?",
            "answer": "UN SECRET"
        },
        {
            "question": "Je brille la nuit sans être une étoile. Les filles m'adorent pour ajouter du style. Qui suis-je ?",
            "answer": "LE MIROIR"
        }
    ]
    random.shuffle(riddles)
    score = 0

    print(f"{YELLOW}{BOLD}Mode Smart Challenge :{END}")
    for item in riddles[:3]:
        print(f"\n{item['question']}")
        answer = input("Ta réponse : ").strip().upper()
        if answer == item['answer']:
            print(f"{GREEN}Tellement intelligent !{END}")
            score += 1
        else:
            print(f"{PINK}Pas mal, mais la bonne réponse était : {item['answer']}.{END}")
    return score


def display_result(score, total):
    print(f"\n{BLUE}{BOLD}Score final : {score}/{total}{END}")
    if score == total:
        print(f"{PINK}Incroyable ! Tu es une reine du glamour et du cerveau !{END}")
    elif score >= total - 1:
        print(f"{GREEN}Superbe score, tu brilles comme une star !{END}")
    else:
        print(f"{YELLOW}On garde le fun et on recommence ? Tu as tout ce qu'il faut pour gagner.{END}")


def main():
    display_title()
    print(f"{PINK}Choisis ton niveau de folie :{END}")
    print("1) Quiz Glam + Smart")
    print("2) Puzzle Sparkle + Brain")
    print("3) Challenge Smart + Fun")
    print("4) Tout en mode party")
    print("5) Quitter")

    choix = input("Ton choix : ").strip()
    if choix == "1":
        score = question_quiz()
        display_result(score, 3)
    elif choix == "2":
        score = pattern_puzzle()
        display_result(score, 3)
    elif choix == "3":
        score = smart_riddle()
        display_result(score, 3)
    elif choix == "4":
        total_score = 0
        total_score += question_quiz()
        total_score += pattern_puzzle()
        total_score += smart_riddle()
        display_result(total_score, 9)
    elif choix == "5":
        print(f"{BLUE}À bientôt, princesse du code !{END}")
        sys.exit(0)
    else:
        print(f"{PINK}Choix invalide. On réessaie ?{END}")


if __name__ == "__main__":
    main()
