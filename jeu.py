import random
import tkinter as tk
from tkinter import messagebox


class GlamBrainPartyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Glam Brain Party")
        self.geometry("900x650")
        self.configure(bg="#fff0f8")
        self.resizable(False, False)

        self.theme = {
            "background": "#fff0f8",
            "panel": "#ffe4f5",
            "button": "#ffb6d2",
            "button_hover": "#ff8fcf",
            "text": "#5b2c6f",
            "accent": "#f7a6d6",
        }

        self.modes = {
            "Quiz Glam": self.create_quiz_questions,
            "Puzzle Sparkle": self.create_puzzle_questions,
            "Smart Challenge": self.create_riddle_questions,
            "Party Total": self.create_all_questions,
        }

        self.current_questions = []
        self.score = 0
        self.question_index = 0
        self.max_score = 0

        self.create_widgets()

    def create_widgets(self):
        self.title_frame = tk.Frame(self, bg=self.theme["background"])
        self.title_frame.pack(fill="x", pady=20)

        title_label = tk.Label(
            self.title_frame,
            text="GLAM BRAIN PARTY",
            font=("Helvetica", 36, "bold"),
            fg=self.theme["text"],
            bg=self.theme["background"],
        )
        title_label.pack()

        subtitle_label = tk.Label(
            self.title_frame,
            text="Un jeu girly, fun et un peu smart avec un design de fou !",
            font=("Helvetica", 16),
            fg=self.theme["text"],
            bg=self.theme["background"],
        )
        subtitle_label.pack(pady=(8, 24))

        self.card_frame = tk.Frame(self, bg=self.theme["panel"], bd=2, relief="groove")
        self.card_frame.pack(padx=40, pady=10, fill="both", expand=True)

        self.dashboard_label = tk.Label(
            self.card_frame,
            text="Choisis ton mode :",
            font=("Helvetica", 22, "bold"),
            fg=self.theme["text"],
            bg=self.theme["panel"],
        )
        self.dashboard_label.pack(pady=20)

        self.button_frame = tk.Frame(self.card_frame, bg=self.theme["panel"])
        self.button_frame.pack(pady=10)

        for mode in self.modes:
            button = tk.Button(
                self.button_frame,
                text=mode,
                font=("Helvetica", 14, "bold"),
                bg=self.theme["button"],
                fg="white",
                activebackground=self.theme["button_hover"],
                width=18,
                height=2,
                command=lambda name=mode: self.start_mode(name),
                bd=0,
                highlightthickness=0,
            )
            button.pack(padx=10, pady=10)

        self.exit_button = tk.Button(
            self.card_frame,
            text="Quitter",
            font=("Helvetica", 12, "bold"),
            bg="#ff8fb1",
            fg="white",
            activebackground="#ff6f9f",
            width=12,
            command=self.on_exit,
            bd=0,
            highlightthickness=0,
        )
        self.exit_button.pack(pady=(24, 16))

    def start_mode(self, mode_name):
        self.score = 0
        self.question_index = 0
        self.current_questions = self.modes[mode_name]()
        self.max_score = len(self.current_questions)
        self.show_question_screen(mode_name)

    def show_question_screen(self, mode_name):
        self.clear_screen()

        header = tk.Label(
            self.card_frame,
            text=f"Mode : {mode_name}",
            font=("Helvetica", 24, "bold"),
            fg=self.theme["text"],
            bg=self.theme["panel"],
        )
        header.pack(pady=14)

        self.question_label = tk.Label(
            self.card_frame,
            text="",
            font=("Helvetica", 20),
            fg=self.theme["text"],
            bg=self.theme["panel"],
            wraplength=780,
            justify="center",
        )
        self.question_label.pack(pady=(16, 24))

        self.answer_frame = tk.Frame(self.card_frame, bg=self.theme["panel"])
        self.answer_frame.pack(pady=10)

        self.next_button = tk.Button(
            self.card_frame,
            text="Suivant",
            font=("Helvetica", 14, "bold"),
            bg=self.theme["button"],
            fg="white",
            activebackground=self.theme["button_hover"],
            width=14,
            command=self.next_question,
            bd=0,
            highlightthickness=0,
            state="disabled",
        )
        self.next_button.pack(pady=(18, 10))

        self.feedback_label = tk.Label(
            self.card_frame,
            text="",
            font=("Helvetica", 14, "italic"),
            fg="#8a2be2",
            bg=self.theme["panel"],
        )
        self.feedback_label.pack(pady=(8, 8))

        self.load_question()

    def load_question(self):
        question_data = self.current_questions[self.question_index]
        self.question_label.config(text=question_data["question"])

        for widget in self.answer_frame.winfo_children():
            widget.destroy()

        self.user_answer = tk.StringVar(value="")
        if question_data.get("choices"):
            for choice in question_data["choices"]:
                button = tk.Button(
                    self.answer_frame,
                    text=choice,
                    font=("Helvetica", 14),
                    bg="white",
                    fg=self.theme["text"],
                    activebackground=self.theme["button_hover"],
                    width=26,
                    pady=8,
                    command=lambda c=choice: self.select_answer(c),
                    bd=0,
                    highlightthickness=0,
                )
                button.pack(pady=6)
        else:
            self.answer_entry = tk.Entry(
                self.answer_frame,
                font=("Helvetica", 16),
                width=32,
                bd=3,
                relief="ridge",
            )
            self.answer_entry.pack(pady=10)
            self.answer_entry.focus()

            submit = tk.Button(
                self.answer_frame,
                text="Valider",
                font=("Helvetica", 14, "bold"),
                bg=self.theme["button"],
                fg="white",
                activebackground=self.theme["button_hover"],
                width=12,
                command=self.submit_text_answer,
                bd=0,
                highlightthickness=0,
            )
            submit.pack(pady=10)

    def select_answer(self, choice):
        self.user_answer.set(choice.split(") ", 1)[0])
        self.evaluate_answer()

    def submit_text_answer(self):
        self.user_answer.set(self.answer_entry.get().strip().upper())
        self.evaluate_answer()

    def evaluate_answer(self):
        question_data = self.current_questions[self.question_index]
        correct_answer = question_data["answer"].upper()
        answer_value = self.user_answer.get().strip().upper()

        if answer_value == correct_answer:
            self.feedback_label.config(text="Bravo ! Tu as trouvé la bonne réponse.", fg="#2e8b57")
            self.score += 1
        else:
            self.feedback_label.config(
                text=f"Ooops... la bonne réponse était : {question_data['answer']}",
                fg="#c71585",
            )
        self.next_button.config(state="normal")
        for child in self.answer_frame.winfo_children():
            child.config(state="disabled")

    def next_question(self):
        self.question_index += 1
        if self.question_index >= len(self.current_questions):
            self.show_result_screen()
            return
        self.next_button.config(state="disabled")
        self.feedback_label.config(text="")
        self.load_question()

    def show_result_screen(self):
        self.clear_screen()

        result_label = tk.Label(
            self.card_frame,
            text=f"Ton score final : {self.score} / {self.max_score}",
            font=("Helvetica", 28, "bold"),
            fg=self.theme["text"],
            bg=self.theme["panel"],
        )
        result_label.pack(pady=30)

        if self.score == self.max_score:
            message = "Incroyable ! Tu es une reine du glamour et du cerveau !"
        elif self.score >= self.max_score - 1:
            message = "Superbe score, tu brilles comme une star !"
        else:
            message = "On garde le fun et on recommence ? Tu as tout ce qu'il faut pour gagner."

        summary_label = tk.Label(
            self.card_frame,
            text=message,
            font=("Helvetica", 18),
            fg="#4b0082",
            bg=self.theme["panel"],
            wraplength=760,
            justify="center",
        )
        summary_label.pack(padx=20, pady=20)

        replay_button = tk.Button(
            self.card_frame,
            text="Rejouer",
            font=("Helvetica", 14, "bold"),
            bg=self.theme["button"],
            fg="white",
            activebackground=self.theme["button_hover"],
            width=14,
            command=self.reset_app,
            bd=0,
            highlightthickness=0,
        )
        replay_button.pack(pady=(20, 10))

        quit_button = tk.Button(
            self.card_frame,
            text="Retour au menu",
            font=("Helvetica", 14, "bold"),
            bg="#ff8fb1",
            fg="white",
            activebackground="#ff6f9f",
            width=16,
            command=self.reset_app,
            bd=0,
            highlightthickness=0,
        )
        quit_button.pack(pady=(6, 20))

    def reset_app(self):
        self.clear_screen()
        self.create_widgets()

    def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.card_frame = tk.Frame(self, bg=self.theme["panel"], bd=2, relief="groove")
        self.card_frame.pack(padx=40, pady=10, fill="both", expand=True)

    def create_quiz_questions(self):
        questions = [
            {
                "question": "Quel accessoire est généralement associé à un look girly ?",
                "choices": ["A) Un sac pailleté", "B) Des bottes de pluie", "C) Un casque de vélo"],
                "answer": "A",
            },
            {
                "question": "Quelle couleur est souvent appelée 'rose poupée' ?",
                "choices": ["A) Émeraude", "B) Fuchsia", "C) Indigo"],
                "answer": "B",
            },
            {
                "question": "Quel animal est souvent associé à la douceur et à la magie girly ?",
                "choices": ["A) Licorne", "B) Chèvre", "C) Crocodile"],
                "answer": "A",
            },
        ]
        random.shuffle(questions)
        return questions

    def create_puzzle_questions(self):
        puzzles = [
            {
                "question": "Complète le mot mystère : _ELLE (indice : féminité)",
                "choices": ["A) BELLE", "B) POLLE", "C) SELLE"],
                "answer": "A",
            },
            {
                "question": "Trouve la couleur suivante : rose, fuchsia, ... ?",
                "choices": ["A) Bleu ciel", "B) Lavande", "C) Or"],
                "answer": "B",
            },
            {
                "question": "Si 1 sac = 2 paillettes et 2 rouges à lèvres = 1 sac, combien de paillettes pour 1 rouge à lèvres ?",
                "choices": ["A) 1", "B) 0.5", "C) 4"],
                "answer": "B",
            },
        ]
        random.shuffle(puzzles)
        return puzzles

    def create_riddle_questions(self):
        riddles = [
            {
                "question": "Je suis légère comme une plume, mais même la plus forte ne peut me tenir plus de quelques secondes. Qui suis-je ?",
                "answer": "LE SOUFFLE",
            },
            {
                "question": "Je peux être cassée sans être touchée, je peux être partagée sans être donnée. Qui suis-je ?",
                "answer": "UN SECRET",
            },
            {
                "question": "Je brille la nuit sans être une étoile et j'aide à ajouter du style. Qui suis-je ?",
                "answer": "LE MIROIR",
            },
        ]
        random.shuffle(riddles)
        return riddles

    def create_all_questions(self):
        return self.create_quiz_questions() + self.create_puzzle_questions() + self.create_riddle_questions()

    def on_exit(self):
        if messagebox.askyesno("Quitter", "Voulez-vous quitter Glam Brain Party ?"):
            self.destroy()


if __name__ == "__main__":
    app = GlamBrainPartyApp()
    app.mainloop()
