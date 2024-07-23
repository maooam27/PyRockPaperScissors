import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Rock - Paper - Scissors")
        self.geometry("600x400")
        self.resizable(False, False)
        self.configure(bg="#f0f0f0")

        self.label = tk.Label(self, text="Rock - Paper - Scissors", font=("Arial", 26), fg="black", bg="#f0f0f0")
        self.label.pack(pady=20)

        self.bot_choice = tk.Entry(self, bg="white", font=("Arial", 20))
        self.bot_choice.pack(pady=10)


if __name__ == "__main__":
    app = App()
    app.mainloop()
