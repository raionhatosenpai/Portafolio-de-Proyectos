import urllib.request
import tkinter as tk
from tkinter import messagebox, scrolledtext
import os

HISTORIAL = "historial_webs.txt"

def check_website_connectivity(url):
    try:
        response = urllib.request.urlopen(url, timeout=5)
        return response.getcode()
    except Exception as e:
        return None

class ConnectivityApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Comprobador de Conectividad Web")
        self.master.geometry("500x300")

        self.label = tk.Label(master, text="Ingresa la URL del sitio web:", font=("Helvetica", 12))
        self.label.pack(pady=10)

        self.url_entry = tk.Entry(master, width=60)
        self.url_entry.pack(pady=5)
        self.url_entry.focus()
        self.url_entry.bind("<Control-a>", lambda event: self.url_entry.select_range(0, tk.END))

        self.check_button = tk.Button(master, text="Comprobar Conectividad", command=self.check_connectivity)
        self.check_button.pack(pady=10)

        self.result_label = tk.Label(master, text="", font=("Helvetica", 12))
        self.result_label.pack(pady=5)

        self.history_button = tk.Button(master, text="Ver Historial", command=self.show_history)
        self.history_button.pack(pady=5)

    def check_connectivity(self):
        url = self.url_entry.get().strip()

        if not url:
            messagebox.showwarning("Advertencia", "Por favor ingresa una URL.")
            return

        if not url.startswith("http"):
            url = "http://" + url

        status_code = check_website_connectivity(url)
        if status_code == 200:
            self.result_label.config(text="✅ El sitio está disponible (HTTP 200)", fg="green")
            self.save_to_history(url, "Disponible")
        else:
            self.result_label.config(text="❌ El sitio no está disponible o falló la conexión", fg="red")
            self.save_to_history(url, "No disponible")

    def save_to_history(self, url, estado):
        with open(HISTORIAL, "a", encoding="utf-8") as f:
            f.write(f"{url} → {estado}\n")

    def show_history(self):
        if not os.path.exists(HISTORIAL):
            messagebox.showinfo("Historial", "Aún no hay historial guardado.")
            return
        
        with open(HISTORIAL, "r", encoding="utf-8") as f:
            contenido = f.read()

        history_win = tk.Toplevel(self.master)
        history_win.title("Historial de URLs Comprobadas")
        history_win.geometry("500x400")

        text_area = scrolledtext.ScrolledText(history_win, wrap=tk.WORD)
        text_area.insert(tk.END, contenido)
        text_area.config(state='disabled')
        text_area.pack(padx=10, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = ConnectivityApp(root)
    root.mainloop()