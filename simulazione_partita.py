import tkinter as tk
from PIL import Image, ImageTk
import customtkinter as ctk
import random

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

        # Label per mostrare i risultati con wrapping del testo
        self.risultati_label = ctk.CTkLabel(self, text="", font=("Poppins", 14), wraplength=500, anchor="center", justify="center")
        self.risultati_label.pack(pady=20, fill="x", expand=True)
    
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

            # Bottone per iniziare la partita
            self.center_button = ctk.CTkButton(self, text="Inizia partita", command=self.avvia_simulazione)
            self.center_button.pack(pady=10)

        except Exception as e:
            ctk.CTkLabel(self, text=f"Errore nel caricamento delle immagini: {e}").pack()

    def avvia_simulazione(self):
        # Aspetta 3 secondi per cambiare l'immagine e mostrare i risultati
        self.master.after(3000, lambda: self.center_label.configure(image=self.img_center_2))
        self.master.after(3000, self.genera_risultati)

    def genera_risultati(self):
        risultati = self.simula_partita()
        testo_risultati = (
            f"🏆 {risultati['Squadra A']['Punteggio']} - {risultati['Squadra B']['Punteggio']} 🏆\n"
            f"Squadra A:\nGol: {risultati['Squadra A']['Gol']} | Assist: {risultati['Squadra A']['Assist']} | "
            f"Autogol: {risultati['Squadra A']['Autogol']} | Cartellini gialli: {risultati['Squadra A']['Cartellini gialli']} | "
            f"Cartellini rossi: {risultati['Squadra A']['Cartellini rossi']} | Punteggio: {risultati['Squadra A']['Punteggio']}\n\n"
            f"Squadra B:\nGol: {risultati['Squadra B']['Gol']} | Assist: {risultati['Squadra B']['Assist']} | "
            f"Autogol: {risultati['Squadra B']['Autogol']} | Cartellini gialli: {risultati['Squadra B']['Cartellini gialli']} | "
            f"Cartellini rossi: {risultati['Squadra B']['Cartellini rossi']} | Punteggio: {risultati['Squadra B']['Punteggio']}\n"
        )
        self.risultati_label.configure(text=testo_risultati)

        # Salva i risultati in un file
        self.salva_risultati_su_file(risultati)

    def salva_risultati_su_file(self, risultati):
        try:
            # Nome del file basato sull'utente e sulla lega
            filename = f"risultati_{self.username}_{self.lega}.txt"
            with open(filename, "a", encoding="utf-8") as file:
                file.write("=== Risultati Partita ===\n")
                file.write(f"Squadra A:\n")
                for key, value in risultati["Squadra A"].items():
                    file.write(f"{key}: {value}\n")
                file.write("\nSquadra B:\n")
                for key, value in risultati["Squadra B"].items():
                    file.write(f"{key}: {value}\n")
                file.write("\n\n")
        except Exception as e:
            print(f"Errore durante il salvataggio dei risultati: {e}")

    def simula_partita(self):
        teams = ["Squadra A", "Squadra B"]
        match_stats = {}
        
        for team in teams:
            goals = random.choices([0, 1, 2, 3, 4], weights=[20, 35, 25, 15, 5])[0]
            assists = random.randint(goals // 2, goals)
            own_goals = random.choices([0, 1], weights=[95, 5])[0]
            clean_sheet = 1 if goals == 0 else 0
            yellow_cards = random.choices([0, 1, 2], weights=[60, 30, 10])[0]
            red_cards = random.choices([0, 1], weights=[98, 2])[0]

            points = (goals * 3) + (assists * 1) + (own_goals * -2) + (clean_sheet * 1) + (yellow_cards * -0.5) + (red_cards * -1.5)

            match_stats[team] = {
                "Gol": goals,
                "Assist": assists,
                "Autogol": own_goals,
                "Porta inviolata": clean_sheet,
                "Cartellini gialli": yellow_cards,
                "Cartellini rossi": red_cards,
                "Punteggio": round(points, 1)
            }
        
        return match_stats

    def torna_home(self):
        self.master.mostra_schermata_home(self.username, self.giocatori, self.lega, False)
