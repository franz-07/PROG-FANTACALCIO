import customtkinter as ctk
from tkinter import messagebox
import random
from giocatori import giocatori  # Dizionario dei giocatori

class CreaLega(ctk.CTkFrame):
    def __init__(self, master, username):
        super().__init__(master)
        self.master = master
        self.username = username

        # Display username and logout button
        ctk.CTkLabel(self, text=f"Loggato come: {username}!", font=("Poppins", 12)).pack(anchor="ne", padx=5, pady=5)
        ctk.CTkButton(self, text="Torna alle leghe", command=self.esci).pack(anchor="ne", padx=5, pady=5)

        # Title label
        ctk.CTkLabel(self, text="Crea la tua lega", font=("Poppins", 28)).pack(pady=20)

        # Input for league name
        ctk.CTkLabel(self, text="Nome della lega:", font=("Poppins", 16)).pack(pady=5)
        self.nome_lega_entry = ctk.CTkEntry(self)
        self.nome_lega_entry.pack(pady=5)

        # Inputs for unique team names
        ctk.CTkLabel(self, text="Inserisci 8 nomi di squadre:", font=("Poppins", 16)).pack(pady=5)
        self.team_entries = []
        for i in range(8):  # Ora ci sono 8 squadre
            entry = ctk.CTkEntry(self)
            entry.pack(pady=2)
            self.team_entries.append(entry)

        # Button to create league
        ctk.CTkButton(self, text="Crea lega", command=self.crea_lega).pack(pady=10)

    def crea_lega(self):
        nome_lega = self.nome_lega_entry.get()
        squadre = [entry.get() for entry in self.team_entries]

        # Controllo: squadre devono avere nomi unici
        if len(set(squadre)) != len(squadre):
            messagebox.showerror("Errore", "I nomi delle squadre devono essere differenti")
            return

        if not nome_lega or any(not nome for nome in squadre):
            messagebox.showerror("Errore", "Compila tutti i campi!")
            return

        nomi_giocatori = list(giocatori.keys())  # Prendi solo i nomi dei giocatori

        if len(nomi_giocatori) < len(squadre) * 11:  # Controllo che ci siano abbastanza giocatori
            messagebox.showerror("Errore", "Numero insufficiente di giocatori!")
            return

        random.shuffle(nomi_giocatori)  # Mescoliamo i giocatori
        squadre_giocatori = {squadra: nomi_giocatori[i * 11:(i + 1) * 11] for i, squadra in enumerate(squadre)}

        dettagli_squadre = "\n".join([f"{squadra}: {', '.join(players)}" for squadra, players in squadre_giocatori.items()])
        messagebox.showinfo("Successo", f"Lega '{nome_lega}' creata!\n\n{dettagli_squadre}")

    def esci(self):
        self.master.mostra_schermata_leghe(self.username)
