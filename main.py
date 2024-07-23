import random
import tkinter as tk

bets = ["rock", "paper", "scissors"]


class App(tk.Tk):
    gameStarted = False

    def play(self, bet: str):
        print(bet)
        self.choice.set(bet)

    def rock(self):
        self.play("rock")

    def paper(self):
        self.play("paper")

    def scissors(self):
        self.play("scissors")

    def __init__(self):
        super().__init__()
        self.title("Rock - Paper - Scissors")
        self.geometry("600x400")
        self.resizable(False, False)
        self.configure(bg="#f0f0f0")

        self.label = tk.Label(self, text="Rock - Paper - Scissors", font=("Arial", 28), fg="black", bg="#f0f0f0")
        self.label.pack(pady=30)

        self.choice = tk.StringVar()
        self.choice.set("place your bet")

        self.bot_choice = tk.Entry(self, bg="white", font=("Arial", 20), textvariable=self.choice, state="readonly",
                                   justify="center")
        self.bot_choice.pack(pady=10)

        # Frame for the buttons
        self.stack = tk.Frame(self, bg="#f0f0f0")
        self.stack.pack(pady=30)

        self.rock = tk.Button(self.stack, text="Rock", font=("Arial", 20), bg="white", width=5,
                              borderwidth=3, command=self.rock)
        self.rock.pack(side="left", padx=10)

        self.paper = tk.Button(self.stack, text="Paper", font=("Arial", 20), bg="white", width=5,
                               borderwidth=3, command=self.paper)
        self.paper.pack(side="left", padx=10)

        self.scissors = tk.Button(self.stack, text="Scissors", font=("Arial", 20), bg="white", width=5,
                                  borderwidth=3, command=self.scissors)
        self.scissors.pack(side="left", padx=10)


if __name__ == "__main__":
    app = App()
    app.mainloop()
