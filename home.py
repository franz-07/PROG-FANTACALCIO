import tkinter as tk

class SchermataHome(tk.Frame):
    def __init__(self, master, username):
        super().__init__(master)
        tk.Label(self, text=f"Benvenuto, {username}!", font=("Arial", 20)).pack(pady=20)
        tk.Button(self, text="Logout", command=master.mostra_schermata_login).pack(pady=20)
