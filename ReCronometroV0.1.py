from tkinter import *
from datetime import datetime
import pyglet
pyglet.font.add_file("digital-7.ttf")

black = "#3d3d3d"
Green = "#21c25c"


j = Tk()
j.title("Rélogio digital")
j.geometry("440x180")
j.resizable(width=FALSE, height=FALSE)

j.configure(bg=black)

def relogio():
    tempo = datetime.now()

    hora = tempo.strftime("%H:%M:%S")
    ds = tempo.strftime("%A")
    dia = tempo.day
    mes = tempo.strftime('%b')
    ano = tempo.strftime("%Y")

    l1.config(text=hora)
    l1.after(200, relogio)
    l2.config(text=ds  + str(dia) + "/" + str(mes) + "/" + str(ano))

l1 = Label(j, text="", font=('digital-7 100'), bg=black, fg=Green)
l1.grid(row=0, column=0, sticky=NW, padx=5)

l2 = Label(j, text="", font=('digital-7 20'), bg=black, fg=Green)
l2.grid(row=1, column=0, sticky=NW, padx=5)


relogio()
j.mainloop()
