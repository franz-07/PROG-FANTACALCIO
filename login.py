import customtkinter as ctk
from tkinter import messagebox
import os
import random
import pyglet

pyglet.font.add_file("Poppins-Regular.ttf")

class SchermataLogin(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        ctk.CTkLabel(self, text="Nome utente:", font=("Poppins", 16)).grid(row=0, column=0, padx=20, pady=10, sticky="e")
        self.username_entry = ctk.CTkEntry(self, font=("Poppins", 16))
        self.username_entry.grid(row=0, column=1, padx=20, pady=10, sticky="w")
        self.username_entry.bind("<KeyRelease>", self.check_fields)

        ctk.CTkLabel(self, text="Password:", font=("Arial", 16)).grid(row=1, column=0, padx=20, pady=10, sticky="e")
        self.password_entry = ctk.CTkEntry(self, show="*", font=("Arial", 16))
        self.password_entry.grid(row=1, column=1, padx=20, pady=10, sticky="w")
        self.password_entry.bind("<KeyRelease>", self.check_fields)

        self.create_account_button = ctk.CTkButton(self, text="Non hai un account? Crealo ora!", command=self.create_account, width=200, font=("Arial", 12))
        self.create_account_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.login_button = ctk.CTkButton(self, text="Login", command=self.login, width=200, font=("Arial", 16), fg_color="red")
        self.login_button.grid(row=3, column=0, columnspan=2, pady=20)
        self.login_button.bind("<Enter>", self.move_button)

        self.error_label = ctk.CTkLabel(self, text="", text_color="red", font=("Arial", 14))
        self.error_label.grid(row=4, column=0, columnspan=2)

    def move_button(self, event):
        if not self.fields_filled():
            x = random.randint(0, 300)
            y = random.randint(0, 500)
            self.login_button.place(x=x, y=y)

    def reset_button_position(self):
        self.login_button.place(x=70, y=200)

    def check_fields(self, event):
        if self.fields_filled():
            self.reset_button_position()
            self.login_button.unbind("<Enter>")
            self.login_button.configure(fg_color="green")
        else:
            self.login_button.bind("<Enter>", self.move_button)
            self.login_button.configure(fg_color="red")

    def fields_filled(self):
        return bool(self.username_entry.get().strip()) and bool(self.password_entry.get().strip())

    def login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if not os.path.exists("user_data.txt"):
            self.error_label.configure(text="Nessun account registrato!")
            return

        with open("user_data.txt", "r") as file:
            users = [line.strip().split(",") for line in file.readlines()]

        for saved_username, saved_password in users:
            if username == saved_username:
                if password == saved_password:
                    messagebox.showinfo("Login", "Login effettuato con successo!")
                    self.error_label.configure(text="")
                    self.reset_button_position()
                    self.login_button.unbind("<Enter>")
                    self.master.mostra_schermata_home(username)
                    return
                else:
                    self.error_label.configure(text="Password errata")
                    return

        self.error_label.configure(text="Utente non trovato")

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
                    self.error_label.configure(text="Questo nome utente è già registrato")
                    return

        try:
            with open("user_data.txt", "a") as file:
                file.write(f"{username},{password}\n")
            messagebox.showinfo("Account", "Account creato con successo!")
            self.error_label.configure(text="")
        except Exception as e:
            messagebox.showerror("Errore", f"Errore durante la creazione dell'account: {e}")
