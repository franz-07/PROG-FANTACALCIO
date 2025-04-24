import customtkinter as ctk
from PIL import Image


ctk.set_appearance_mode("dark")  

class SchermataLeghe(ctk.CTkFrame):
    def __init__(self, master, username):
        super().__init__(master)
        self.master = master
        self.username = username

        # Display username and logout button
        ctk.CTkLabel(self, text=f"Loggato come: {username}!", font=("Poppins", 12)).pack(anchor="ne", padx=5, pady=5)
        ctk.CTkButton(self, text="Esci", command=self.logout).pack(anchor="ne", padx=5, pady=5)

        # Title label
        ctk.CTkLabel(self, text="Scegli la tua lega", font=("Poppins", 18)).pack(pady=20)

        # Display images
        self.mostra_immagini()

    def mostra_immagini(self):
        try:
    
            img1 = ctk.CTkImage(Image.open("immagini/immagine1_lega.png"), size=(200, 200))
            img2 = ctk.CTkImage(Image.open("immagini/immagine2_lega.png"), size=(200, 200))

    
            ctk.CTkButton(self, text="", image=img1, command=self.lega1).pack(side="left", padx=10, pady=10)
            ctk.CTkButton(self, text="", image=img2, command=self.lega2).pack(side="right", padx=10, pady=10)

            ctk.CTkButton(self, text="creazione lega", command=self.crea_lega).pack(anchor="ne", padx=10, pady=10)
        except Exception as e:
            ctk.CTkLabel(self, text=f"Errore nel caricamento delle immagini: {e}").pack()

    def logout(self):
        self.master.mostra_schermata_login()

    def lega1(self):
        self.master.mostra_schermata_home(self.username, lega="lega1")

    def lega2(self):
        self.master.mostra_schermata_home(self.username, lega="lega2")

    def crea_lega(self):
        self.master.mostra_schermata_crea_lega(self.username)