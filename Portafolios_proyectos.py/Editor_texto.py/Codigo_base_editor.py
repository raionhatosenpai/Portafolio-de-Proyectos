"""Crea una interfaz gráfica de usuario (GUI) para simular nuestro propio editor de texto. Este 
ejemplo también utiliza componentes estándar de GUI, incluyendo etiquetas, botones y 
campos de entrada. 
Puedes añadir la capacidad de abrir y guardar archivos, al igual que un editor de texto real."""

import tkinter as tk
from tkinter import filedialog

class TextEditor:
    def __init__(self, master):
        self.master = master
        self.master.title("Editor de Texto Simple")
        
        self.text_area = tk.Text(master, wrap='word')
        self.text_area.pack(expand=1, fill='both')
        
        self.menu = tk.Menu(master)
        master.config(menu=self.menu)
        
        file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Archivo", menu=file_menu)
        file_menu.add_command(label="Abrir", command=self.open_file)
        file_menu.add_command(label="Guardar", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Salir", command=master.quit)
    
    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt",
                                               filetypes=[("Archivos de Texto", "*.txt"),
                                                          ("Todos los Archivos", "*.*")])
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, content)
    
    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Archivos de Texto", "*.txt"),
                                                            ("Todos los Archivos", "*.*")])
        if file_path:
            with open(file_path, 'w', encoding='utf-8') as file:
                content = self.text_area.get(1.0, tk.END)
                file.write(content)

if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditor(root)
    root.mainloop()