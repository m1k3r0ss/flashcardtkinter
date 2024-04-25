from tkinter import Tk, Canvas, PhotoImage, Menu, messagebox
from tkmacosx import CircleButton
import json
import random

word_meaning = {}
current_lang = ""
BACKGROUND_COLOR = "#B1DDC6"
words = []  # Initialize words list
count = 0
right = -1
wrong = 0


def start_flash(file_path, lang):
    global words, current_lang
    current_lang = lang
    with open(file_path, mode="r") as data:
        words = json.load(data)[lang]


def next_word(button_id):
    global word_meaning, count
    try:
        if not words:
            raise ValueError("Please select a language first.")
        word_meaning = random.choice(words)  # Choose a random word from the words list
        show_word()
        # Check if the "wrong" button (button_id = 1) was clicked
        if button_id == 1:
            # Append the weak word to the text file
            with open("weak_words.txt", mode="a", encoding="utf-8") as text_file:
                for word, translations in word_meaning.items():
                    text_file.write(f"{word}, {translations['romaji']}, {translations['english']}\n")
    except ValueError as e:
        messagebox.showerror("Error", str(e))



def show_word():
    global word_meaning, current_lang, flip_timer
    root.after_cancel(flip_timer)
    canvas.itemconfig(card, image=front)
    for each_word, translations in word_meaning.items():
        canvas.itemconfig(language, text=current_lang, fill="black")
        canvas.itemconfig(word, text=each_word, fill="black")
        canvas.itemconfig(romaji, text=translations['romaji'], fill="black")
    flip_timer = root.after(3000, func=flip_card)


def flip_card():
    global word_meaning
    if current_lang != "":
        canvas.itemconfig(card, image=back)
        canvas.itemconfig(language, text="english", fill="white")
        for each_word, translations in word_meaning.items():
            canvas.itemconfig(word, text=translations["english"], fill="white")
        canvas.itemconfig(romaji, text="")


# Menu Bar Functions
def sel_japanese():
    file_path = "data/japanese.json"
    start_flash(file_path, "japanese")


def sel_french():
    file_path = "data/french.json"
    start_flash(file_path, "french")


def sel_german():
    file_path = "data/german.json"
    start_flash(file_path, "german")


root = Tk()
root.title("Flash Card")
flip_timer = root.after(3000, func=flip_card)

# Menu Bar
menu_bar = Menu(root)
root.config(padx=50, pady=50, bg=BACKGROUND_COLOR, menu=menu_bar)
language_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Language", menu=language_menu)

language_menu.add_command(label="French", command=sel_french)
language_menu.add_command(label="Japanese", command=sel_japanese)
language_menu.add_command(label="German", command=sel_german)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front = PhotoImage(file="images/card_front.png")
back = PhotoImage(file="images/card_back.png")
card = canvas.create_image(400, 263, image=front)
language = canvas.create_text(400, 150, text="Language", font=("Ariel", 40, "italic"), fill="black")
word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"), fill="black")
romaji = canvas.create_text(400, 376, text="/prəˌnʌnsɪˈeɪʃn/", font=("Ariel", 30, "italic"), fill="black")
canvas.grid(column=0, row=0, columnspan=2)

right_button_photo = PhotoImage(file="images/right.png")
right_button = CircleButton(image=right_button_photo, highlightthickness=0, borderless=True, bg=BACKGROUND_COLOR, bd=0,
                            highlightcolor=BACKGROUND_COLOR, radius=50, command=lambda: next_word(0))
right_button.grid(column=1, row=1)

left_button_photo = PhotoImage(file="images/wrong.png")
left_button = CircleButton(image=left_button_photo, highlightthickness=0, borderless=True, bg=BACKGROUND_COLOR, bd=0,
                           highlightcolor=BACKGROUND_COLOR, radius=50, command=lambda: next_word(1))
left_button.grid(column=0, row=1, padx=0)

root.mainloop()
