import tkinter as tk
import time
import random
import difflib

class TypingSpeedTest:
    def __init__(self, master):
        self.master = master
        self.master.title("⏱ Prueba de Velocidad de Escritura")
        self.master.geometry("700x300")

        self.phrases = [
            "El rápido zorro marrón salta sobre el perro perezoso.",
            "La vida es como una caja de chocolates, nunca sabes lo que te va a tocar.",
            "Python es un lenguaje de programación versátil y poderoso.",
            "La práctica hace al maestro en cualquier habilidad que desees aprender.",
            "Nunca subestimes el poder de una mente enfocada."
        ]

        self.current_phrase = ""
        self.start_time = 0
        self.timer_running = False
        self.elapsed_label = None

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="Presiona 'Iniciar' para comenzar la prueba.", font=("Helvetica", 14))
        self.label.pack(pady=10)

        self.text_entry = tk.Entry(self.master, font=("Courier", 14), width=70)
        self.text_entry.pack(pady=10)
        self.text_entry.config(state="disabled")

        self.start_button = tk.Button(self.master, text="🟢 Iniciar", command=self.start_test, bg="lightgreen")
        self.start_button.pack(pady=5)

        self.timer_label = tk.Label(self.master, text="Tiempo: 0.00s", font=("Helvetica", 12))
        self.timer_label.pack()

        self.result_label = tk.Label(self.master, text="", font=("Helvetica", 12))
        self.result_label.pack(pady=10)

    def start_test(self):
        self.result_label.config(text="", fg="black")
        self.current_phrase = random.choice(self.phrases)
        self.label.config(text=self.current_phrase)
        self.text_entry.config(state="normal")
        self.text_entry.delete(0, tk.END)
        self.text_entry.focus()
        self.start_time = time.time()
        self.timer_running = True
        self.update_timer()
        self.text_entry.bind("<Return>", self.check_result)

    def update_timer(self):
        if self.timer_running:
            elapsed = time.time() - self.start_time
            self.timer_label.config(text=f"Tiempo: {elapsed:.2f}s")
            self.master.after(100, self.update_timer)

    def check_result(self, event):
        self.timer_running = False
        end_time = time.time()
        elapsed_time = end_time - self.start_time
        user_input = self.text_entry.get().strip()
        expected = self.current_phrase.strip()

        # Precisión con difflib
        similarity = difflib.SequenceMatcher(None, user_input.lower(), expected.lower()).ratio()
        accuracy = round(similarity * 100, 2)

        if similarity >= 0.95:
            wpm = (len(user_input.split()) / elapsed_time) * 60
            self.result_label.config(
                text=f"✅ ¡Correcto!\nVelocidad: {wpm:.2f} palabras por minuto\nPrecisión: {accuracy}%",
                fg="green"
            )
        else:
            self.result_label.config(
                text=f"❌ Texto incorrecto.\nPrecisión: {accuracy}%. Intenta de nuevo.",
                fg="red"
            )

        self.text_entry.config(state="disabled")
        self.text_entry.unbind("<Return>")

        # Cambiar botón para reiniciar
        self.start_button.config(text="🔁 Intentar otra vez", command=self.start_test, bg="lightblue")

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTest(root)
    root.mainloop()
