# mercato.py
import customtkinter as ctk
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
        self.budget = 500
        self.giocatori_dict = giocatori_dict
        self.giocatori_comprati = []

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

        search_button = ctk.CTkButton(search_frame, text="Cerca", command=self.cerca_giocatore)
        search_button.pack(side="right", padx=5)

        # Tabella giocatori
        self.tabella_frame = ctk.CTkFrame(self)
        self.tabella_frame.pack(fill="both", expand=True, padx=10, pady=10)

        colonne = ("Nome", "Squadra", "Ruolo", "Prezzo", "Disponibile")
        self.tree = ttk.Treeview(self.tabella_frame, columns=colonne, show="headings")
        for col in colonne:
            self.tree.heading(col, text=col)

        self.tree.pack(fill="both", expand=True)

        self.riempi_tabella(self.giocatori_dict)

    def riempi_tabella(self, dati):
        for i in self.tree.get_children():
            self.tree.delete(i)

        for nome, info in dati.items():
            squadra, ruolo, prezzo, disponibile = info
            if disponibile == "NO":
                self.tree.insert('', 'end', values=(nome, squadra, ruolo, prezzo, "Disponibile"))

        self.tree.bind("<Double-1>", self.compra_giocatore)

    def cerca_giocatore(self):
        ricerca = self.search_var.get().lower()
        filtrati = {nome: dati for nome, dati in self.giocatori_dict.items() if ricerca in nome.lower() and dati[3] == "NO"}
        self.riempi_tabella(filtrati)

    def compra_giocatore(self, event):
        selected = self.tree.selection()
        if not selected:
            return

        item = self.tree.item(selected)
        nome, squadra, ruolo, prezzo, disponibile = item['values']

        if self.budget >= prezzo:
            self.budget -= prezzo
            self.label_budget.configure(text=f"Budget: {self.budget}")
            messagebox.showinfo("Acquisto", f"Hai acquistato {nome} per {prezzo} crediti!")

            self.giocatori_dict[nome][3] = "SI"
            self.giocatori_comprati.append(nome)
            self.salva_acquisti()
            self.riempi_tabella(self.giocatori_dict)
        else:
            messagebox.showerror("Errore", "Budget insufficiente per acquistare questo giocatore.")

    def salva_acquisti(self):
        try:
            with open("user_data.txt", "r") as file:
                righe = file.readlines()

            nuove_righe = []
            for riga in righe:
                parti = riga.strip().split()
                if not parti:
                    continue
                if parti[0] == self.username:
                    if "giocatori_comprati:" in riga:
                        index = riga.index("giocatori_comprati:")
                        nuova_riga = riga[:index] + f"giocatori_comprati: {','.join(self.giocatori_comprati)}\n"
                    else:
                        nuova_riga = riga.strip() + f" giocatori_comprati: {','.join(self.giocatori_comprati)}\n"
                    nuove_righe.append(nuova_riga)
                else:
                    nuove_righe.append(riga)

            with open("user_data.txt", "w") as file:
                file.writelines(nuove_righe)

        except Exception as e:
            messagebox.showerror("Errore", f"Errore salvataggio acquisti: {e}")

    def torna_home(self):
        self.master.mostra_schermata_home(self.username, self.lega)
