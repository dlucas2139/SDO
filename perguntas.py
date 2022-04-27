from tkinter import *
from tkinter import *

janela = Tk()
janela.geometry("500x500")
x_pos = 0
y_pos = 0
def move(event):
    global x_pos
    global snack
    snack.destroy()
    janela.after(100)
    snack['bg'] = "#000000"
    x_pos += 5
    print (x_pos)
    pass


snack = Label(janela,width=2,height=1,bg="#FF00FF")
snack.place(x=x_pos,y=y_pos)
snack.bind("<Enter>",move)


janela.mainloop()