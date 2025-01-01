import tkinter as tk
import random
from tkinter import messagebox

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        master.title("Number Guessing Game")

        self.label = tk.Label(master, text="Guess the number!", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.range_label = tk.Label(master, text="Set Range:", font=("Helvetica", 14))
        self.range_label.pack()
        self.lower_bound_label = tk.Label(master, text="Lower Bound:", font=("Helvetica", 12))
        self.lower_bound_label.pack()
        self.lower_bound_entry = tk.Entry(master, font=("Helvetica", 12))
        self.lower_bound_entry.pack(pady=5)
        self.upper_bound_label = tk.Label(master, text="Upper Bound:", font=("Helvetica", 12))
        self.upper_bound_label.pack()
        self.upper_bound_entry = tk.Entry(master, font=("Helvetica", 12))
        self.upper_bound_entry.pack(pady=5)

        self.set_range_button = tk.Button(master, text="Set Range", command=self.set_range, font=("Helvetica", 12), bg="light blue")
        self.set_range_button.pack(pady=10)

        self.guess_label = tk.Label(master, text="Enter your guess:", font=("Helvetica", 14))
        self.guess_label.pack()
        self.guess_entry = tk.Entry(master, font=("Helvetica", 12))
        self.guess_entry.pack(pady=5)

        self.submit_button = tk.Button(master, text="Submit", command=self.check_guess, font=("Helvetica", 12), bg="light green")
        self.submit_button.pack(pady=10)

        self.feedback_label = tk.Label(master, text="", font=("Helvetica", 14))
        self.feedback_label.pack(pady=5)

        self.previous_guesses_label = tk.Label(master, text="Previous guesses: None", font=("Helvetica", 12))
        self.previous_guesses_label.pack(pady=5)

        self.new_game_button = tk.Button(master, text="Play Again", command=self.new_game, font=("Helvetica", 12), bg="orange")
        self.new_game_button.pack(pady=10)
        self.new_game_button.config(state="disabled")

        self.number_to_guess = None
        self.attempts = 0
        self.previous_guesses = []

    def set_range(self):
        try:
            self.lower_bound = int(self.lower_bound_entry.get())
            self.upper_bound = int(self.upper_bound_entry.get())
            if self.lower_bound >= self.upper_bound:
                raise ValueError("Lower bound must be less than upper bound.")
            self.number_to_guess = random.randint(self.lower_bound, self.upper_bound)
            self.attempts = 0
            self.previous_guesses = []
            self.feedback_label.config(text="Range set! Start guessing.")
            self.lower_bound_entry.config(state="disabled")
            self.upper_bound_entry.config(state="disabled")
            self.set_range_button.config(state="disabled")
            self.new_game_button.config(state="normal")
            self.previous_guesses_label.config(text="Previous guesses: None")
        except ValueError as e:
            messagebox.showerror("Invalid Input", f"Error: {e}")

    def check_guess(self):
        try:
            guess = int(self.guess_entry.get())
            self.attempts += 1
            self.previous_guesses.append(guess)
            self.previous_guesses_label.config(text=f"Previous guesses: {', '.join(map(str, self.previous_guesses))}")
            
            if guess < self.number_to_guess:
                self.feedback_label.config(text="Too low!", fg="blue")
                self.guess_entry.delete(0, tk.END)  # Clear the input field
            elif guess > self.number_to_guess:
                self.feedback_label.config(text="Too high!", fg="blue")
                self.guess_entry.delete(0, tk.END)  # Clear the input field
            else:
                self.feedback_label.config(text=f"Congratulations! You've guessed the correct number in {self.attempts} attempts.", fg="green", bg="yellow")
                self.new_game_button.config(state="normal")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")
            self.guess_entry.delete(0, tk.END)  # Clear the input field on error

    def new_game(self):
        self.lower_bound_entry.config(state="normal")
        self.upper_bound_entry.config(state="normal")
        self.set_range_button.config(state="normal")
        self.feedback_label.config(text="", bg="SystemButtonFace")
        self.guess_entry.delete(0, tk.END)
        self.lower_bound_entry.delete(0, tk.END)
        self.upper_bound_entry.delete(0, tk.END)
        self.new_game_button.config(state="disabled")
        self.previous_guesses_label.config(text="Previous guesses: None")

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
