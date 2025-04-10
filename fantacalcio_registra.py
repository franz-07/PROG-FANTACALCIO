import tkinter as tk
from PIL import Image, ImageTk

# === Funzione per i placeholder ===
def aggiungi_placeholder(entry, testo_esempio):
    entry.insert(0, testo_esempio)
    entry.config(fg="gray")

    def al_focus_in(event):
        if entry.get() == testo_esempio:
            entry.delete(0, tk.END)
            entry.config(fg="black")

    def al_focus_out(event):
        if entry.get() == "":
            entry.insert(0, testo_esempio)
            entry.config(fg="gray")

    entry.bind("<FocusIn>", al_focus_in)
    entry.bind("<FocusOut>", al_focus_out)

# === Funzione per cambiare schermata ===
def apri_seconda_schermata():
    for widget in root.winfo_children():
        widget.destroy()
    root.configure(bg="white")

# === Setup della finestra ===
root = tk.Tk()
root.title("NomeApp")
root.geometry("430x932")
root.configure(bg="#eaf3f3")
root.resizable(False, False)

# === Immagine ===
img = Image.open("brazil.png")
img = img.resize((250, 250))
img_tk = ImageTk.PhotoImage(img)
img_label = tk.Label(root, image=img_tk, bg="#eaf3f3")
img_label.place(x=180, y=0)

# === Titolo ===
title = tk.Label(root, text="Benvenuto in NomeApp", font=("Helvetica", 14, "bold"), bg="#eaf3f3")
title.pack(pady=(270, 5))

subtitle = tk.Label(root, text="Ti aiutiamo a organizzare\ni tuoi task.", font=("Helvetica", 10), bg="#eaf3f3", justify="center")
subtitle.pack(pady=(0, 20))

# === Campi con placeholder ===
def crea_entry(testo_esempio):
    entry = tk.Entry(root, font=("Helvetica", 12), bg="white", fg="gray", relief="flat")
    entry.pack(pady=10, ipadx=10, ipady=10, padx=20, fill='x')
    aggiungi_placeholder(entry, testo_esempio)
    return entry

name_entry = crea_entry("Inserisci il tuo nome")
email_entry = crea_entry("Inserisci la tua email")
password_entry = crea_entry("Inserisci la password")
confirm_entry = crea_entry("Conferma la password")

# === Bottone Registrati ===
register_btn = tk.Button(root, text="Registrati", bg="#3cc7cb", fg="white",
                         font=("Helvetica", 12, "bold"), relief="flat",
                         command=apri_seconda_schermata)
register_btn.pack(pady=30, ipadx=10, ipady=10, padx=20, fill="x")

# === Testo in basso ===
bottom_text = tk.Label(root, text="Hai già un account?", bg="#eaf3f3", font=("Helvetica", 10))
bottom_text.pack()

login_link = tk.Label(root, text="Accedi", fg="#3cc7cb", bg="#eaf3f3", font=("Helvetica", 10, "underline"), cursor="hand2")
login_link.pack()

root.mainloop()