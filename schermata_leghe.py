import random
import customtkinter as ctk
from PIL import Image
from giocatori import giocatori  # File contenente i giocatori

class SchermataLeghe(ctk.CTkFrame):
    def __init__(self, master, username):
        super().__init__(master)
        self.master = master
        self.username = username

        ctk.CTkLabel(self, text=f"Loggato come: {username}!", font=("Poppins", 12)).pack(anchor="ne", padx=5, pady=5)
        ctk.CTkButton(self, text="Esci", command=self.logout).pack(anchor="ne", padx=5, pady=5)

        ctk.CTkLabel(self, text="Scegli la tua lega", font=("Poppins", 24, "bold")).pack(pady=20)

        self.mostra_immagini()


    def mostra_immagini(self):
        try:
            # Creazione delle immagini
            img1 = ctk.CTkImage(Image.open("immagini/immagine1_lega.png"), size=(200, 200))
            img2 = ctk.CTkImage(Image.open("immagini/immagine2_lega.png"), size=(200, 200))
            img3 = ctk.CTkImage(Image.open("immagini/immagine3_lega.png"), size=(200, 200))

            # Disposizione orizzontale delle immagini/bottoni
            button_frame = ctk.CTkFrame(self)  # Frame principale per i bottoni
            button_frame.pack(pady=20)

            ctk.CTkButton(button_frame, text="", image=img1, command=self.lega1).pack(side="left", padx=10)
            ctk.CTkButton(button_frame, text="", image=img2, command=self.lega2).pack(side="left", padx=10)
            ctk.CTkButton(button_frame, text="", image=img3, command=self.lega3).pack(side="left", padx=10)

        except Exception as e:
            ctk.CTkLabel(self, text=f"Errore nel caricamento delle immagini: {e}").pack()

    def logout(self):
        # Ripristina lo stato dei giocatori al momento dell'uscita
        self.resetta_giocatori_disponibili()
        self.master.mostra_schermata_login()

    def lega1(self):
        self.master.mostra_schermata_home(self.username, lega="lega1", genera_squadre=True)

    def lega2(self):
        self.master.mostra_schermata_home(self.username, lega="lega2", genera_squadre=True)

    def lega3(self):
        self.master.mostra_schermata_home(self.username, lega="lega3", genera_squadre=True)



    
