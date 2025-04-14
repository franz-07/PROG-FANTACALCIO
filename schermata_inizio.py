import tkinter as tk
import tkinter.font as tkFont
import pyglet
import itertools

pyglet.font.add_file("Poppins-Regular.ttf")

class SchermataInizio(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.label1 = tk.Label(self, text="FANTA-ALCHIMISTI", font=("Poppins", 18))
        self.label1.pack(pady=20)

        self.rotellina = Rotellina(self)
        self.after(2000, self.mostra_label2)  # Aspetta 2s prima di mostrare label2

    def mostra_label2(self):
        self.label2 = tk.Label(self, text="Premi qualsiasi tasto per iniziare", font=("Poppins", 11))
        self.label2.pack(pady=20)
        self.bind_all("<Key>", self.on_key_press)

    def on_key_press(self, event):
        self.master.mostra_schermata_login()

class Rotellina:
    def __init__(self, parent):
        self.canvas = tk.Canvas(parent, width=100, height=100)
        self.canvas.pack()
        self.arc = self.canvas.create_arc(20, 20, 80, 80, start=0, extent=90, outline="blue", width=5, style="arc")
        self.angles = itertools.cycle(range(0, 360, 10))
        self.animate()

    def animate(self):
        next_angle = next(self.angles)
        self.canvas.itemconfig(self.arc, start=next_angle)
        self.canvas.after(50, self.animate)
