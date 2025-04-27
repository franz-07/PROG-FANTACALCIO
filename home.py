import tkinter as tk
from tkinter import ttk, Tk, StringVar
from tkinter.ttk import Combobox
import customtkinter as ctk
from customtkinter import CTk, CTkFrame, CTkLabel, CTkButton, CTkScrollbar, CTkOptionMenu
from tkinter import ttk
import pyglet
from giocatori import giocatori
from PIL import Image


class SchermataHome(ctk.CTkFrame):
    def __init__(self, master, username, giocatori, lega):
        super().__init__(master)
        self.master = master
        ctk.set_appearance_mode("dark")

        # Displaying the user information and logout button
        ctk.CTkLabel(self, text=f"Loggato come: {username}!", font=("Poppins", 10)).pack(anchor="ne", padx=5, pady=5)
        ctk.CTkButton(self, text="Esci", command=self.logout).pack(anchor="ne", padx=5, pady=5)

        nomi_lega = {
            "lega1": "Lega 10",
            "lega2": "Lega 5"
        }
        nome_visibile = nomi_lega.get(lega, lega)  # Se non trova, mostra il nome originale

        ctk.CTkLabel(self, text=f"Benvenuto nella {nome_visibile}!", font=("Poppins", 20)).pack(pady=10)


        # Displaying the league image
        self.mostra_immagine_lega(lega)

        # Calling the function for the dropdown menu
        self.menu_tendina()

    def mostra_immagine_lega(self, lega):
        if lega == "lega1":
            immagine_path = "immagini/immagine1_lega.png"
        elif lega == "lega2":
            immagine_path = "immagini/immagine2_lega.png"
        else:
            return

        try:
            img = Image.open(immagine_path)
            self.img = ctk.CTkImage(img, size=(200, 200))  # ✅ usa CTkImage

            label_immagine = ctk.CTkLabel(self, image=self.img, text="")
            label_immagine.pack(pady=20)

        except Exception as e:
            ctk.CTkLabel(self, text=f"Errore caricamento immagine: {e}").pack()


    def tabella_giocatori(self):
        colonne = ("Nome", "Squadra", "Ruoli", "Numero Maglia", "SI/NO")
        self.frame_tabella = ctk.CTkFrame(self)
        self.frame_tabella.pack(fill="none", expand=True, padx=10, pady=10)

        # Croce per chiudere la tabella
        ctk.CTkButton(self.frame_tabella, text="X", command=self.chiudi_tabella, width=30).pack(anchor="ne", padx=5, pady=5)

        tabella = ttk.Treeview(self.frame_tabella, columns=colonne, show="headings")
        for colonna in colonne:
            tabella.heading(colonna, text=colonna)

        for nome, dati in giocatori.items():
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

        # Creazione del bottone menu in alto a sinistra
        self.bottone_menu = ctk.CTkButton(self, text="Menu", command=self.aprichhiudi_menu)
        self.bottone_menu.place(x=0, y=0)

        # Frame menu
        self.frame_menu = ctk.CTkFrame(self, width=self.larghezza_menu, height=self.master.winfo_height())
        self.frame_menu.pack_propagate(False)
        self.frame_menu.place(x=-self.larghezza_menu, y=0)

        # Crocetta per chiudere il menu
        ctk.CTkButton(self.frame_menu, text="X", command=self.chiudi_menu, width=30).pack(anchor="ne", padx=5, pady=5)

        # Titolo
        ctk.CTkLabel(self.frame_menu, text="Menu", font=("Poppins", 16), text_color="white").pack(pady=10)

        # Pulsante per la tabella
        ctk.CTkButton(self.frame_menu, text="Giocatori", command=self.aprichiudi_tabella_giocatori).pack(fill="x", pady=5)

        # Aggiungi i nuovi bottoni
        ctk.CTkButton(self.frame_menu, text="Mercato", command=self.apri_mercato).pack(fill="x", pady=5)
        ctk.CTkButton(self.frame_menu, text="Partite").pack(fill="x", pady=5)
        ctk.CTkButton(self.frame_menu, text="Giornali").pack(fill="x", pady=5)
        ctk.CTkButton(self.frame_menu, text="Formazione").pack(fill="x", pady=5)

    def aprichhiudi_menu(self):
        if self.menu_aperto:
            self.frame_menu.place(x=-self.larghezza_menu, y=0)
        else:
            self.frame_menu.place(x=0, y=0)
        self.menu_aperto = not self.menu_aperto

    def chiudi_menu(self):
        self.frame_menu.place(x=-self.larghezza_menu, y=0)
        self.menu_aperto = False

    def aprichiudi_tabella_giocatori(self):
        if self.tabella_visibile:
            self.chiudi_tabella()
        else:
            self.tabella_giocatori()

    def chiudi_tabella(self):
        if self.frame_tabella:
            self.frame_tabella.destroy()
            self.frame_tabella = None
        self.tabella_visibile = False

    def apri_mercato(self):
        self.master.mostra_schermata_mercato()

    def logout(self):
        self.master.mostra_schermata_login()
