
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\aliam\OneDrive\Desktop\build\assets\frame13")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1476x621")
window.configure(bg = "#B6F6AA")


canvas = Canvas(
    window,
    bg = "#B6F6AA",
    height = 621,
    width = 1476,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    98.0,
    33.0,
    anchor="nw",
    text="Find the most general anti-derrivative of X^2",
    fill="#000000",
    font=("Aleo Regular", 64 * -1)
)

canvas.create_text(
    175.0,
    158.0,
    anchor="nw",
    text="A. X^3",
    fill="#000000",
    font=("Aleo Regular", 64 * -1)
)

canvas.create_text(
    175.0,
    311.0,
    anchor="nw",
    text="B. X^2/2",
    fill="#000000",
    font=("Aleo Regular", 64 * -1)
)

canvas.create_text(
    204.0,
    464.0,
    anchor="nw",
    text="C. X^-2",
    fill="#000000",
    font=("Aleo Regular", 64 * -1)
)
window.resizable(False, False)
window.mainloop()
