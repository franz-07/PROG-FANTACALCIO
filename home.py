import tkinter as tk
from tkinter import ttk, Tk, StringVar
from tkinter.ttk import Combobox
import customtkinter as ctk
from customtkinter import CTk, CTkFrame, CTkLabel, CTkButton, CTkScrollbar, CTkOptionMenu
from tkinter import ttk

class SchermataHome(ctk.CTkFrame):
    def __init__(self, master, username, giocatori):
        super().__init__(master)
        self.master = master
        
        ctk.CTkLabel(self, text=f"Loggato come: {username}!", font=("Arial", 10)).pack(anchor="ne", padx=5, pady=5)
        ctk.CTkButton(self, text="Esci", command=master.mostra_schermata_login).pack(anchor="ne", padx=5, pady=5)

        self.menu_tendina()
        self.tabella_giocatori(giocatori)

    def tabella_giocatori(self, giocatori):
        colonne = ("Nome", "Squadra", "Ruoli", "Numero Maglia", "SI/NO")
        frame_tabella = ctk.CTkFrame(self)
        frame_tabella.pack(fill="both", expand=True, padx=10, pady=10)

        tabella = ttk.Treeview(frame_tabella, columns=colonne, show="headings")
        for colonna in colonne:
            tabella.heading(colonna, text=colonna)

        for nome, dati in giocatori.items():
            tabella.insert('', 'end', values=(nome, *dati))

        tabella.pack(side="left", fill="both", expand=True)

        scrollbar = ctk.CTkScrollbar(frame_tabella, orientation="vertical", command=tabella.yview)
        scrollbar.pack(side="right", fill="y")
        tabella.configure(yscrollcommand=scrollbar.set)

    def menu_tendina(self):
        self.larghezza_menu = 200
        self.menu_aperto = False

        self.bottone_menu = ctk.CTkButton(self, text="Home", command=self.toggle_menu)
        self.bottone_menu.pack(anchor="nw", padx=10, pady=10)

        self.frame_menu = ctk.CTkFrame(self, fg_color="teal", width=self.larghezza_menu)
        self.frame_menu.pack_propagate(False)
        self.frame_menu.place(x=-self.larghezza_menu, y=0)

        ctk.CTkLabel(self.frame_menu, text="Menu", font=("Arial", 16), text_color="white").pack(pady=10)
        ctk.CTkButton(self.frame_menu, text="Pagina 1", command=lambda: self.seleziona_opzione("Pagina 1")).pack(fill="x", pady=5)
        ctk.CTkButton(self.frame_menu, text="Pagina 2", command=lambda: self.seleziona_opzione("Pagina 2")).pack(fill="x", pady=5)
        ctk.CTkButton(self.frame_menu, text="Pagina 3", command=lambda: self.seleziona_opzione("Pagina 3")).pack(fill="x", pady=5)

    def toggle_menu(self):
        if self.menu_aperto:
            self.frame_menu.place(x=-self.larghezza_menu, y=0)
            self.menu_aperto = False
        else:
            self.frame_menu.place(x=0, y=0)
            self.menu_aperto = True

    def seleziona_opzione(self, opzione):
        print(f"Hai selezionato: {opzione}")
        self.toggle_menu()
