'''La idea de este proyecto es crear un programa que pruebe la conectividad de sitios web. 
Puedes usar los modulos urllib y tkinter para crear una interfaz gráfica de usuario (GUI) que 
permita a los usuarios ingresar una dirección web. Después de haber recopilado la dirección 
web del usuario, puedes pasarla a una función para devolver un código de estado HTTP para 
el sitio web actual mediante la función .getcode() del módulo urllib. 
En este ejemplo, simplemente determinamos si el código HTTP es 200. Si lo es, sabemos que 
el sitio está funcionando; de lo contrario, informamos al usuario de que no está disponible. '''

import urllib.request
import tkinter as tk
from tkinter import messagebox

def check_website_connectivity(url):
    try:
        response = urllib.request.urlopen(url)
        return response.getcode()
    except Exception as e:
        return None
    
class ConnectivityApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Comprobador de Conectividad Web")
        self.master.geometry("400x200")

        self.label = tk.Label(master, text="Ingresa la URL del sitio web:", font=("Helvetica", 12))
        self.label.pack(pady=10)

        self.url_entry = tk.Entry(master, width=50)
        self.url_entry.pack(pady=5)

        self.check_button = tk.Button(master, text="Comprobar Conectividad", command=self.check_connectivity)
        self.check_button.pack(pady=10)

    def check_connectivity(self):
        url = self.url_entry.get()
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "http://" + url
        
        status_code = check_website_connectivity(url)
        if status_code == 200:
            messagebox.showinfo("Resultado", f"El sitio web está disponible (Código HTTP: {status_code})")
        else:
            messagebox.showerror("Resultado", "El sitio web no está disponible o no se pudo conectar.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ConnectivityApp(root)
    root.mainloop()