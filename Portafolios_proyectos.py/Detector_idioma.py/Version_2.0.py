from langdetect import detect
import tkinter as tk
from tkinter import messagebox, scrolledtext
import os

language_names = {
    'en': 'Inglés', 'es': 'Español', 'fr': 'Francés', 'de': 'Alemán',
    'pt': 'Portugués', 'it': 'Italiano', 'nl': 'Neerlandés', 'ru': 'Ruso',
    'zh-cn': 'Chino simplificado', 'ja': 'Japonés', 'ko': 'Coreano',
}

HISTORIAL_ARCHIVO = "historial_idiomas.txt"

class LanguageDetectorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Detector de Idioma")
        self.master.geometry("500x450")

        self.label = tk.Label(master, text="Ingresa el texto para detectar el idioma:", font=("Helvetica", 12))
        self.label.pack(pady=10)

        self.text_area = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=60, height=15)
        self.text_area.pack(pady=5)

        self.detect_button = tk.Button(master, text="Detectar Idioma", command=self.detect_language)
        self.detect_button.pack(pady=10)

        self.history_button = tk.Button(master, text="Ver Historial", command=self.show_history)
        self.history_button.pack(pady=5)

    def detect_language(self):
        text = self.text_area.get("1.0", tk.END).strip()
        if text:
            try:
                language_code = detect(text)
                language_full = language_names.get(language_code, "Idioma desconocido")

                self.master.clipboard_clear()
                self.master.clipboard_append(language_code)

                messagebox.showinfo("Resultado", f"Idioma detectado: {language_full} ({language_code})\n(Código copiado al portapapeles)")

                self.save_to_history(text, language_code, language_full)
            except Exception:
                messagebox.showerror("Error", "No se pudo detectar el idioma. Intenta con más texto.")
        else:
            messagebox.showwarning("Advertencia", "Por favor ingresa algún texto.")

    def save_to_history(self, text, code, full_name):
        with open(HISTORIAL_ARCHIVO, "a", encoding="utf-8") as f:
            f.write(f"[{code}] {full_name} -> \"{text}\"\n\n")

    def show_history(self):
        if not os.path.exists(HISTORIAL_ARCHIVO):
            messagebox.showinfo("Historial", "Aún no hay historial de detecciones.")
            return
        
        with open(HISTORIAL_ARCHIVO, "r", encoding="utf-8") as f:
            historial = f.read()

        history_window = tk.Toplevel(self.master)
        history_window.title("Historial de Detecciones")
        history_window.geometry("500x400")

        text_area = scrolledtext.ScrolledText(history_window, wrap=tk.WORD, width=60, height=20)
        text_area.insert(tk.END, historial)
        text_area.configure(state='disabled')
        text_area.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = LanguageDetectorApp(root)
    root.mainloop()