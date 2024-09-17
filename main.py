from tkinter import *
import pandas
import random
import time

BACKGROUND_COLOR = "#B1DDC6"
current_word = 0
data = pandas.read_csv("./data/french_words.csv")
data_d = data.to_dict()
english = ""
french = ""


def change_word():
    global english, french, flip_timer
    window.after_cancel(flip_timer)
    index = random.randint(0, 100)
    english = data_d["English"][index]
    french = data_d["French"][index]
    word_window.itemconfig(language, text="French")
    word_window.itemconfig(word, text=french)
    word_window.itemconfig(back_ground, image=front_photo)
    window.after(3000, func=change_lang)


def change_lang():
    word_window.itemconfig(language, text="English")
    word_window.itemconfig(word, text=english)
    word_window.itemconfig(back_ground, image=back_photo)
# ------------------------- set up --------------------------#


window = Tk()
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)
window.title("Flashy")


word_window = Canvas(width=800, height=526, bg= BACKGROUND_COLOR, highlightthickness=0)
front_photo = PhotoImage(file="./images/card_front.png")
back_photo = PhotoImage(file="./images/card_back.png")
back_ground = word_window.create_image(400, 263, image=front_photo)
word_window.grid(column=0, row=0, columnspan=2)
language = word_window.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word = word_window.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
flip_timer = window.after(3000, func=change_lang)
change_word()
right_image = PhotoImage(file="./images/right.png")
right = Button(image=right_image, highlightthickness=0, command=change_word)
right.grid(column=1, row=1)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong = Button(image=wrong_image, highlightthickness=0, command=change_word)
wrong.grid(column=0, row=1)




window.mainloop()


