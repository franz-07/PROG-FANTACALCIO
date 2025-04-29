import tkinter as tk
from PIL import Image, ImageTk
import customtkinter as ctk


class SchermataSimulazione(ctk.CTkFrame):
        
    def __init__(self, master, username, giocatori, lega):
        super().__init__(master)
        self.master = master
        self.username = username
        self.giocatori = giocatori
        self.lega = lega
        

        ctk.CTkLabel(self, text=f"Loggato come: {username} in lega {lega}!", font=("Poppins", 12)).pack(anchor="ne", padx=5, pady=5)

        ctk.CTkButton(self, text="Torna alla home", command=self.torna_home).pack(anchor="ne", padx=5, pady=5)

        ctk.CTkLabel(self, text="Partita in corso..", font=("Poppins", 24, "bold")).pack(pady=20)

        self.mostra_immagini()
    
    def mostra_immagini(self):
        try:
            # Caricamento delle immagini
            self.img_left = ctk.CTkImage(Image.open("immagini/Squadra1.png"), size=(200, 200))
            self.img_right = ctk.CTkImage(Image.open("immagini/Squadra2.png"), size=(200, 200))
            self.img_center_1 = ctk.CTkImage(Image.open("immagini/start.png"), size=(200, 200))
            self.img_center_2 = ctk.CTkImage(Image.open("immagini/finished.png"), size=(200, 200))

            # Disposizione delle immagini laterali
            self.left_label = ctk.CTkLabel(self, text="", image=self.img_left)
            self.left_label.pack(side="left", padx=20, pady=20)

            self.right_label = ctk.CTkLabel(self, text="", image=self.img_right)
            self.right_label.pack(side="right", padx=20, pady=20)

            # Immagine centrale (iniziale)
            self.center_label = ctk.CTkLabel(self, text="", image=self.img_center_1)
            self.center_label.pack(pady=10)

            # Bottone sotto l'immagine centrale
            self.center_button = ctk.CTkButton(self, text="Inizia partita", command=self.cambia_immagine)
            self.center_button.pack(pady=10)

        except Exception as e:
            ctk.CTkLabel(self, text=f"Errore nel caricamento delle immagini: {e}").pack()

    def cambia_immagine(self):
    
        # Aspetta 3 secondi per cambiare alla prima immagine
        self.master.after(3000, lambda: self.center_label.configure(image=self.img_center_2))



    def torna_home(self):
        self.master.mostra_schermata_home(self.username, self.giocatori, self.lega, False)
