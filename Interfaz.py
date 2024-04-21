from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import imutils
import numpy as np
import customtkinter

def elegir_imagen():
    path_image = filedialog.askopenfilename(filetypes=[
        ("image", ".jpeg"),
        ("image", ".png"),
        ("image", ".jpg")])

    if len(path_image) > 0:
        global image
        image = cv2.imread(path_image)
        image = imutils.resize(image, height=380)

        imageToShow = imutils.resize(image, width=180)
        imageToShow = cv2.cvtColor(imageToShow, cv2.COLOR_BGR2RGB)
        im = Image.fromarray(imageToShow)
        img = ImageTk.PhotoImage(image=im)

        lblInputImage.configure(image=img)
        lblInputImage.image = img

        lblOutputImage.configure(image="")
        selected.set(0)

def filtros_imagenes(filtro):
    global image
    global lblOutputImage
    
    if image is not None:
        if filtro == 'Media':
            print(image)
            im = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
            img = ImageTk.PhotoImage(image=im)
            
            lblOutputImage.configure(image=img)
            lblOutputImage.image = img
        if filtro == 'Mediana':
            print(image)
            im = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
            img = ImageTk.PhotoImage(image=im)
            
            lblOutputImage.configure(image=img)
            lblOutputImage.image = img
        if filtro == 'Sobel':
            print(image)
            im = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
            img = ImageTk.PhotoImage(image=im)
            
            lblOutputImage.configure(image=img)
            lblOutputImage.image = img
        if filtro == 'Laplaciano':
            print(image)
            im = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
            img = ImageTk.PhotoImage(image=im)
            
            lblOutputImage.configure(image=img)
            lblOutputImage.image = img



customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
lblInputImage = Label(root)
lblInputImage.grid(column=0, row=2)

lblOutputImage = Label(root)
lblOutputImage.grid(column=1, row=1, rowspan=6)

lblInfo2 = customtkinter.CTkLabel(root, text="Filtros", width=25, corner_radius=5, fg_color='gray30')
lblInfo2.grid(column=0, row=3, padx=5, pady=5)

selected = IntVar()
rad1 = customtkinter.CTkButton(root, text='Media', width=25, command=lambda: filtros_imagenes('Media'))
rad2 = customtkinter.CTkButton(root, text='Mediana', width=25, command=lambda: filtros_imagenes('Mediana'))
rad3 = customtkinter.CTkButton(root, text='Sobel', width=25, command=lambda: filtros_imagenes('Sobel'))
rad4 = customtkinter.CTkButton(root, text='Laplaciano ', width=25, command=lambda: filtros_imagenes('Laplaciano'))
rad1.grid(column=0, row=4, pady=5)
rad2.grid(column=0, row=5, pady=5)
rad3.grid(column=0, row=6, pady=5)
rad4.grid(column=0, row=7, pady=5)

btn = customtkinter.CTkButton(root, text="Elegir imagen", width=25, command=elegir_imagen)
btn.grid(column=0, row=0, padx=5, pady=5)

root.mainloop()
