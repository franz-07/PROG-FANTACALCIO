import tkinter as tk
from tkinter import messagebox
import os
import random

class SchermataLogin(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        tk.Label(self, text="Nome utente:", font=("Arial", 16)).grid(row=0, column=0, padx=20, pady=10, sticky="e")
        self.username_entry = tk.Entry(self, font=("Arial", 16))
        self.username_entry.grid(row=0, column=1, padx=20, pady=10, sticky="w")
        self.username_entry.bind("<KeyRelease>", self.check_fields)  # Verifica cambiamenti nei campi

        tk.Label(self, text="Password:", font=("Arial", 16)).grid(row=1, column=0, padx=20, pady=10, sticky="e")
        self.password_entry = tk.Entry(self, show="*", font=("Arial", 16))
        self.password_entry.grid(row=1, column=1, padx=20, pady=10, sticky="w")
        self.password_entry.bind("<KeyRelease>", self.check_fields)  # Verifica cambiamenti nei campi

        self.create_account_button = tk.Button(self, text="Non hai un account? Crealo ora!", command=self.create_account, font=("Arial", 7), width=25)
        self.create_account_button.grid(row=2, column=0, columnspan=3, pady=5)

        self.login_button = tk.Button(self, text="Login", command=self.login, font=("Arial", 16), width=25)
        self.login_button.grid(row=3, column=0, columnspan=3, pady=20)
        self.login_button.bind("<Enter>", self.move_button)  # Comportamento "fuga"

        self.error_label = tk.Label(self, text="", fg="red", font=("Arial", 14))
        self.error_label.grid(row=4, column=0, columnspan=3)

        self.login_button.config(fg="red")

    def move_button(self, event):
        if not self.fields_filled():  # Solo se i campi non sono riempiti
            x = random.randint(0, 300)
            y = random.randint(0, 500)
            self.login_button.place(x=x, y=y)

    def reset_button_position(self):
        self.login_button.place(x=80, y=150)


    def check_fields(self, event):
        # Controlla se entrambi i campi sono riempiti
        if self.fields_filled():
            self.reset_button_position()  # Torna alla posizione originale
            self.login_button.unbind("<Enter>")  # Disattiva il comportamento "fuga"
            self.login_button.config(fg="green")
        else:
            self.login_button.bind("<Enter>", self.move_button)  # Riattiva il comportamento "fuga"
            self.login_button.config(fg="red")

    def fields_filled(self):
        # Verifica se entrambi i campi contengono testo
        return bool(self.username_entry.get().strip()) and bool(self.password_entry.get().strip())

    def login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if not os.path.exists("user_data.txt"):
            self.error_label.config(text="Nessun account registrato!", fg="red")
            return

        with open("user_data.txt", "r") as file:
            users = [line.strip().split(",") for line in file.readlines()]

        for saved_username, saved_password in users:
            if username == saved_username:
                if password == saved_password:
                    messagebox.showinfo("Login", "Login effettuato con successo!")
                    self.error_label.config(text="")
                    self.reset_button_position()  # Torna alla posizione originale
                    self.login_button.unbind("<Enter>")  # Disattiva il comportamento "fuga"
                    self.master.mostra_schermata_home(username)  # Passa alla schermata Home
                    return
                else:
                    self.error_label.config(text="Password errata", fg="red")
                    return

        self.error_label.config(text="Utente non trovato", fg="red")

    def create_account(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if not username or not password:
            messagebox.showwarning("Attenzione", "Inserisci un nome utente e una password validi.")
            return

        if os.path.exists("user_data.txt"):
            with open("user_data.txt", "r") as file:
                users = [line.strip().split(",")[0] for line in file.readlines()]
                if username in users:
                    self.error_label.config(text="Questo nome utente è già registrato", fg="red")
                    return

        try:
            with open("user_data.txt", "a") as file:
                file.write(f"{username},{password}\n")
            messagebox.showinfo("Account", "Account creato con successo!")
            self.error_label.config(text="")  # Pulisce errori precedenti
        except Exception as e:
            messagebox.showerror("Errore", f"Errore durante la creazione dell'account: {e}")
