import random
import tkinter as tk
import customtkinter as ctk
from PIL import Image
from english_words import get_english_words_set


hangman0 = ctk.CTkImage(Image.open("hangman/0.png"), size=(350, 350))
hangman1 = ctk.CTkImage(Image.open("hangman/1.png"), size=(350, 350))
hangman2 = ctk.CTkImage(Image.open("hangman/2.png"), size=(350, 350))
hangman3 = ctk.CTkImage(Image.open("hangman/3.png"), size=(350, 350))
hangman4 = ctk.CTkImage(Image.open("hangman/4.png"), size=(350, 350))
hangman5 = ctk.CTkImage(Image.open("hangman/5.png"), size=(350, 350))
hangman6 = ctk.CTkImage(Image.open("hangman/6.png"), size=(350, 350))

window = ctk.CTk()
ctk.set_appearance_mode("light")
window.title("Hangman")
window.geometry("800x500")
window.resizable(False, False)
canvas = ctk.CTkCanvas(window, bg="black", width=800, height=500)
canvas.pack()
background = tk.PhotoImage(file="hangman/board.png")
canvas.create_image(400, 250, image=background)
hangman_img = ctk.CTkLabel(window, text="", image=hangman0, bg_color="#0a3a00")
hangman_img.place(x=50, y=18)


class buttons():
    hata = 0
    word = get_english_words_set(['web2'], lower=False)
    word_list = list(word)
    secim = random.choice(word_list).upper()
    while not ((len(secim) > 3) and (len(secim) < 8)):
        secim = random.choice(word_list).upper()
    secim2 = secim
    cizgi = ""
    for i in secim:
        cizgi += "_ "
    label = ctk.CTkLabel(window, text=cizgi, font=("Noto Sans CJK JP", 40, "bold"), bg_color="#0a3a00", text_color="white")
    label.place(x=450, y=180)

    def __init__(self, letter, x, y):
        self.letter = letter
        self.x = x
        self.y = y
        self.create()


    def create(self):
        self.button = ctk.CTkButton(window,
                                    text=self.letter,
                                    bg_color="#0a3a00",
                                    width=50,
                                    corner_radius=10,
                                    font=("Noto Sans CJK JP", 30, "bold"),
                                    fg_color="#8EC3B0",
                                    hover_color="#5c7d71",
                                    state="normal",
                                    command=self.yap)
        self.button.place(x=self.x, y=self.y)


    def yap(self):
        self.button.configure(state="disabled")
        if self.letter not in buttons.secim2:
            buttons.hata += 1

        if buttons.hata == 0:
            hangman_img.configure(image=hangman0)
        elif buttons.hata == 1:
            hangman_img.configure(image=hangman1)
        elif buttons.hata == 2:
            hangman_img.configure(image=hangman2)
        elif buttons.hata == 3:
            hangman_img.configure(image=hangman3)
        elif buttons.hata == 4:
            hangman_img.configure(image=hangman4)
        elif buttons.hata == 5:
            hangman_img.configure(image=hangman5)
        elif buttons.hata == 6:
            hangman_img.configure(image=hangman6)

        if buttons.hata == 6:
            buttons.label.place_forget()
            lose_label = ctk.CTkLabel(window, text="You Lose!", font=("Noto Sans CJK JP", 40, "bold"), bg_color="#0a3a00", text_color="red")
            lose_label.place(x=450, y=180)

        if self.letter in buttons.secim2:
            while self.letter in buttons.secim2:
                index = int(buttons.secim2.index(self.letter))
                buttons.secim2 = buttons.secim2[:index] + "_" + buttons.secim2[(index + 1):]
                index2 = index * 2
                buttons.cizgi = buttons.cizgi[:index2] + self.letter + buttons.cizgi[(index2+1):]

        buttons.label.configure(text=buttons.cizgi)

        if buttons.hata < 6 and "_" not in buttons.cizgi:
            buttons.label.place_forget()
            win_label = ctk.CTkLabel(window, text="You Win!", font=("Noto Sans CJK JP", 40, "bold"), bg_color="#0a3a00", text_color="green")
            win_label.place(x=450, y=180)


buttons("A", 47, 374)
buttons("B", 102, 374)
buttons("C", 157, 374)
buttons("D", 212, 374)
buttons("E", 267, 374)
buttons("F", 323, 374)
buttons("G", 377, 374)
buttons("H", 432, 374)
buttons("I", 487, 374)
buttons("J", 542, 374)
buttons("K", 597, 374)
buttons("L", 652, 374)
buttons("M", 707, 374)

buttons("N", 47, 420)
buttons("O", 102, 420)
buttons("P", 157, 420)
buttons("Q", 212, 420)
buttons("R", 267, 420)
buttons("S", 323, 420)
buttons("T", 377, 420)
buttons("U", 432, 420)
buttons("V", 487, 420)
buttons("W", 542, 420)
buttons("X", 597, 420)
buttons("Y", 652, 420)
buttons("Z", 707, 420)

print(buttons.secim)

window.mainloop()
