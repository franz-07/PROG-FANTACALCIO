import tkinter as tk
from schermata_inizio import SchermataInizio
from registra import SchermataRegistra
from login import SchermataLogin
from home import SchermataHome
from giocatori import giocatori
from schermata_leghe import SchermataLeghe
from crea_lega import CreaLega
from mercato import SchermataMercato
from formazione import SchermataFormazione


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("FANTA-ALCHIMISTI")
        self.geometry("1080x720")
        self.schermate = {}
        self.mostra_schermata_inizio()

    def mostra_schermata_inizio(self):
        self.cambia_frame("inizio", SchermataInizio)

    def mostra_schermata_crea_lega(self, username):
        # Rimuove qualsiasi binding globale di tasti rimasto dalla schermata iniziale
        self.unbind_all("<Key>")
        if "crea_lega" in self.schermate:
            self.schermate["crea_lega"].destroy()
            del self.schermate["crea_lega"]
        frame = CreaLega(self, username)
        self.schermate["crea_lega"] = frame
        
        for i in self.schermate.values():
            if i != frame:
                i.pack_forget()
        frame.pack(fill="both", expand=True)

    def mostra_schermata_login(self):
        # Rimuove qualsiasi binding globale di tasti rimasto dalla schermata iniziale
        self.unbind_all("<Key>")
        if "login" in self.schermate:
            self.schermate["login"].destroy()
            del self.schermate["login"]
        frame = SchermataLogin(self)
        self.schermate["login"] = frame
        
        for i in self.schermate.values():
            if i != frame:
                i.pack_forget()
        frame.pack(fill="both", expand=True)

    def mostra_schermata_registra(self):
        # Rimuove qualsiasi binding globale di tasti
        self.unbind_all("<Key>")
        if "registra" in self.schermate:
            self.schermate["registra"].destroy()
            del self.schermate["registra"]
        frame = SchermataRegistra(self)
        self.schermate["registra"] = frame
        
        for i in self.schermate.values():
            if i != frame:
                i.pack_forget()
        frame.pack(fill="both", expand=True)

    def mostra_schermata_leghe(self, username):
        self.unbind_all("<Key>")
        self.username = username  # Imposta 'username' qui
        # Assicurati che 'giocatori' e 'lega' siano inizializzati altrove
        if "leghe" in self.schermate:
            self.schermate["leghe"].destroy()
            del self.schermate["leghe"]

        frame = SchermataLeghe(self, username)
        self.schermate["leghe"] = frame

        for i in self.schermate.values():
            if i != frame:
                i.pack_forget()

        frame.pack(fill="both", expand=True)


    def mostra_schermata_home(self, username, lega, genera_squadre, formazione=None):
        self.unbind_all("<Key>")

        # Inizializza gli attributi globali
        self.username = username
        self.giocatori = giocatori
        self.lega = lega
            
        if "home" in self.schermate:
            self.schermate["home"].destroy()
            del self.schermate["home"]

        # Passa la formazione alla schermata Home
        frame = SchermataHome(self, username, giocatori, lega, genera_squadre, formazione=formazione)
        self.schermate["home"] = frame

        for i in self.schermate.values():
            if i != frame:
                i.pack_forget()

        frame.pack(fill="both", expand=True)



    def mostra_schermata_formazione(self, username, lega):
        self.unbind_all("<Key>")  # Rimuove eventuali binding di tasti

        # Controlla che gli attributi siano stati inizializzati
        if not hasattr(self, "username") or not hasattr(self, "lega"):
            raise AttributeError("Gli attributi 'username' e 'lega' non sono stati inizializzati.")

        # Rimuove la schermata formazione esistente (se c'è)
        if "formazione" in self.schermate:
            self.schermate["formazione"].destroy()
            del self.schermate["formazione"]

        # Crea una nuova istanza della schermata formazione
        frame = SchermataFormazione(self, self.giocatori, username, lega)
        self.schermate["formazione"] = frame

        # Nasconde tutte le altre schermate e mostra la schermata formazione
        for i in self.schermate.values():
            if i != frame:
                i.pack_forget()

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

    def mostra_schermata_mercato(self):
        self.unbind_all("<Key>")  # Rimuove eventuali binding di tasti

        # Assicurati che gli attributi siano stati inizializzati (username, giocatori, lega)
        if not hasattr(self, "username") or not hasattr(self, "giocatori") or not hasattr(self, "lega"):
            raise AttributeError("Gli attributi 'username', 'giocatori' e 'lega' non sono stati inizializzati.")

        # Rimuove la schermata esistente (se c'è)
        if "mercato" in self.schermate:
            self.schermate["mercato"].destroy()
            del self.schermate["mercato"]

        # Crea una nuova istanza della schermata Mercato con gli attributi definiti
        frame = SchermataMercato(self, self.username, self.giocatori, self.lega)
        self.schermate["mercato"] = frame

        # Nasconde tutte le altre schermate
        for i in self.schermate.values():
            if i != frame:
                i.pack_forget()

        # Mostra la schermata del mercato
        frame.pack(fill="both", expand=True)


        

if __name__ == "__main__":
    app = App()
    app.mainloop()
