import tkinter as tk
from PIL import Image, ImageTk

# === Funzione per i placeholder ===
def add_placeholder(entry, placeholder):
    entry.insert(0, placeholder)
    entry.config(fg="gray")

    def on_focus_in(event):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry.config(fg="black")

    def on_focus_out(event):
        if entry.get() == "":
            entry.insert(0, placeholder)
            entry.config(fg="gray")

    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)

# === Funzione per cambiare schermata ===
def apri_seconda_schermata():
    for widget in root.winfo_children():
        widget.destroy()
    root.configure(bg="white")  # Sfondo bianco per la nuova schermata

# === Setup della finestra ===
root = tk.Tk()
root.title("NomeApp")
root.geometry("430x932")
root.configure(bg="#eaf3f3")
root.resizable(False, False)

# === Immagine ===
img = Image.open("brazil.png")  # Usa la tua immagine
img = img.resize((250, 250))
img_tk = ImageTk.PhotoImage(img)
img_label = tk.Label(root, image=img_tk, bg="#eaf3f3")
img_label.place(x=180, y=0)

# === Titolo ===
title = tk.Label(root, text="Benvenuto nel NomeApp", font=("Helvetica", 14, "bold"), bg="#eaf3f3")
title.pack(pady=(270, 5))

subtitle = tk.Label(root, text="Let's help to meet up your\ntasks.", font=("Helvetica", 10), bg="#eaf3f3", justify="center")
subtitle.pack(pady=(0, 20))

# === Campi con placeholder ===
def crea_entry(placeholder):
    entry = tk.Entry(root, font=("Helvetica", 12), bg="white", fg="gray", relief="flat")
    entry.pack(pady=10, ipadx=10, ipady=10, padx=20, fill='x')
    add_placeholder(entry, placeholder)
    return entry

name_entry = crea_entry("Inserisci il nome")
email_entry = crea_entry("Inserisci l'email")
password_entry = crea_entry("Inserisci la Password")
confirm_entry = crea_entry("Conferma la Password")

# === Bottone Registrati ===
register_btn = tk.Button(root, text="Registrati", bg="#3cc7cb", fg="white",
                         font=("Helvetica", 12, "bold"), relief="flat",
                         command=apri_seconda_schermata)
register_btn.pack(pady=30, ipadx=10, ipady=10, padx=20, fill="x")

# === Testo basso ===
bottom_text = tk.Label(root, text="Hai già un account ?", bg="#eaf3f3", font=("Helvetica", 10))
bottom_text.pack()

login_link = tk.Label(root, text="Accedi", fg="#3cc7cb", bg="#eaf3f3", font=("Helvetica", 10, "underline"), cursor="hand2")
login_link.pack()

root.mainloop()
