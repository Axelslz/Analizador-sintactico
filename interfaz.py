# interfaz.py
from tkinter import *
from tkinter import scrolledtext
from analizador import analizar_entrada

class Interfaz:
    def __init__(self, root):
        self.root = root
        self.root.title("Analizador Sintáctico")
        self.root.geometry("800x600")

        self.text_area = scrolledtext.ScrolledText(root, wrap=WORD)
        self.text_area.pack(expand=YES, fill=BOTH)

        boton_analizar = Button(root, text="Analizar", command=self.analizar)
        boton_analizar.pack()

    def analizar(self):
        entrada = self.text_area.get("1.0", END)
        resultado = analizar_entrada(entrada)
        print(resultado)  # Puedes hacer lo que desees con el resultado

if __name__ == "__main__":
    root = Tk()
    interfaz = Interfaz(root)
    root.mainloop()
