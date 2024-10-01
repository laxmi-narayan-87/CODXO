import tkinter as tk
import pygame
import random

# Initialize pygame mixer
pygame.mixer.init()

# Load sound effects
correct_sound = pygame.mixer.Sound("correct-83487.mp3.crdownload")  # Add path to your correct sound file
wrong_sound = pygame.mixer.Sound("buzzer-4-183895.mp3.crdownload")      # Add path to your wrong sound file

def play_sound(sound):
    sound.play()

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    def check_guess():
        nonlocal attempts
        guess = int(entry.get())
        attempts += 1
        if guess < number_to_guess:
            result_label.config(text="Too low!")
            play_sound(wrong_sound)
        elif guess > number_to_guess:
            result_label.config(text="Too high!")
            play_sound(wrong_sound)
        else:
            result_label.config(text=f"Congratulations! You guessed the number in {attempts} attempts.")
            play_sound(correct_sound)

    # Create main window
    root = tk.Tk()
    root.title("Number Guessing Game")

    # Create and place widgets
    tk.Label(root, text="Guess a number between 1 and 100:").pack()
    entry = tk.Entry(root)
    entry.pack()
    tk.Button(root, text="Guess", command=check_guess).pack()
    result_label = tk.Label(root, text="")
    result_label.pack()

    # Run the main loop
    root.mainloop()

if __name__ == "__main__":
    guess_the_number()
