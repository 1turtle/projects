from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image


root = Tk()
root.title("HEIC Viewer")
frm = ttk.Frame(root, padding=10)
frm.grid()

img = ImageTk.PhotoImage(Image.open('test.png'))
ttk.Label(frm, image=img).grid(column=0, row=0)

'''
Unused code for a dropdown menu for file formats
ttk.Label(frm, text="New File Format").grid(column=0,row=1)
img_formats = ['jpeg', 'png', 'pdf']
default_img_format = StringVar(value=img_formats[0])
img_formats_options = ttk.OptionMenu(frm, default_img_format, img_formats[0], *img_formats)
img_formats_options.grid(column=1,row=1)
'''

ttk.Button(frm, text="Save As", command="").grid(column=0, row=1)

root.mainloop()

print("Success!")