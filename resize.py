from PIL import Image
import tkinter as tk
from tkinter import filedialog

def resize(event=None):
    filename = filedialog.askopenfile()
    print(filename)
    image = Image.open(filename.name)
    image = image.convert("RGB")
    new_image = image.resize((20, 5))
    new_image.save('image.jpg')

window = tk.Tk()
window.geometry("500x500")
button = tk.Button(window, text='upload', command=resize)
button.pack()

window.mainloop()


