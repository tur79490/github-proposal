
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\aliam\OneDrive\Desktop\build\assets\frame12")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1287x632")
window.configure(bg = "#F2BBF3")


canvas = Canvas(
    window,
    bg = "#F2BBF3",
    height = 632,
    width = 1287,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    153.0,
    80.0,
    anchor="nw",
    text="Which Elemnet has the highest atomic number?",
    fill="#000000",
    font=("Inter", 48 * -1)
)

canvas.create_text(
    237.0,
    268.0,
    anchor="nw",
    text="A. Mg",
    fill="#000000",
    font=("Inter", 48 * -1)
)

canvas.create_text(
    260.0,
    409.0,
    anchor="nw",
    text="B. Au",
    fill="#000000",
    font=("Inter", 48 * -1)
)

canvas.create_text(
    921.0,
    276.0,
    anchor="nw",
    text="C. F",
    fill="#000000",
    font=("Inter", 48 * -1)
)

canvas.create_text(
    923.0,
    466.0,
    anchor="nw",
    text="D. I",
    fill="#000000",
    font=("Inter", 48 * -1)
)
window.resizable(False, False)
window.mainloop()