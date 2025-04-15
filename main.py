import tkinter as tk
from schermata_inizio import SchermataInizio
from login import SchermataLogin
from home import SchermataHome
from giocatori import giocatori

class App(tk.Tk): #tk.Tk rende la finestra App direttamente il root
    def __init__(self):
        super().__init__()
        self.title("FANTA-ALCHIMISTI")
        self.geometry("1080x720")
    
    
        self.schermate = {}
        self.mostra_schermata_inizio()

    def mostra_schermata_inizio(self):
        self.cambia_frame("inizio", SchermataInizio)

    def mostra_schermata_login(self):
        self.cambia_frame("login", SchermataLogin)

    def mostra_schermata_home(self, username):
        # Se esiste già una schermata home, distruggila
        if "home" in self.schermate:
            self.schermate["home"].destroy()
            del self.schermate["home"]
        
        # Crea una nuova schermata home per l'utente
        frame = SchermataHome(self, username, giocatori)
        self.schermate["home"] = frame

        # Nascondi tutti gli altri frame
        for i in self.schermate.values():
            if i != frame:
                i.pack_forget()

        # Mostra la nuova schermata home
        frame.pack(fill="both", expand=True)


    def cambia_frame(self, nome, frame_class):
        if nome in self.schermate:
            frame = self.schermate[nome]
        else:
            frame = frame_class(self)
            self.schermate[nome] = frame

        # Rimuovi tutti i frame visibili
        for i in self.schermate.values():
            i.pack_forget()

        # Mostra il frame attuale
        frame.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = App()
    app.mainloop()
