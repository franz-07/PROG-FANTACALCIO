import json
import os

def carica_dati_squadre():
    if os.path.exists("squadre.json"):
        try:
            with open("squadre.json", "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Il file 'squadre.json' è corrotto o vuoto. Reinizializzo i dati.")
            return {}  # Ritorna un dizionario vuoto se il file è corrotto
    return {}  # Ritorna un dizionario vuoto se il file non esiste


def salva_dati_squadre(dati):
    with open("squadre.json", "w") as file:
        json.dump(dati, file, indent=4)
