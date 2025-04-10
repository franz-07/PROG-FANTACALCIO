import tkinter as tk
from tkinter import Canvas, Entry, font as tkFont

# === CONFIGURAZIONE ===
WIDTH = 430
HEIGHT = 700
BG_COLOR = "#eff3f2"
BUTTON_COLOR = "#50cfd5"
BUTTON_HOVER = "#3cb1b6"
TEXT_COLOR = "#000"
PLACEHOLDER_COLOR = "#999"
CIRCLE_COLOR = "#50cfd5"

# === ENTRY CON PLACEHOLDER ===
class RoundedEntry(Entry):
    def __init__(self, master=None, placeholder="", show=None, **kwargs):
        super().__init__(master, **kwargs)
        self.placeholder = placeholder
        self.placeholder_color = PLACEHOLDER_COLOR
        self.default_fg_color = self['fg']
        self.show_char = show
        
        self.config(
            font=("Poppins", 10),
            relief="flat",
            highlightthickness=0,
            borderwidth=0,
            bg="white"
        )
        
        self.bind("<FocusIn>", self._clear_placeholder)
        self.bind("<FocusOut>", self._add_placeholder)
        self._add_placeholder()

    def _clear_placeholder(self, e):
        if self['fg'] == self.placeholder_color:
            self.delete(0, "end")
            self['fg'] = self.default_fg_color
            if self.show_char:
                self.config(show=self.show_char)

    def _add_placeholder(self, e=None):
        if not self.get():
            self.insert(0, self.placeholder)
            self['fg'] = self.placeholder_color
            if self.show_char:
                self.config(show='')

# === GESTIONE SCHERMATE ===
def show_screen(screen_func):
    for widget in root.winfo_children():
        widget.destroy()
    screen_func()

def empty_screen():
    frame = tk.Frame(root, bg="white")
    frame.pack(fill="both", expand=True)
    tk.Label(frame, text="Nuova Schermata", font=("Poppins", 20)).pack(pady=300)

# === SCHERMATA DI REGISTRAZIONE ===
def registration_screen():
    canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg=BG_COLOR, highlightthickness=0)
    canvas.pack()

    # Carica il font Poppins
    try:
        poppins = tkFont.Font(family="Poppins", size=10)
        poppins_bold = tkFont.Font(family="Poppins", size=13, weight="bold")
        poppins_button = tkFont.Font(family="Poppins", size=11, weight="bold")
    except:
        poppins = ("Helvetica", 10)
        poppins_bold = ("Helvetica", 13, "bold")
        poppins_button = ("Helvetica", 11, "bold")

    # Cerchi verdi sovrapposti a sinistra
    canvas.create_oval(-50, -50, 150, 150, fill=CIRCLE_COLOR, outline="", stipple='gray25')
    canvas.create_oval(50, -70, 250, 130, fill=CIRCLE_COLOR, outline="", stipple='gray25')

    # Titolo
    canvas.create_text(WIDTH/2, 180, text="Fantacalcio", font=poppins_bold, fill=TEXT_COLOR)
    canvas.create_text(WIDTH/2, 210, text="Crea il tuo account", font=poppins, fill=TEXT_COLOR)

    # Campi di registrazione
    fields = [
        {"placeholder": "Nome e Cognome", "y": 280},
        {"placeholder": "Email", "y": 340},
        {"placeholder": "Password", "y": 400, "show": "*"},
        {"placeholder": "Conferma Password", "y": 460, "show": "*"}
    ]

    for field in fields:
        entry = RoundedEntry(
            root,
            placeholder=field["placeholder"],
            show=field.get("show"),
        )
        entry.place(x=40, y=field["y"], width=350, height=45)

    # Bottone Registrati
    btn = tk.Button(
        root,
        text="REGISTRATI",
        bg=BUTTON_COLOR,
        fg="white",
        font=poppins_button,
        activebackground=BUTTON_HOVER,
        command=lambda: show_screen(empty_screen),
        relief="flat",
        cursor="hand2",
        borderwidth=0
    )
    btn.place(x=40, y=530, width=350, height=50)
    
    btn.bind("<Enter>", lambda e: btn.config(bg=BUTTON_HOVER))
    btn.bind("<Leave>", lambda e: btn.config(bg=BUTTON_COLOR))

    # Link per accesso
    canvas.create_text(WIDTH/2 - 30, 600, text="Hai già un account?", font=poppins, fill=TEXT_COLOR)

    login_link = tk.Label(
        root,
        text="Accedi ora",
        font=(poppins["family"], poppins["size"], "bold"),
        fg=BUTTON_COLOR,
        bg=BG_COLOR,
        cursor="hand2"
    )
    login_link.place(x=WIDTH/2 + 40, y=590)
    login_link.bind("<Button-1>", lambda e: show_screen(login_screen))

# === SCHERMATA DI LOGIN ===
def login_screen():
    canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg=BG_COLOR, highlightthickness=0)
    canvas.pack()

    # Carica il font Poppins
    try:
        poppins = tkFont.Font(family="Poppins", size=10)
        poppins_bold = tkFont.Font(family="Poppins", size=13, weight="bold")
        poppins_button = tkFont.Font(family="Poppins", size=11, weight="bold")
    except:
        poppins = ("Helvetica", 10)
        poppins_bold = ("Helvetica", 13, "bold")
        poppins_button = ("Helvetica", 11, "bold")

    # Cerchi verdi sovrapposti a sinistra
    canvas.create_oval(-50, -50, 150, 150, fill=CIRCLE_COLOR, outline="", stipple='gray25')
    canvas.create_oval(50, -70, 250, 130, fill=CIRCLE_COLOR, outline="", stipple='gray25')

    # Titolo
    canvas.create_text(WIDTH/2, 180, text="Fantacalcio", font=poppins_bold, fill=TEXT_COLOR)
    canvas.create_text(WIDTH/2, 210, text="Bentornato!", font=poppins, fill=TEXT_COLOR)

    # LOGO (solo nella schermata login)
    canvas.create_rectangle(165, 240, 265, 340, outline="#ddd", fill="#f8f8f8")  # Placeholder quadrato
    canvas.create_text(WIDTH/2, 290, text="LOGO", font=("Poppins", 12), fill="#aaa")

    # Campi di login
    fields = [
        {"placeholder": "Email", "y": 370},
        {"placeholder": "Password", "y": 430, "show": "*"}
    ]

    for field in fields:
        entry = RoundedEntry(
            root,
            placeholder=field["placeholder"],
            show=field.get("show"),
        )
        entry.place(x=40, y=field["y"], width=350, height=45)

    # Link "Password dimenticata?"
    canvas.create_text(WIDTH-40, 480, text="Password dimenticata?", font=poppins, fill=BUTTON_COLOR, anchor="e")

    # Bottone Accedi
    btn = tk.Button(
        root,
        text="ACCEDI",
        bg=BUTTON_COLOR,
        fg="white",
        font=poppins_button,
        activebackground=BUTTON_HOVER,
        command=lambda: show_screen(empty_screen),
        relief="flat",
        cursor="hand2",
        borderwidth=0
    )
    btn.place(x=40, y=520, width=350, height=50)
    
    btn.bind("<Enter>", lambda e: btn.config(bg=BUTTON_HOVER))
    btn.bind("<Leave>", lambda e: btn.config(bg=BUTTON_COLOR))

    # Link per registrazione
    canvas.create_text(WIDTH/2 - 40, 590, text="Non hai un account?", font=poppins, fill=TEXT_COLOR)

    register_link = tk.Label(
        root,
        text="Registrati",
        font=(poppins["family"], poppins["size"], "bold"),
        fg=BUTTON_COLOR,
        bg=BG_COLOR,
        cursor="hand2"
    )
    register_link.place(x=WIDTH/2 + 40, y=580)
    register_link.bind("<Button-1>", lambda e: show_screen(registration_screen))

# === MAIN ===
root = tk.Tk()
root.geometry(f"{WIDTH}x{HEIGHT}")
root.title("Fantacalcio")
root.resizable(False, False)

# Avvia con la schermata di registrazione
registration_screen()
root.mainloop()