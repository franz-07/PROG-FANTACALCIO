import tkinter as tk
from tkinter import ttk, Tk, StringVar
from tkinter.ttk import Combobox
import customtkinter as ctk
from customtkinter import CTk, CTkFrame, CTkLabel, CTkButton, CTkScrollbar, CTkOptionMenu
from tkinter import ttk
import pyglet
from giocatori import giocatori
from PIL import Image
import random

class SchermataFormazione(ctk.CTkFrame):
    def __init__(self, master, giocatori, username, lega):
        super().__init__(master)
        self.master = master
        self.giocatori = giocatori
        self.username = username
        self.lega = lega
        self.formazione_selezionata = None

        ctk.set_appearance_mode("dark")

        # Titolo
        ctk.CTkLabel(self, text="Seleziona la Formazione", font=("Poppins", 20)).pack(pady=10)

        # Frame per le immagini delle formazioni
        self.frame_formazioni = ctk.CTkFrame(self)
        self.frame_formazioni.pack(pady=10)

        # Immagine Formazione 1
        self.img_formazione1 = ctk.CTkImage(Image.open("immagini/formazione1.png"), size=(200, 200))
        ctk.CTkButton(self.frame_formazioni, image=self.img_formazione1, text="1-3-4-3",
                      command=lambda: self.seleziona_formazione("1-3-4-3")).pack(side="left", padx=10)

        # Immagine Formazione 2
        self.img_formazione2 = ctk.CTkImage(Image.open("immagini/formazione2.png"), size=(200, 200))
        ctk.CTkButton(self.frame_formazioni, image=self.img_formazione2, text="1-3-4-1-2",
                      command=lambda: self.seleziona_formazione("1-3-4-1-2")).pack(side="left", padx=10)

        # Bottone per salvare la formazione
        ctk.CTkButton(self, text="Salva Formazione", command=self.salva_formazione).pack(pady=20)

    def seleziona_formazione(self, formazione):
        self.formazione_selezionata = formazione
        print(f"Formazione selezionata: {formazione}")

    def salva_formazione(self):
        if not self.formazione_selezionata:
            print("Nessuna formazione selezionata.")
            self.master.mostra_schermata_home(self.username, self.lega, genera_squadre=False)
            return

        try:
            # Aggiorna giocatori_data.txt con la formazione scelta
            with open("giocatori_data.txt", "r") as file:
                lines = []
                for line in file:
                    parts = line.strip().split(";")
                    if parts[0] == self.username:
                        giocatori_info = parts[2] if len(parts) > 2 else ""
                        lines.append(f"{self.username};{parts[1]};{giocatori_info};{self.formazione_selezionata}\n")
                    else:
                        lines.append(line)

            with open("giocatori_data.txt", "w") as file:
                file.writelines(lines)

            print(f"Formazione {self.formazione_selezionata} salvata con successo!")
            
            # Salva la formazione selezionata in un attributo condiviso
            self.master.formazione = self.formazione_selezionata

            # Torna alla schermata Home
            self.master.mostra_schermata_home(self.username, self.lega, genera_squadre=False, formazione=self.formazione_selezionata)

        except Exception as e:
            print(f"Errore nel salvataggio: {e}")

