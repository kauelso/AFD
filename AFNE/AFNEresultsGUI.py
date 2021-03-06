import tkinter as tk
import json

def to_tuple(f):
    aux = [tuple(elem) for elem in f] 
    return aux

def format_transition(t):
    convert = lambda x: str(x[3])
    aux = convert(t)
    return aux

def executar(window,contador,steps,state,label,slabel,Clabel):
    if contador[0] < len(steps):
        Clabel.config(text= f"Cadeia não lida: {steps[contador[0]][0]}")
        Clabel.update()

        label.config(text= f"Caracter: {steps[contador[0]][0][0]}  {steps[contador[0]][1]}  {steps[contador[0]][2]}")
        label.update()

        slabel.config(text = str(format_transition(steps[contador[0]])))
        slabel.update()
    else:
        statelabel = tk.Label(window,text= state)
        statelabel.pack()

    contador[0] = contador[0] + 1

def GUIstart(cadeia):

    with open('AFNE/AFNE_automata_result.json','r') as json_file:
        ADF = json.load(json_file)
    steps = to_tuple(ADF['steps'])  # Lista de tuplas executadas - [(Estado atual, simbolo, proximo estado),...]
    state = ADF['result']

    contador = [0]

    window = tk.Tk()
    window.geometry("300x300")
    frame = tk.Frame(window,width="300",height="300")
    frame.pack()
    label = tk.Label(frame,text= f"Cadeia: {cadeia}")
    label.pack()
    slabel = tk.Label(frame)
    slabel.pack()
    stlabel = tk.Label(frame)
    stlabel.pack()
    Clabel = tk.Label(frame)
    Clabel.pack()
    avancar = tk.Button(frame, text ="Avançar", command = lambda: executar(frame,contador,steps,state,slabel,stlabel,Clabel))
    avancar.pack()

    window.mainloop()




