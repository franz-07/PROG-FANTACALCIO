import tkinter as tk
from tkinter import ttk, Tk, StringVar
from tkinter.ttk import Combobox
import customtkinter as ctk
from customtkinter import CTk, CTkFrame, CTkLabel, CTkButton, CTkScrollbar, CTkOptionMenu
from tkinter import ttk
import pyglet
from giocatori import giocatori

pyglet.font.add_file("Poppins-Regular.ttf")

class SchermataHome(ctk.CTkFrame):
    def __init__(self, master, username, giocatori, lega):
        super().__init__(master)
        self.master = master
        ctk.set_appearance_mode("dark")
        ctk.CTkLabel(self, text=f"Loggato come: {username}!", font=("Poppins", 10)).pack(anchor="ne", padx=5, pady=5)
        ctk.CTkButton(self, text="Esci", command=self.logout).pack(anchor="ne", padx=5, pady=5)

        ctk.CTkLabel(self, text=f"lega: {lega}!", font=("Poppins", 10)).pack(anchor="ne", padx=5, pady=5)

        self.menu_tendina()

    def tabella_giocatori(self):
        colonne = ("Nome", "Squadra", "Ruoli", "Numero Maglia", "SI/NO")
        self.frame_tabella = ctk.CTkFrame(self)
        self.frame_tabella.pack(fill="none", expand=True, padx=10, pady=10)

        # croce per chiudere la tabella
        ctk.CTkButton(self.frame_tabella, text="X", command=self.chiudi_tabella, width=30).pack(anchor="ne", padx=5, pady=5)

        tabella = ttk.Treeview(self.frame_tabella, columns=colonne, show="headings") #treewiew crea la struttura ad albero o in una tabella (da noi la tabella)
        for colonna in colonne:
            tabella.heading(colonna, text=colonna)

        for nome, dati in giocatori.items():  #prendo valori che il file giocatori contenga dati_giocatori
            tabella.insert('', 'end', values=(nome, *dati))

        tabella.pack(side="left", fill="none", expand=True)

        scrollbar = ctk.CTkScrollbar(self.frame_tabella, orientation="vertical", command=tabella.yview)
        scrollbar.pack(side="right", fill="y")
        tabella.configure(yscrollcommand=scrollbar.set)
        self.tabella_visibile = True

    def menu_tendina(self):
        self.larghezza_menu = 200
        self.menu_aperto = False
        self.tabella_visibile = False

        # creazione del ottone menu in alto a sinistra
        self.bottone_menu = ctk.CTkButton(self, text="Menu", command=self.aprichhiudi_menu)  #collega alla funzione dell'apertura chiusura del menu
        self.bottone_menu.place(x=0, y=0)

        #frame menu
        self.frame_menu = ctk.CTkFrame(self, width=self.larghezza_menu, height=self.master.winfo_height())
        self.frame_menu.pack_propagate(False)
        self.frame_menu.place(x=-self.larghezza_menu, y=0)

        #crocetta per chiudere il menu
        ctk.CTkButton(self.frame_menu, text="X", command=self.chiudi_menu, width=30).pack(anchor="ne", padx=5, pady=5)

        #titolo
        ctk.CTkLabel(self.frame_menu, text="Menu", font=("Poppins", 16), text_color="white").pack(pady=10)

        #pulsante per la tabella
        ctk.CTkButton(self.frame_menu, text="Giocatori", command=self.aprichiudi_tabella_giocatori).pack(fill="x", pady=5) #collego il pulsante alla funzione aprichiudi tabella

    def aprichhiudi_menu(self):
        if self.menu_aperto:
            self.frame_menu.place(x=-self.larghezza_menu, y=0)
        else:
            self.frame_menu.place(x=0, y=0)
        self.menu_aperto = not self.menu_aperto

    def chiudi_menu(self):
        #chiude solo il menu ma non influenzando la tabella
        self.frame_menu.place(x=-self.larghezza_menu, y=0)
        self.menu_aperto = False

    def aprichiudi_tabella_giocatori(self):
        if self.tabella_visibile:
            #chiude la tabella se già visibile
            self.chiudi_tabella()
        else:
            #fa vedere la tabella se non gia aperta
            self.tabella_giocatori()

    def chiudi_tabella(self):
        #chiude la tabella
        if self.frame_tabella:
            self.frame_tabella.destroy()
            self.frame_tabella = None
        self.tabella_visibile = False

    def logout(self):
        self.master.mostra_schermata_login()
#letszgohsky #flezz