"""La idea de este proyecto es crear un programa que evalúe cuan rápido puedes escribir una 
oración de manera precisa. 
Este programa puede requerir crear una interfaz gráfica de usuario (GUI) mediante el módulo 
tkinter. Si eres nuevo en las GUI, este ejemplo es una buena introducción, ya que tan solo 
necesitas crear una serie de etiquetas simples, botones y campos de entrada para crear una 
ventana. Puedes usar el módulo timeit de Python para manejar el aspecto de temporización 
de nuestra prueba de escritura, y el módulo random para seleccionar aleatoriamente una frase 
de prueba."""

import tkinter as tk
import time

class TypingSpeedTest:
    def __init__(self, master):
        self.master = master
        self.master.title("Prueba de Velocidad de Escritura")
        
        self.phrases = [
            "El rápido zorro marrón salta sobre el perro perezoso.",
            "La vida es como una caja de chocolates, nunca sabes lo que te va a tocar.",
            "Python es un lenguaje de programación versátil y poderoso.",
            "La práctica hace al maestro en cualquier habilidad que desees aprender."
        ]
        
        self.current_phrase = ""
        self.start_time = 0
        
        self.label = tk.Label(master, text="Presiona 'Iniciar' para comenzar la prueba.")
        self.label.pack(pady=10)
        
        self.text_entry = tk.Entry(master, width=50)
        self.text_entry.pack(pady=10)
        
        self.start_button = tk.Button(master, text="Iniciar", command=self.start_test)
        self.start_button.pack(pady=5)
        
        self.result_label = tk.Label(master, text="")
        self.result_label.pack(pady=10)
    
    def start_test(self):
        import random
        self.current_phrase = random.choice(self.phrases)
        self.label.config(text=self.current_phrase)
        self.text_entry.delete(0, tk.END)
        self.start_time = time.time()
        self.text_entry.focus()
        self.text_entry.bind('<Return>', self.check_result)
    
    def check_result(self, event):
        end_time = time.time()
        elapsed_time = end_time - self.start_time
        user_input = self.text_entry.get()
        
        if user_input == self.current_phrase:
            wpm = (len(user_input.split()) / elapsed_time) * 60
            self.result_label.config(text=f"Correcto! Tu velocidad es {wpm:.2f} palabras por minuto.")
        else:
            self.result_label.config(text="Incorrecto. Intenta de nuevo.")
        
        self.text_entry.unbind('<Return>')

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTest(root)
    root.mainloop()