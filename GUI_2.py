import tkinter
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry("900x900")
image = Image.open("IMG_20170522_214725.jpg")
resize= image.resize((100,100))
edit = ImageTk.PhotoImage(resize)
let = tkinter.Label(image=edit)
let.pack()
root.minsize(400,400)
image2=Image.open("photo_2023-07-27_11-58-23.jpg")
resize2=image.resize((200,200))
edit2=ImageTk.PhotoImage(resize2)
let2= tkinter.Label(image=edit2)
let2.pack()
root.mainloop()
