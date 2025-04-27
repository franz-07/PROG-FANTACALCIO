import customtkinter as ctk
import os
from tkinter import ttk
from tkinter import messagebox
from giocatori import giocatori

class SchermataMercato(ctk.CTkFrame):
    def __init__(self, master, username, giocatori_dict, lega):
        super().__init__(master)
        self.master = master
        ctk.set_appearance_mode("dark")

        self.username = username
        self.lega = lega
        self.giocatori_dict = giocatori_dict
        
        self.carica_dati_utente()

        # Barra in alto
        top_frame = ctk.CTkFrame(self)
        top_frame.pack(fill="x", padx=10, pady=10)

        self.label_budget = ctk.CTkLabel(top_frame, text=f"Budget: {self.budget}", font=("Poppins", 16))
        self.label_budget.pack(side="left", padx=5)

        ctk.CTkButton(top_frame, text="Torna alla Home", command=self.torna_home).pack(side="right", padx=5)

        # Barra di ricerca
        search_frame = ctk.CTkFrame(self)
        search_frame.pack(fill="x", padx=10)

        self.search_var = ctk.StringVar()
        search_entry = ctk.CTkEntry(search_frame, textvariable=self.search_var, placeholder_text="Cerca giocatore...")
        search_entry.pack(side="left", fill="x", expand=True, padx=5, pady=5)
        search_entry.bind("<Return>", lambda e: self.cerca_giocatore())  # Ricerca con Enter

        search_button = ctk.CTkButton(search_frame, text="Cerca", command=self.cerca_giocatore)
        search_button.pack(side="right", padx=5)

        # Tabella giocatori
        self.tabella_frame = ctk.CTkFrame(self)
        self.tabella_frame.pack(fill="both", expand=True, padx=10, pady=10)

        colonne = ("Nome", "Squadra", "Ruolo", "Prezzo", "Stato")
        self.tree = ttk.Treeview(self.tabella_frame, columns=colonne, show="headings")
        
        # Configura le colonne
        for col in colonne:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120 if col != "Nome" else 150)

        self.tree.pack(fill="both", expand=True)
        self.tree.bind("<Double-1>", self.compra_giocatore)  # Binding del doppio click
        
        # Stili per la treeview
        style = ttk.Style()
        style.configure("Treeview", rowheight=25)
        style.configure("Treeview.Heading", font=('Poppins', 10, 'bold'))
        
        self.riempi_tabella(self.giocatori_dict)

    def carica_dati_utente(self):
            """Carica budget e giocatori acquistati da giocatori_data.txt"""
            self.budget = 50  # Default
            self.giocatori_comprati = []
            
            try:
                if not os.path.exists("giocatori_data.txt"):
                    return
                    
                with open("giocatori_data.txt", "r") as file:
                    for line in file:
                        parts = line.strip().split(";")
                        if parts[0] == self.username:
                            self.budget = int(parts[1])
                            if len(parts) > 2 and parts[2]:
                                self.giocatori_comprati = parts[2].split(",")
                            break
            except Exception as e:
                print(f"Errore caricamento dati giocatore: {e}")

    def riempi_tabella(self, dati):
        for i in self.tree.get_children():
            self.tree.delete(i)
        
        for nome, info in dati.items():
            squadra, ruolo, prezzo, disponibile = info
            stato = "Acquistato" if nome in self.giocatori_comprati else "Disponibile" if disponibile == "SI" else "Non disponibile"
            
            self.tree.insert('', 'end', values=(nome, squadra, ruolo, prezzo, stato), 
                           tags=('acquistato' if stato == "Acquistato" else ''))

        # Configura stili
        self.tree.tag_configure('acquistato', background='#2e8b57', foreground='white')

    def cerca_giocatore(self):
        ricerca = self.search_var.get().lower()
        filtrati = {nome: dati for nome, dati in self.giocatori_dict.items() 
                   if ricerca in nome.lower() and (dati[3] == "SI" or nome in self.giocatori_comprati)}
        self.riempi_tabella(filtrati)

    def compra_giocatore(self, event):
        selected = self.tree.selection()
        if not selected:
            return

        item = self.tree.item(selected)
        nome, squadra, ruolo, prezzo_str, stato = item['values']
        
        if stato != "Disponibile":
            messagebox.showwarning("Attenzione", "Questo giocatore non è acquistabile!")
            return
            
        try:
            prezzo = int(prezzo_str)
        except ValueError:
            messagebox.showerror("Errore", "Prezzo non valido")
            return
            
        if self.budget >= prezzo:
            self.budget -= prezzo
            self.giocatori_comprati.append(nome)
            self.giocatori_dict[nome][3] = "NO"  # Marca come non disponibile
            
            self.label_budget.configure(text=f"Budget: {self.budget}")
            messagebox.showinfo("Acquisto", f"Hai acquistato {nome} per {prezzo} crediti!")
            self.salva_acquisti()
            self.riempi_tabella(self.giocatori_dict)
        else:
            messagebox.showerror("Errore", "Budget insufficiente!")

    def salva_acquisti(self):
            try:
                lines = []
                user_found = False
                
                # Leggi il file esistente se c'è
                if os.path.exists("giocatori_data.txt"):
                    with open("giocatori_data.txt", "r") as file:
                        for line in file:
                            parts = line.strip().split(";")
                            if parts[0] == self.username:
                                # Sostituisci la riga esistente
                                lines.append(f"{self.username};{self.budget};{','.join(self.giocatori_comprati)}\n")
                                user_found = True
                            else:
                                lines.append(line)
                
                # Se utente non trovato, aggiungi nuova riga
                if not user_found:
                    lines.append(f"{self.username};{self.budget};{','.join(self.giocatori_comprati)}\n")
                
                # Scrivi tutto il file
                with open("giocatori_data.txt", "w") as file:
                    file.writelines(lines)
                    
            except Exception as e:
                messagebox.showerror("Errore", f"Errore nel salvataggio: {str(e)}")

    def torna_home(self):
        self.master.mostra_schermata_home(self.username, self.lega)