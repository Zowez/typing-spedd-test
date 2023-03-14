from tkinter import *
from tkinter import messagebox
from random import *

BG = "#B7EAFA"
BG2 = "#FAF7D3"
dictionary = []
user_words = []
showed_words = []
wpm = 0
cpm = 0

def start():
    global dictionary, user_words, showed_words, wpm, cpm
    dictionary = []
    user_words = []
    showed_words = []
    wpm = 0
    cpm = 0
    start_timer()
    display_words()
    entry.config(state="normal")
    button.config(text="Restart")
    pass


def start_timer():
    if window.after_id is not None:
        window.after_cancel(window.after_id)
    count_down(60)


def count_down(c):
    if c > 0:
        window.after_id = window.after(1000, count_down, c - 1)
    else:
        window.after_id = None
    if c == 0:
        finish()
        window.bind("<Return>", start)
    timer_label.config(text=f"Time Left: {c}")


def finish():
    entry.config(state="disabled")
    compare()
    if messagebox.askyesno(title="Here is your score", message=f"WPM = {wpm}\nCPM = {cpm}\nDo you wanna try again?"):
        start()
    else:
        window.destroy()


def user_input(event):
    if len(entry.get().replace(" ", "")) > 0:
        user_words.append(entry.get().replace(" ", ""))
        entry.delete(0, "end")
        showed_words.append(dictionary[-1])
        text_area.config(state="normal")
        text_area.delete("0.1", f"1.{len(dictionary.pop()) + 4}")
        text_area.config(state="disabled")


def compare():
    global wpm, cpm
    for words in user_words:
        if words in showed_words:
            wpm += 1
            cpm += len(words)


def display_words():
    with open("words.txt") as file:

        lines = file.readlines()
        for line in lines:
            dictionary.append(line.replace("\n", ""))

        shuffle(dictionary)

    for words in dictionary:
        text_area.config(state="normal")
        text_area.insert("1.0", f"{words}    ")
        text_area.config(state="disabled")


window = Tk()
window.title("Typing Speed Test")
window.config(padx=50, pady=50, background=BG)
window.after_id = None
window.bind("<space>", user_input)
window.bind("<Return>", user_input)

title = Label(text="Typing Speed Test", background=BG, font=("Agency FB", 40), pady=20)
title.grid(row=0, column=0)

timer_label = Label(text="Time Left:", background=BG, font=("Agency FB", 40), pady=20)
timer_label.grid(row=0, column=2)

text_area = Text(background=BG2, font=("Agency FB", 40), width=50, height=2, state="disabled", padx=20, pady=20)
text_area.grid(row=1, columnspan=3)

entry = Entry(window, background=BG2, font=("Agency FB", 40), justify="center", state="disabled")
entry.focus()
entry.grid(row=2, columnspan=3, pady=10)

button = Button(window, text="Start", background=BG2, font=("Agency FB", 40), justify="center", command=start)
button.grid(row=3, columnspan=3)

window.mainloop()
