import tkinter as tk
from tkinter import font as tkFont

# Configurazione
WIDTH = 430
HEIGHT = 700
BG_COLOR = "#eff3f2"
BUTTON_COLOR = "#50cfd5"
TEXT_COLOR = "#000"
PLACEHOLDER_COLOR = "#999"  # Colore per il testo placeholder

# Font standard
font_normal = ("Helvetica", 10)
font_bold = ("Helvetica", 13, "bold")
font_button = ("Helvetica", 11, "bold")

# Creazione finestra principale
root = tk.Tk()
root.geometry(f"{WIDTH}x{HEIGHT}")
root.title("Fantacalcio")
root.resizable(False, False)
root.configure(bg=BG_COLOR)

# Funzioni per gestire i placeholder
def on_entry_click(entry, placeholder):
    if entry.get() == placeholder:
        entry.delete(0, tk.END)
        entry.config(fg=TEXT_COLOR)
        if placeholder == "Password" or placeholder == "Conferma Password":
            entry.config(show="*")

def on_focusout(entry, placeholder):
    if entry.get() == "":
        entry.insert(0, placeholder)
        entry.config(fg=PLACEHOLDER_COLOR)
        if placeholder == "Password" or placeholder == "Conferma Password":
            entry.config(show="")

# Funzioni di navigazione
def clear_screen():
    for widget in root.winfo_children():
        widget.destroy()

def show_empty_screen():
    clear_screen()
    tk.Label(root, text="Nuova Schermata", font=font_bold).pack(pady=300)

# Funzioni helper per la navigazione
def go_to_login(event=None):  # Aggiunto event=None per gestire sia click che chiamata diretta
    login_screen()

def go_to_registration(event=None):
    registration_screen()

# Schermata di Registrazione
def registration_screen():
    clear_screen()
    
    # Titoli
    tk.Label(root, text="Fantacalcio", font=font_bold, bg=BG_COLOR).place(x=WIDTH/2, y=180, anchor="center")
    tk.Label(root, text="Crea il tuo account", font=font_normal, bg=BG_COLOR).place(x=WIDTH/2, y=210, anchor="center")

    # Campi di input con placeholder
    fields = [
        {"placeholder": "Nome e Cognome", "y": 280, "show": ""},
        {"placeholder": "Email", "y": 340, "show": ""},
        {"placeholder": "Password", "y": 400, "show": "*"},
        {"placeholder": "Conferma Password", "y": 460, "show": "*"}
    ]
    
    for field in fields:
        frame = tk.Frame(root, bg="white")
        frame.place(x=40, y=field["y"], width=350, height=45)
        
        entry = tk.Entry(frame, font=font_normal, relief="flat", bg="white", fg=PLACEHOLDER_COLOR)
        entry.pack(fill="both", expand=True, padx=10, pady=10)
        entry.insert(0, field["placeholder"])
        entry.config(show=field["show"])
        
        # Bind per i placeholder
        entry.bind("<FocusIn>", lambda e, entry=entry, ph=field["placeholder"]: on_entry_click(entry, ph))
        entry.bind("<FocusOut>", lambda e, entry=entry, ph=field["placeholder"]: on_focusout(entry, ph))

    # Pulsante Registrati
    btn = tk.Button(root, text="REGISTRATI", font=font_button, bg=BUTTON_COLOR, fg="white", command=show_empty_screen)
    btn.place(x=40, y=530, width=350, height=50)

    # Link per accesso
    tk.Label(root, text="Hai già un account?", font=font_normal, bg=BG_COLOR).place(x=WIDTH/2-30, y=600, anchor="e")
    
    login_link = tk.Label(root, text="Accedi ora", font=(font_normal[0], font_normal[1], "bold"), fg=BUTTON_COLOR, bg=BG_COLOR, cursor="hand2")
    login_link.place(x=WIDTH/2+40, y=600, anchor="w")
    login_link.bind("<Button-1>", go_to_login)

# Schermata di Login
def login_screen():
    clear_screen()
    
    # Titoli
    tk.Label(root, text="Fantacalcio", font=font_bold, bg=BG_COLOR).place(x=WIDTH/2, y=180, anchor="center")
    tk.Label(root, text="Bentornato!", font=font_normal, bg=BG_COLOR).place(x=WIDTH/2, y=210, anchor="center")

    # Logo placeholder
    tk.Frame(root, width=100, height=100, bg="#f8f8f8", highlightbackground="#ddd", highlightthickness=1).place(x=WIDTH/2-50, y=240)
    tk.Label(root, text="LOGO", font=font_normal, fg="#aaa", bg="#f8f8f8").place(x=WIDTH/2, y=290, anchor="center")

    # Campi di input con placeholder
    fields = [
        {"placeholder": "Email", "y": 370, "show": ""},
        {"placeholder": "Password", "y": 430, "show": "*"}
    ]
    
    for field in fields:
        frame = tk.Frame(root, bg="white")
        frame.place(x=40, y=field["y"], width=350, height=45)
        
        entry = tk.Entry(frame, font=font_normal, relief="flat", bg="white", fg=PLACEHOLDER_COLOR)
        entry.pack(fill="both", expand=True, padx=10, pady=10)
        entry.insert(0, field["placeholder"])
        entry.config(show=field["show"])
        
        # Bind per i placeholder
        entry.bind("<FocusIn>", lambda e, entry=entry, ph=field["placeholder"]: on_entry_click(entry, ph))
        entry.bind("<FocusOut>", lambda e, entry=entry, ph=field["placeholder"]: on_focusout(entry, ph))

    # Link password dimenticata
    tk.Label(root, text="Password dimenticata?", font=font_normal, fg=BUTTON_COLOR, bg=BG_COLOR).place(x=390, y=480, anchor="e")

    # Pulsante Accedi
    btn = tk.Button(root, text="ACCEDI", font=font_button, bg=BUTTON_COLOR, fg="white", command=show_empty_screen)
    btn.place(x=40, y=520, width=350, height=50)

    # Link per registrazione
    tk.Label(root, text="Non hai un account?", font=font_normal, bg=BG_COLOR).place(x=WIDTH/2-40, y=590, anchor="e")
    
    register_link = tk.Label(root, text="Registrati", font=(font_normal[0], font_normal[1], "bold"), fg=BUTTON_COLOR, bg=BG_COLOR, cursor="hand2")
    register_link.place(x=WIDTH/2+40, y=590, anchor="w")
    register_link.bind("<Button-1>", go_to_registration)

# Avvia con la schermata di registrazione
registration_screen()
root.mainloop()