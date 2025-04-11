import tkinter as tk
from tkinter import ttk

class SchermataHome(tk.Frame):
    def __init__(self, master, username, giocatori):
        super().__init__(master)
        tk.Label(self, text=f"Loggato come:{username}!", font=("Arial", 10)).pack(anchor="ne", padx=5, pady=5)
        tk.Button(self, text="Esci", command=master.mostra_schermata_login).pack(anchor="ne", padx=5, pady=5)       #anchor per definire una posizione a livello generale
        
        self.tabella_giocatori(giocatori)

    def tabella_giocatori(self, giocatori):
        colonne = ("Nome", "Squadra", "Ruoli", "Numero Maglia", "SI/NO")
        tabella = ttk.Treeview(self, columns=colonne, show="headings")
        tabella.pack(fill="none", expand=True, padx=10, pady=10)
        
        frame_tabella = tk.Frame(self)
        frame_tabella.pack(fill="both", expand=True, padx=10, pady=10)

        for colonna in colonne:
            tabella.heading(colonna, text=colonna)
            
        for nome, dati in giocatori.items():
            tabella.insert('','end', values=(nome,*dati)) #per ogni nome in tutti gli elementi della lista di dizionari mette nella tabella e scrivera il nome per tutti i valori presenti
        
        tabella.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(frame_tabella, orient="vertical", command=tabella.yview)
        scrollbar.pack(side="right", fill="y")  # Posizionata accanto alla tabella e lunga quanto la tabella
        tabella.configure(yscrollcommand=scrollbar.set)
