import tkinter as tk
import random

dice = {
    1: "⚀",
    2: "⚁",
    3: "⚂",
    4: "⚃",
    5: "⚄",
    6: "⚅"
}


def roll_dice():
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)

    dice1.config(text=dice[d1])
    dice2.config(text=dice[d2])

    total.config(text=f"Total = {d1 + d2}")

    if d1 + d2 == 12:
        result.config(text="🎉 Jackpot! You got 12")
    else:
        result.config(text="")


root = tk.Tk()
root.title("Dice Rolling Game")
root.geometry("400x450")
root.config(bg="white")

title = tk.Label(root, text="DICE ROLLING GAME",
                font=("Arial", 20, "bold"),
                bg="white")
title.pack(pady=15)


frame = tk.Frame(root, bg="white")
frame.pack()

dice1 = tk.Label(frame, text="⚀", font=("Arial", 80), bg="white")
dice1.grid(row=0, column=0, padx=20)

dice2 = tk.Label(frame, text="⚀", font=("Arial", 80), bg="white")
dice2.grid(row=0, column=1, padx=20)

btn = tk.Button(root, text="ROLL DICE",
                font=("Arial", 14, "bold"),
                bg="blue", fg="white",
                command=roll_dice)
btn.pack(pady=20)

total = tk.Label(root, text="Total = 0",
                font=("Arial", 18),
                bg="white")
total.pack()

result = tk.Label(root, text="",
                font=("Arial", 16, "bold"),
                fg="green",
                bg="white")
result.pack(pady=10)

exit_button = tk.Button(root, text="Exit", command=root.destroy)
exit_button.pack(pady=10)

root.mainloop()
