import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
import os

class TextEditor:
    def __init__(self, master):
        self.master = master
        self.master.title("Editor de Texto Simple")
        self.current_file = None

        # Área de texto con scroll
        self.text_area = ScrolledText(master, wrap='word', font=("Consolas", 12))
        self.text_area.pack(expand=1, fill='both')

        # Menú superior
        self.menu = tk.Menu(master)
        master.config(menu=self.menu)

        file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Archivo", menu=file_menu)
        file_menu.add_command(label="📂 Abrir", command=self.open_file)
        file_menu.add_command(label="💾 Guardar", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Salir", command=self.exit_app)

        # Barra de estado
        self.status = tk.Label(master, text="Listo", anchor="w", bg="lightgrey")
        self.status.pack(side="bottom", fill="x")

    def open_file(self):
        file_path = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
        )
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, content)
                self.current_file = file_path
                self.master.title(f"Editor de Texto - {os.path.basename(file_path)}")
                self.status.config(text=f"Abriste: {file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo abrir el archivo:\n{e}")

    def save_file(self):
        if not self.current_file:
            file_path = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
            )
            if not file_path:
                return
            self.current_file = file_path

        try:
            with open(self.current_file, 'w', encoding='utf-8') as file:
                content = self.text_area.get(1.0, tk.END).rstrip()
                file.write(content)
            self.master.title(f"Editor de Texto - {os.path.basename(self.current_file)}")
            self.status.config(text=f"Guardado: {self.current_file}")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar el archivo:\n{e}")

    def exit_app(self):
        if messagebox.askokcancel("Salir", "¿Seguro que quieres salir?"):
            self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    app = TextEditor(root)
    root.mainloop()
