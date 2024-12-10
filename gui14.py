
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\aliam\OneDrive\Desktop\build\assets\frame14")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1526x825")
window.configure(bg = "#9F7AC6")


canvas = Canvas(
    window,
    bg = "#9F7AC6",
    height = 825,
    width = 1526,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    169.0,
    88.0,
    anchor="nw",
    text="What is the Anti-derrivative of Cos(x)",
    fill="#000000",
    font=("Inter", 48 * -1)
)

canvas.create_text(
    146.0,
    242.0,
    anchor="nw",
    text="A. Cos^-1(x)",
    fill="#000000",
    font=("Inter", 48 * -1)
)

canvas.create_text(
    146.0,
    412.0,
    anchor="nw",
    text="B. Tan(x)",
    fill="#000000",
    font=("Inter", 48 * -1)
)

canvas.create_text(
    146.0,
    566.0,
    anchor="nw",
    text="C. -Sin(x)",
    fill="#000000",
    font=("Inter", 48 * -1)
)
window.resizable(False, False)
window.mainloop()