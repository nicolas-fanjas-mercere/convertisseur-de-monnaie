import tkinter
import json
from tkinter import *
import tkinter as tk

with open("convert.json", "r") as f:#ouvre le fichier json en mode lecture
    convert = json.load(f)#charge le fichier json

root = tk.Tk()
root.geometry("600x600+100+200")
root.resizable(False,False)

selected1 = tk.StringVar(root)#recupère les valeurs de la chaine de caractère
selected2 = tk.StringVar(root)



def converti():#fonction pour covertir
    global result
    rate = convert[selected1.get()][selected2.get()]["rate"]#variale qui est egale au ratio par rapport aux options selctionner dans les boîtes de sélections
    devise = int(entry.get())#converti notre entré en int
    result = devise * rate#mutipli le nombre par le ratio
    echo.config(text=result)#affiche le resultat dans le label plus bas


entry = Entry(root, width=50, bg='#FFFFFF', fg='#000000', font=('Arial', 16), bd=5)#notre entrée pour marquer la somme
entry.pack()

oui = Label(root, text="Devise :", font=("Arial", 16), fg="red")
oui.place(x=35, y=40)

option_menu = tk.OptionMenu(root, selected1, *convert)#notre menu déroulant pour selection notre devise
option_menu.pack()

oui2 = Label(root, text="Convertir en :", font=("Arial", 16), fg="red")
oui2.place(x=35, y=70)

option_menu = tk.OptionMenu(root, selected2, *convert)#le deuxième menu déroulant pour sélectionner en quoi la convertir
option_menu.pack()


Button(root, text="convert", width=10, height=1, font=('arial', 25, 'bold'), command=lambda: converti()).place(x=200, y=200)#le boutton qui accionne la fonction

echo = Label(root, text="",width=24, height=2, font=('arial', 30,))#la ou les calcule et les resultats font s'afficher
echo.place(x=50, y=500)

root.mainloop()