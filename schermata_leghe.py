import tkinter as tk
from tkinter import PhotoImage

# Creazione della finestra
root = tk.Tk()
root.title("Scegli la tua lega")
root.geometry("1080x720")

# Creazione del testo
label = tk.Label(root, text="Scegli la tua lega", font=("Arial", 24))
label.pack(pady=20)

# Caricamento immagini
try:
    img1 = PhotoImage(file="immagini/immagine1_lega.png")  
    img2 = PhotoImage(file="immagini/immagine2_lega.png")  
    # Posizionamento immagini
    img_label1 = tk.Label(root, image=img1)
    img_label1.pack(side=tk.LEFT, padx=10)

    img_label2 = tk.Label(root, image=img2)
    img_label2.pack(side=tk.RIGHT, padx=10)
except:
    tk.Label(root, text="Non sono state trovate immagini, sostituiscile con file locali.").pack()

# Loop della finestra
root.mainloop()
