import tkinter as tk
from tkinter import messagebox

class SchermataLogin(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        tk.Label(self, text="Nome utente:", font=("Arial", 16)).grid(row=0, column=0, padx=20, pady=10, sticky="e")
        self.username_entry = tk.Entry(self, font=("Arial", 16))
        self.username_entry.grid(row=0, column=1, padx=20, pady=10, sticky="w")

        tk.Label(self, text="Password:", font=("Arial", 16)).grid(row=1, column=0, padx=20, pady=10, sticky="e")
        self.password_entry = tk.Entry(self, show="*", font=("Arial", 16))
        self.password_entry.grid(row=1, column=1, padx=20, pady=10, sticky="w")

        self.create_account_button = tk.Button(self, text="Non hai un account? Crealo ora!", command=self.create_account, font=("Arial", 7), width=25)
        self.create_account_button.grid(row=2, column=0, columnspan=3, pady=5)

        self.login_button = tk.Button(self, text="Login", command=self.login, font=("Arial", 16), width=25)
        self.login_button.grid(row=3, column=0, columnspan=3, pady=20)

        self.error_label = tk.Label(self, text="", fg="red", font=("Arial", 14))
        self.error_label.grid(row=4, column=0, columnspan=3)

        self.create_account_button.bind("<Enter>", lambda e: self.create_account_button.config(fg="blue"))
        self.create_account_button.bind("<Leave>", lambda e: self.create_account_button.config(fg="black"))

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        try:
            with open("user_data.txt", "r") as file:
                users = file.readlines()
                for user in users:
                    saved_username, saved_password = user.strip().split(",")
                    if username == saved_username and password == saved_password:
                        messagebox.showinfo("Login", "Login effettuato con successo!")
                        return
            self.error_label.config(text="Nome utente o password errati", fg="red")
        except FileNotFoundError:
            self.error_label.config(text="File user_data.txt non trovato", fg="red")

    def create_account(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username and password:
            try:
                with open("user_data.txt", "a") as file:
                    file.write(f"{username},{password}\n")
                messagebox.showinfo("Account", "Account creato con successo!")
            except Exception as e:
                messagebox.showerror("Errore", f"Errore durante la creazione dell'account: {e}")
        else:
            messagebox.showwarning("Attenzione", "Inserisci un nome utente e una password validi.")
