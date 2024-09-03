import tkinter as tk
import pandas as pd
import random

# Load data
data = pd.read_csv("data/french_words.csv")
french_words = data["French"].tolist()
english_words = data["English"].tolist()

def next_card():
    """Display the next French word and schedule card flip."""
    global current_french_word, current_french_word_index
    current_french_word = random.choice(french_words)
    current_french_word_index = french_words.index(current_french_word)
    update_card("French", current_french_word, "black")
    window.after(3000, flip_card)

def flip_card():
    """Flip the card to show the English translation."""
    update_card("English", english_words[current_french_word_index], "white")

def update_card(title, word, color):
    """Update card title, word, and color."""
    canvas.itemconfig(title_id, text=title, fill=color)
    canvas.itemconfig(word_id, text=word, fill=color)
    canvas.itemconfig(card_img, image=card_back_img if color == "white" else card_front_img)

def mark_as_known():
    """Mark the current word as known and remove it from the list."""
    try:
        with open("data/letters_to_learn.csv", mode="a") as file:
            file.write(f"{current_french_word},{english_words[current_french_word_index]}\n")
        french_words.remove(current_french_word)
        english_words.pop(current_french_word_index)
    except ValueError:
        pass
    finally:
        next_card()

def mark_as_unknown():
    """Mark the current word as unknown and show the next card."""
    next_card()

# UI Setup
BACKGROUND_COLOR = "#B1DDC6"
window = tk.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Load images
card_front_img = tk.PhotoImage(file="images/card_front.png")
card_back_img = tk.PhotoImage(file="images/card_back.png")

# Canvas
canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_img = canvas.create_image(400, 263, image=card_front_img)
title_id = canvas.create_text(400, 150, text="title", font=("Arial", 40, "italic"))
word_id = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
right_img = tk.PhotoImage(file="images/right.png")
right_button = tk.Button(image=right_img, highlightthickness=0, command=mark_as_known)
right_button.grid(row=1, column=0)

wrong_img = tk.PhotoImage(file="images/wrong.png")
wrong_button = tk.Button(image=wrong_img, highlightthickness=0, command=mark_as_unknown)
wrong_button.grid(row=1, column=1)

# Start with the first card
next_card()

window.mainloop()
