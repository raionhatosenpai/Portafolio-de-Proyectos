'''En este proyecto utilizarás el módulo "langdetect" para ayudarnos a identificar el idioma que 
se ha ingresado. Esto puede ser realmente útil si no estás seguro de qué idioma estás 
tratando. 
Puedes crear también una GUI sencilla para interactuar con el usuario. Después puedes 
recopilar el texto del campo de entrada y procesarlo con "langdetect" para determinar qué 
idioma se ingresó. Finalmente, puedes imprimir este resultado en la GUI para informar al 
usuario sobre el resultado. 
Ten en cuenta que los resultados devueltos por "langdetect" son códigos abreviados de 
idioma. Por ejemplo, si ingresamos texto en inglés, veremos 'en' como el valor de retorno. '''

from langdetect import detect
import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext

class LanguageDetectorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Detector de Idioma")
        self.master.geometry("500x400")

        self.label = tk.Label(master, text="Ingresa el texto para detectar el idioma:", font=("Helvetica", 12))
        self.label.pack(pady=10)

        self.text_area = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=60, height=15)
        self.text_area.pack(pady=5)

        self.detect_button = tk.Button(master, text="Detectar Idioma", command=self.detect_language)
        self.detect_button.pack(pady=10)

    def detect_language(self):
        text = self.text_area.get("1.0", tk.END).strip()
        if text:
            try:
                language_code = detect(text)
                messagebox.showinfo("Resultado", f"El idioma detectado es: {language_code}")
            except Exception as e:
                messagebox.showerror("Error", "No se pudo detectar el idioma. Intenta con más texto.")
        else:
            messagebox.showwarning("Advertencia", "Por favor ingresa algún texto.")

if __name__ == "__main__":
    root = tk.Tk()
    app = LanguageDetectorApp(root)
    root.mainloop()