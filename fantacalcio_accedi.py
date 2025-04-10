import tkinter as tk
from PIL import Image, ImageTk
import os

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

# === Funzione per pulire la schermata ===
def clear_screen():
    for widget in root.winfo_children():
        widget.destroy()

# === Funzione schermata LOGIN ===
def mostra_login():
    clear_screen()
    root.configure(bg="#eaf3f3")

    # Immagine login
    img = Image.open("aura.png")  # usa il file che mi hai appena caricato
    img = img.resize((200, 200))
    img_tk = ImageTk.PhotoImage(img)
    img_label = tk.Label(root, image=img_tk, bg="#eaf3f3")
    img_label.image = img_tk  # evita che venga eliminata
    img_label.pack(pady=(60, 10))

    # Testo
    titolo = tk.Label(root, text="Welcome back", font=("Helvetica", 14, "bold"), bg="#eaf3f3")
    titolo.pack(pady=10)

    # Email
    email_entry = tk.Entry(root, font=("Helvetica", 12), bg="white", fg="gray", relief="flat")
    email_entry.pack(pady=10, ipadx=10, ipady=10, padx=20, fill='x')
    add_placeholder(email_entry, "Enter your Email")

    # Password
    password_entry = tk.Entry(root, font=("Helvetica", 12), bg="white", fg="gray", relief="flat")
    password_entry.pack(pady=10, ipadx=10, ipady=10, padx=20, fill='x')
    add_placeholder(password_entry, "Enter Password")

    # Link Forget Password
    forgot = tk.Label(root, text="Forget password ?", font=("Helvetica", 9), fg="#3cc7cb", bg="#eaf3f3", cursor="hand2")
    forgot.pack(pady=(5, 20))

    # Bottone Login
    login_btn = tk.Button(root, text="Login", bg="#3cc7cb", fg="white",
                          font=("Helvetica", 12, "bold"), relief="flat")
    login_btn.pack(pady=10, ipadx=10, ipady=10, padx=20, fill="x")

    # Link Sign Up
    bottom_text = tk.Label(root, text="Don’t have an account ?", bg="#eaf3f3", font=("Helvetica", 10))
    bottom_text.pack()

    signup_link = tk.Label(root, text="Sign Up", fg="#3cc7cb", bg="#eaf3f3", font=("Helvetica", 10, "underline"), cursor="hand2")
    signup_link.pack()
    signup_link.bind("<Button-1>", lambda e: mostra_registrazione())

# === Funzione schermata REGISTRAZIONE ===
def mostra_registrazione():
    clear_screen()
    root.configure(bg="#eaf3f3")

    # Immagine registrazione
    img = Image.open("image.png")  # immagine omino col pallone
    img = img.resize((250, 250))
    img_tk = ImageTk.PhotoImage(img)
    img_label = tk.Label(root, image=img_tk, bg="#eaf3f3")
    img_label.image = img_tk
    img_label.place(x=180, y=0)

    # Titolo
    title = tk.Label(root, text="Benvenuto nel NomeApp", font=("Helvetica", 14, "bold"), bg="#eaf3f3")
    title.pack(pady=(270, 5))

    subtitle = tk.Label(root, text="Let's help to meet up your\ntasks.", font=("Helvetica", 10), bg="#eaf3f3", justify="center")
    subtitle.pack(pady=(0, 20))

    # Campi
    def crea_entry(placeholder):
        entry = tk.Entry(root, font=("Helvetica", 12), bg="white", fg="gray", relief="flat")
        entry.pack(pady=10, ipadx=10, ipady=10, padx=20, fill='x')
        add_placeholder(entry, placeholder)
        return entry

    crea_entry("Inserisci il nome")
    crea_entry("Inserisci l'email")
    crea_entry("Inserisci la Password")
    crea_entry("Conferma la Password")

    # Bottone
    register_btn = tk.Button(root, text="Registrati", bg="#3cc7cb", fg="white",
                             font=("Helvetica", 12, "bold"), relief="flat",
                             command=mostra_login)
    register_btn.pack(pady=30, ipadx=10, ipady=10, padx=20, fill="x")

    # Link in basso
    bottom_text = tk.Label(root, text="Hai già un account ?", bg="#eaf3f3", font=("Helvetica", 10))
    bottom_text.pack()

    login_link = tk.Label(root, text="Accedi", fg="#3cc7cb", bg="#eaf3f3", font=("Helvetica", 10, "underline"), cursor="hand2")
    login_link.pack()
    login_link.bind("<Button-1>", lambda e: mostra_login())

# === Inizializza finestra ===
root = tk.Tk()
root.title("NomeApp")
root.geometry("430x932")
root.configure(bg="#eaf3f3")
root.resizable(False, False)

# Mostra schermata registrazione all'inizio
mostra_registrazione()

root.mainloop()
