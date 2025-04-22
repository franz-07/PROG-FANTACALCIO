import customtkinter as ctk
from PIL import Image


ctk.set_appearance_mode("dark")  

class SchermataLeghe(ctk.CTkFrame):
    def __init__(self, master, username):
        super().__init__(master)
        self.master = master

        # Display username and logout button
        ctk.CTkLabel(self, text=f"Loggato come: {username}!", font=("Poppins", 12)).pack(anchor="ne", padx=5, pady=5)
        ctk.CTkButton(self, text="Esci", command=self.logout).pack(anchor="ne", padx=5, pady=5)

        # Title label
        ctk.CTkLabel(self, text="Scegli la tua lega", font=("Poppins", 18)).pack(pady=20)

        # Display images
        self.mostra_immagini()

    def mostra_immagini(self):
        try:
            # Load and display images using PIL for compatibility with CTkLabel
            img1 = ctk.CTkImage(Image.open("immagini/immagine1_lega.png"), size=(200, 200))
            img2 = ctk.CTkImage(Image.open("immagini/immagine2_lega.png"), size=(200, 200))
            
            img_label1 = ctk.CTkLabel(self, image=img1, text="")
            img_label1.pack(side="left", padx=10)

            img_label2 = ctk.CTkLabel(self, image=img2, text="")
            img_label2.pack(side="right", padx=10)
        except Exception as e:
            ctk.CTkLabel(self, text=f"Errore nel caricamento delle immagini: {e}").pack()

    def logout(self):
        self.master.mostra_schermata_login()