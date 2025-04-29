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
            self.img1 = ctk.CTkImage(Image.open("immagini/immagine1_lega.png"), size=(200, 200))
            self.img2 = ctk.CTkImage(Image.open("immagini/immagine2_lega.png"), size=(200, 200))
            self.img3 = ctk.CTkImage(Image.open("immagini/immagine3_lega.png"), size=(200, 200))
            self.img_cambiata = ctk.CTkImage(Image.open("immagini/immagine_cambiata.png"), size=(200, 200))

            # Creazione del frame per la disposizione orizzontale
            button_frame = ctk.CTkFrame(self)
            button_frame.pack(pady=20)

            # Bottone immagine sinistra
            ctk.CTkButton(button_frame, text="Inizia la partita", image=self.img1, command=self.lega1).pack(side="left", padx=10)

            # Bottone immagine centrale
            self.central_button = ctk.CTkButton(button_frame, text="Inizia la partita", image=self.img2, command=self.cambia_immagine_centrale)
            self.central_button.pack(side="left", padx=10)

            # Bottone immagine destra
            ctk.CTkButton(button_frame, text="Inizia la partita", image=self.img3, command=self.lega3).pack(side="left", padx=10)

        except Exception as e:
            ctk.CTkLabel(self, text=f"Errore nel caricamento delle immagini: {e}").pack()

    def cambia_immagine_centrale(self):
        # Cambia l'immagine del pulsante centrale
        self.central_button.configure(image=self.img_cambiata)


    def torna_home(self):
        self.master.mostra_schermata_home(self.username, self.giocatori, self.lega, False)
