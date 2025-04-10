import tkinter as tk
import tkinter.font as tkFont
import pyglet
import itertools
import itertools
import time

def on_key_press(event):
    print("Hai premuto un tasto!")
    root.destroy()

def mostra_label2():
    global label2
    label2 = tk.Label(root, text="Premi qualsiasi tasto per iniziare", font=("Poppins", 9))
    label2.pack(pady=20)
    root.bind("<Key>", on_key_press)

class Rotellina:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=100, height=100)
        self.canvas.pack()

        # Disegna la rotellina
        self.arc = self.canvas.create_arc(20, 20, 80, 80, start=0, extent=90, outline="blue", width=5, style="arc")

        # Angoli per animazione
        self.angles = itertools.cycle(range(0, 360, 10))
        self.animate()

    def animate(self):
        """Rotazione della rotellina"""
        next_angle = next(self.angles)
        self.canvas.itemconfig(self.arc, start=next_angle)
        self.root.after(50, self.animate)  # Cambia il valore per controllare la velocità


pyglet.font.add_file("Poppins-Regular.ttf")

root = tk.Tk()
root.geometry("450x700")
root.title("Inizio")

label1 = tk.Label(root, text="FANTA-ALCHIMISTI", font=("Poppins", 18))
label1.pack(pady=20)

# Rotellina simulata (sostituire con la tua implementazione Rotellina)
rotellina = Rotellina(root)

# Fai comparire label2 dopo 3 secondi
root.after(3000, mostra_label2)

root.mainloop()

