import tkinter as tk
from tkinter import messagebox

# Funzione per verificare il login
def login():
    username = username_entry.get()
    password = password_entry.get()
    try:
        with open("user_data.txt", "r") as file:
            users = file.readlines()
            for user in users:
                saved_username, saved_password = user.strip().split(",")
                if username == saved_username and password == saved_password:
                    messagebox.showinfo("Login", "Login effettuato con successo!")
                    return
        error_label.config(text="Nome utente o password errati", fg="red")
    except FileNotFoundError:
        error_label.config(text="File user_data.txt non trovato", fg="red")

# Funzione per creare un nuovo account
def create_account():
    username = username_entry.get()
    password = password_entry.get()
    if username and password:
        try:
            with open("user_data.txt", "a") as file:
                file.write(f"{username},{password}\n")
            messagebox.showinfo("Account", "Account creato con successo!")
        except Exception as e:
            messagebox.showerror("Errore", f"Errore durante la creazione dell'account: {e}")
    else:
        messagebox.showwarning("Attenzione", "Inserisci un nome utente e una password validi.")

# Funzione per cambiare il colore del bottone al passaggio del mouse
def on_enter(event):
    create_account_button.config(fg="blue")

def on_leave(event):
    create_account_button.config(fg="black")

# Creazione della finestra principale
root = tk.Tk()
root.title("Alchemist Fantacalcio - Login")
root.geometry("450x700")  # Imposta la dimensione della finestra
root.resizable(False, False)  # Disabilita il ridimensionamento della finestra

# Etichetta e campo di input per il nome utente
tk.Label(root, text="Nome utente:", font=("Arial", 16)).grid(row=0, column=0, padx=20, pady=10, sticky="e")
username_entry = tk.Entry(root, font=("Arial", 16))
username_entry.grid(row=0, column=1, padx=20, pady=10, sticky="w")

# Etichetta e campo di input per la password
tk.Label(root, text="Password:", font=("Arial", 16)).grid(row=1, column=0, padx=20, pady=10, sticky="e")
password_entry = tk.Entry(root, show="*", font=("Arial", 16))
password_entry.grid(row=1, column=1, padx=20, pady=10, sticky="w")

# Bottone per creare un account
create_account_button = tk.Button(root, text="Non hai un account? Crealo ora!", command=create_account, font=("Arial", 7), width=25)
create_account_button.grid(row=2, column=0, columnspan=3, pady=5)

# Bottone per il login
login_button = tk.Button(root, text="Login", command=login, font=("Arial", 16), width=25)
login_button.grid(row=3, column=0, columnspan=3, pady=20)

# Etichetta per mostrare errori
error_label = tk.Label(root, text="", fg="red", font=("Arial", 14))
error_label.grid(row=4, column=0, columnspan=3)

# Aggiunta degli eventi per il cambio colore del bottone
create_account_button.bind("<Enter>", on_enter)
create_account_button.bind("<Leave>", on_leave)

# Avvio del loop principale
root.mainloop()
