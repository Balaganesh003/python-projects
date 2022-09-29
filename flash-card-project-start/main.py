from tkinter import *
from pandas import *
from random import *

BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}

try:
    data = read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = read_csv("data/french_words.csv")
    to_learn = data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

french_word = ""
english_word = ""
chosen_card = ""


# choice a random word


def choose_word():
    global french_word, english_word, chosen_card, flip_timer
    window.after_cancel(flip_timer)
    chosen_card = choice(to_learn)
    english_word = chosen_card["English"]
    french_word = chosen_card["French"]
    canvas.itemconfig(front_word, text=f"{french_word}", fill="black")
    canvas.itemconfig(front_language, text="French", fill="black")
    canvas.itemconfig(image, image=front_image)
    flip_timer = window.after(3000, func=flip)


def flip():
    global english_word
    canvas.itemconfig(image, image=back_image)
    canvas.itemconfig(front_language, text="English", fill="White")
    canvas.itemconfig(front_word, text=english_word, fill="White")


def remove_word():
    to_learn.remove(chosen_card)
    choose_word()
    data_1 = DataFrame(to_learn)
    data_1.to_csv("data/words_to_learn.csv", index=False)


# ------------------------------UI SET UP-------------------------------------#
window = Tk()
window.title("game average")
window.config(padx=20, pady=20, bg="#B1DDC6")
flip_timer = window.after(3000, func=flip)
canvas = Canvas(height=530, width=800, bg="#B1DDC6", highlightthickness=0)
back_image = PhotoImage(file="images/card_back.png")
front_image = PhotoImage(file="images/card_front.png")
image = canvas.create_image(400, 265, image=front_image)
front_language = canvas.create_text(400, 200, text="Title", font=("ariel", 40))

front_word = canvas.create_text(400, 300, text="text", font=("ariel", 40))
canvas.grid(row=0, column=0, columnspan=3)

choose_word()
# correct_button
correct_image = PhotoImage(file="images/right.png")
correct_button = Button(image=correct_image, command=remove_word)
correct_button.grid(row=1, column=2)

# wrong button
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, command=choose_word)
wrong_button.grid(row=1, column=0)

window.mainloop()
