import customtkinter as ctk
from tkinter import messagebox
import os
import random
import pyglet
from PIL import Image
from giocatori import giocatori

pyglet.font.add_file("Poppins-Regular.ttf")

class SchermataLogin(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.resetta_giocatori_disponibili()
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=1)

        logo_image = ctk.CTkImage(light_image=Image.open("fantalclogo.png"), size=(180, 81))
        self.logo_label = ctk.CTkLabel(self, image=logo_image, text="")
        self.logo_label.place(relx=0.5, rely=0.15, anchor="center")

        self.frame_centrale = ctk.CTkFrame(self)
        self.frame_centrale.place(relx=0.5, rely=0.4, anchor="center")

        ctk.CTkLabel(self.frame_centrale, text="Nome utente:", font=("Poppins", 16)).grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.username_entry = ctk.CTkEntry(self.frame_centrale, font=("Poppins", 16))
        self.username_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        self.username_entry.bind("<KeyRelease>", self.check_fields)

        ctk.CTkLabel(self.frame_centrale, text="Password:", font=("Poppins", 16)).grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.password_entry = ctk.CTkEntry(self.frame_centrale, show="*", font=("Poppins", 16))
        self.password_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        self.password_entry.bind("<KeyRelease>", self.check_fields)

        self.create_account_button = ctk.CTkButton(
            self.frame_centrale,
            text="Non hai un account? Crealo ora!",
            command=self.master.mostra_schermata_registra,
            width=200, font=("Arial", 12))
        self.create_account_button.grid(row=2, column=0, columnspan=2, pady=20)

        self.error_label = ctk.CTkLabel(self.frame_centrale, text="", text_color="red", font=("Poppins", 14))
        self.error_label.grid(row=3, column=0, columnspan=2)

        self.login_button = ctk.CTkButton(
            self,
            text="Login",
            command=self.login,
            width=200,
            font=("Poppins", 16),
            fg_color="red")
        self.login_button.place(relx=0.5, rely=0.75, anchor="center")
        self.login_button.bind("<Enter>", self.move_button)

        self.login_button_original_pos = (0.5, 0.75)

    def move_button(self, event):
        if not self.fields_filled():
            new_x = random.uniform(0.1, 0.9)
            new_y = random.uniform(0.6, 0.9)
            self.login_button.place(relx=new_x, rely=new_y, anchor="center")

    def reset_button_position(self):
        self.login_button.place(relx=self.login_button_original_pos[0], rely=self.login_button_original_pos[1], anchor="center")

    def check_fields(self, event=None):
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
                    self.master.mostra_schermata_leghe(username)
                    return
                else:
                    self.error_label.configure(text="Password errata")
                    return

        self.error_label.configure(text="Utente non trovato")

    def resetta_giocatori_disponibili(self):
        print("Resetting stato giocatori...")  # Messaggio di debug
        for giocatore in giocatori:
            giocatori[giocatore][3] = "SI"  # Rendi tutti i giocatori disponibili
        self.aggiorna_file_giocatori()

    def aggiorna_file_giocatori(self):
        with open("giocatori.py", "w") as file:
            file.write("giocatori = {\n")
            for nome, dati in giocatori.items():
                file.write(f'    "{nome}": {dati},\n')
            file.write("}\n")
