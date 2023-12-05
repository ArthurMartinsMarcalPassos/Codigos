from cProfile import label
from tkinter import * 
from time import sleep


semaforo = Tk()
semaforo.title("ola")

for i in range(1):
    sleep(0.4)
    lable_vermelho = Label(semaforo,text="teste")
    lable_vermelho["bg"] = ["red"]
    lable_vermelho.pack()

for i in range(1):
    sleep(0.4)
    lable_amarelo = Label(semaforo,text="teste")
    lable_amarelo["bg"] = ["yellow"]
    lable_amarelo.pack()

for i in range(1):
    sleep(0.4)
    lable_verde = Label(semaforo,text="teste")
    lable_verde["bg"] = ["green"]
    lable_verde.pack()
    



semaforo.mainloop()

