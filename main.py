import tkinter as tk
from schermata_inizio import SchermataInizio
from registra import SchermataRegistra
from login import SchermataLogin
from home import SchermataHome
from giocatori import giocatori
from schermata_leghe import SchermataLeghe
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("FANTA-ALCHIMISTI")
        self.geometry("1080x720")
        self.schermate = {}
        self.mostra_schermata_inizio()

    def mostra_schermata_inizio(self):
        self.cambia_frame("inizio", SchermataInizio)

    def mostra_schermata_login(self):
        # Rimuove qualsiasi binding globale di tasti rimasto dalla schermata iniziale
        self.unbind_all("<Key>")
        self.cambia_frame("login", SchermataLogin)

    def mostra_schermata_registra(self):
        # Rimuove qualsiasi binding globale di tasti
        self.unbind_all("<Key>")
        self.cambia_frame("registra", SchermataRegistra)

    def mostra_schermata_leghe(self, username):
        self.unbind_all("<Key>")
        if "leghe" in self.schermate:
            self.schermate["leghe"].destroy()
            del self.schermate["leghe"]
        frame = SchermataLeghe(self, username)
        self.schermate["leghe"] = frame    
        
        for i in self.schermate.values():
            if i != frame:
                i.pack_forget()
        
        frame.pack(fill="both", expand=True)

    def mostra_schermata_home(self, username, lega):
        # Rimuove qualsiasi binding globale di tasti
        self.unbind_all("<Key>")
        # Se esiste già la home, distruggila
        if "home" in self.schermate:
            self.schermate["home"].destroy()
            del self.schermate["home"]

        frame = SchermataHome(self, username, giocatori, lega)
        self.schermate["home"] = frame

        # Nascondi tutti gli altri frame
        for i in self.schermate.values():
            if i != frame:
                i.pack_forget()

        # Mostra la nuova home
        frame.pack(fill="both", expand=True)

    def cambia_frame(self, nome, frame_class):
        # Rimuove event listener globali di tasti per prevenire ritorni imprevisti
        self.unbind_all("<Key>")
        if nome in self.schermate:
            frame = self.schermate[nome]
        else:
            frame = frame_class(self)
            self.schermate[nome] = frame

        # Nascondi tutti i frame
        for i in self.schermate.values():
            i.pack_forget()

        # Mostra il frame richiesto
        frame.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = App()
    app.mainloop()
