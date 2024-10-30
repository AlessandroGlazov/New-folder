import json
from typing import Union


class DatabaseHandler:
    
    def __init__(self, filename: str = "database.json"):
        """
        **Params**
        - filename: str = il nome del file JSON da cui caricare il database.
        """
        self.filename = filename
        self.db = self.read_database()

    def read_database(self) -> dict:
        """
        Funzione per leggere un database

        **Params**
        - filename: str = il nome del file JSON da salvare, default sarà 'database.json'
        """
        with open(self.filename, "r", encoding="utf-8") as file:
            database: dict = json.load(file)
        return database

    def get_database(self):
        return self.db

    def save_database(self) -> None:
        """
        Funzione per salvare un dict python a JSON
        """
        # salvare il database con il nuovo utente inserito
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(self.db, file)
        return f"Database salvato sul file: {self.filename}"

    def add_user_to_database(
            self, 
            nome: str,
            cognome: str,
            sport_preferito: str,
            sogno_nel_cassetto: str,
            ) -> dict:
        """
        Funzione per aggiungere un utente al nostro database

        **Params**
        - nome_utente: str = il nome dell'utente da aggiungere
        """
        id_utente = len(self.db) + 1
        self.db[id_utente] = {
            "nome": nome,
            "cognome": cognome,
            "sport_preferito": sport_preferito,
            "sogno_nel_cassetto": sogno_nel_cassetto
        }
        self.save_database()
        return f"Utente {nome} aggiunto al database con id: {id_utente}"

    def delete_user_from_database(
            self,
            id_utente: int
    ) -> Union[dict, str]:
        """
        Funzione per rimuovere un utente dal database json

        **Params**
        - nome_utente: str = il nome dell'utente da rimuovere
        """
        messaggio: str = f"L'utente {id_utente} non esiste!"
        if id_utente in self.db.keys():
            del self.db[id_utente]
            messaggio = f"L'utente {id_utente} è stato rimosso!"
            self.save_database()
        return messaggio

    def change_sogno_nel_cassetto(
            self, 
            id_utente: int,
            nuovo_sogno: str
        ):
        """
        Funzione per cambiare sogno nel cassetto ad un utente
        **Params**
        - **id_utente**: int = l'id_utente della persona a cui cambiare il sogno nel cassetto
        - **nuovo_sogno**: str = Il nuovo sogno nel cassetto dell'utente
        """
        info_utente = self.db.get(str(id_utente))
        if info_utente is not None:
            info_utente['sogno_nel_cassetto'] = nuovo_sogno
            self.save_database()
            return f"Sogno dell'utente con id {id_utente} cambiato in: {nuovo_sogno}"
        return f"L'utente con id: {id_utente} non esiste!"
    