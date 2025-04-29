import customtkinter as ctk
from tkinter import ttk
import os

class SchermataGiornali(ctk.CTkFrame):
    def __init__(self, master, username, lega):
        super().__init__(master)
        self.master = master
        self.username = username
        self.lega = lega

        # Barra superiore con nome utente
        top_bar = ctk.CTkFrame(self)
        top_bar.pack(fill="x", pady=5, padx=5)

        ctk.CTkLabel(top_bar, text=f"Loggato come: {username}", font=("Poppins", 12)).pack(side="left", padx=5)

        # Titolo della schermata
        ctk.CTkLabel(self, text=f"Risultati per {username} nella lega {lega}", font=("Poppins", 16, "bold")).pack(pady=10)

        # Tabella per mostrare i risultati
        self.tabella_frame = ctk.CTkFrame(self)
        self.tabella_frame.pack(fill="both", expand=True, padx=20, pady=20)

        self.tabella = ttk.Treeview(self.tabella_frame, columns=("Squadra", "Gol", "Assist", "Autogol", "Gialli", "Rossi", "Punteggio"), show="headings")
        self.tabella.pack(fill="both", expand=True)

        # Intestazioni della tabella
        self.tabella.heading("Squadra", text="Squadra")
        self.tabella.heading("Gol", text="Gol")
        self.tabella.heading("Assist", text="Assist")
        self.tabella.heading("Autogol", text="Autogol")
        self.tabella.heading("Gialli", text="Cartellini Gialli")
        self.tabella.heading("Rossi", text="Cartellini Rossi")
        self.tabella.heading("Punteggio", text="Punteggio")

        # Stile della tabella
        style = ttk.Style()
        style.configure("Treeview", rowheight=25)
        style.configure("Treeview.Heading", font=("Poppins", 10, "bold"))

        # Carica i risultati dal file
        self.carica_risultati()

        # Pulsante per tornare alla schermata precedente
        ctk.CTkButton(self, text="Torna alla Home", command=self.torna_home).pack(pady=10)

    def carica_risultati(self):
        # Nome del file basato sull'utente e sulla lega
        filename = f"risultati_{self.username}_{self.lega}.txt"
        if not os.path.exists(filename):
            ctk.CTkLabel(self, text="Nessun risultato trovato.", font=("Poppins", 12)).pack(pady=10)
            return

        # Legge i risultati dal file
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()

        # Processa i risultati e li aggiunge alla tabella
        current_team = None
        team_data = {}
        for line in lines:
            line = line.strip()
            if line.startswith("Squadra A") or line.startswith("Squadra B"):
                current_team = line[:-1]
                team_data[current_team] = {}
            elif ": " in line and current_team:
                key, value = line.split(": ")
                team_data[current_team][key] = value
            elif line == "":
                # Aggiunge i dati alla tabella quando finisce una squadra
                if current_team and current_team in team_data:
                    self.tabella.insert("", "end", values=(
                        current_team,
                        team_data[current_team].get("Gol", "0"),
                        team_data[current_team].get("Assist", "0"),
                        team_data[current_team].get("Autogol", "0"),
                        team_data[current_team].get("Cartellini gialli", "0"),
                        team_data[current_team].get("Cartellini rossi", "0"),
                        team_data[current_team].get("Punteggio", "0")
                    ))
                current_team = None

    def torna_home(self):
        self.master.mostra_schermata_home(self.username, self.lega, genera_squadre=False)

# Esempio di utilizzo
if __name__ == "__main__":
    class App(ctk.CTk):
        def __init__(self):
            super().__init__()
            self.geometry("800x600")
            self.title("Giornali Test")
            frame = SchermataGiornali(self, "utente_test", "lega_test")
            frame.pack(fill="both", expand=True)

    app = App()
    app.mainloop()