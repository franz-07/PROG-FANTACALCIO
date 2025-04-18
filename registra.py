import customtkinter as ctk
from tkinter import messagebox
import os
import pyglet

pyglet.font.add_file("Poppins-Regular.ttf")

class SchermataRegistra(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Frame centrale per i campi (username, password, conferma password)
        self.frame_centrale = ctk.CTkFrame(self, width=350)
        self.frame_centrale.place(relx=0.5, rely=0.4, anchor="center")

        # Campo Nome Utente
        ctk.CTkLabel(self.frame_centrale, text="Nome utente:", font=("Poppins", 16)).grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.username_entry = ctk.CTkEntry(self.frame_centrale, font=("Poppins", 16))
        self.username_entry.grid(row=0, column=1, padx=10, pady=5)
        self.username_entry.bind("<KeyRelease>", self.check_fields)

        # Campo Password
        ctk.CTkLabel(self.frame_centrale, text="Password:", font=("Poppins", 16)).grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.password_entry = ctk.CTkEntry(self.frame_centrale, show="*", font=("Poppins", 16))
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)
        self.password_entry.bind("<KeyRelease>", self.check_fields)

        # Campo Conferma Password
        ctk.CTkLabel(self.frame_centrale, text="Conferma Password:", font=("Poppins", 16)).grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.confirm_password_entry = ctk.CTkEntry(self.frame_centrale, show="*", font=("Poppins", 16))
        self.confirm_password_entry.grid(row=2, column=1, padx=10, pady=5)
        self.confirm_password_entry.bind("<KeyRelease>", self.check_fields)

        # Etichetta di errore (se ce n'è una)
        self.error_label = ctk.CTkLabel(self.frame_centrale, text="", text_color="red", font=("Poppins", 14))
        self.error_label.grid(row=3, column=0, columnspan=2)

        # Tasto "Registrati" al di fuori del frame centrale
        self.frame_bottone_registra = ctk.CTkFrame(self)
        self.frame_bottone_registra.place(relx=0.5, rely=0.7, anchor="center")

        self.register_button = ctk.CTkButton(self.frame_bottone_registra, text="Registrati", command=self.registra_utente, font=("Poppins", 16), fg_color="red", width=200)
        self.register_button.pack(pady=10)
        
        # Cambia il colore del tasto se i campi sono compilati
        self.check_fields()  # Controllo iniziale per verificare se i campi sono vuoti

        # Tasto "Login" sotto il tasto "Registrati"
        self.login_button = ctk.CTkButton(self.frame_centrale, text="Hai già un account? Accedi ora!", 
                                          command=self.master.mostra_schermata_login, font=("Arial", 12))
        self.login_button.grid(row=4, column=0, columnspan=2, pady=5)

    def check_fields(self, event=None):
        if self.username_entry.get().strip() and self.password_entry.get().strip() and self.confirm_password_entry.get().strip():
            self.register_button.configure(fg_color="green")
        else:
            self.register_button.configure(fg_color="red")

    def registra_utente(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        conferma = self.confirm_password_entry.get().strip()

        if not username or not password or not conferma:
            self.error_label.configure(text="Compila tutti i campi.")
            return

        if password != conferma:
            self.error_label.configure(text="Le password non coincidono.")
            return

        if os.path.exists("user_data.txt"):
            with open("user_data.txt", "r") as file:
                for line in file:
                    existing_user, _ = line.strip().split(",")
                    if username == existing_user:
                        self.error_label.configure(text="Nome utente già esistente.")
                        return

        with open("user_data.txt", "a") as file:
            file.write(f"{username},{password}\n")

        messagebox.showinfo("Registrazione", "Utente registrato con successo!")
        self.master.mostra_schermata_home(username)
