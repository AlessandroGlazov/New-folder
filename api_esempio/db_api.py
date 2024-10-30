from fastapi import FastAPI
from db_handler import DatabaseHandler
from ai_utils import get_db_summary, ask_ai


# init delle variabili e degli oggetti
app = FastAPI()
db = DatabaseHandler(filename="database.json")


@app.get("/")
async def homepage() -> dict:
    """
    Funzione di base per restituire un messaggio di partenza quando si raggiunge l'homepage dell'API
    """
    return {
        "message": "Benvenuto, questa API gestisce un database tramite un file JSON, buon divertimento."
        }

@app.get("/database")
async def get_database_info() -> dict:
    """
    Funzione per ottenere in output il database sotto forma di JSON
    """
    return db.get_database()

@app.post("/database")
async def create_new_user(
    nome: str,
    cognome: str,
    sport_preferito: str,
    sogno_nel_cassetto: str,
    ):
    """
     Funzione per creare un nuovo user dentro il nostro database

    **Params**:
    - **nome**: str = Il nome dell'utente che voglio creare
    """
    # inizializziamo un nuovo record con il nome dell'utente
    db.add_user_to_database(
        nome=nome,
        cognome=cognome,
        sport_preferito=sport_preferito,
        sogno_nel_cassetto=sogno_nel_cassetto
    )
    return {"message": "utente creato!"}

@app.delete("/database")
async def delete_user(id_utente: int):
    """
    Funzione per eliminare un utente dal database
    **Params**
    - **id_utente**: int = l'id_utente dell'utente da eliminare
    """
    messaggio = db.delete_user_from_database(id_utente)
    return {"message": messaggio}

@app.put("/database")
async def change_sogno(
    id_utente: int,
    nuovo_sogno: str
    ):
    """
    Funzione per cambiare sogno nel cassetto ad un utente
    **Params**
    - **id_utente**: int = l'id_utente della persona a cui cambiare il sogno nel cassetto
    - **nuovo_sogno**: str = Il nuovo sogno nel cassetto dell'utente
    """
    messaggio = db.change_sogno_nel_cassetto(
        id_utente=id_utente, 
        nuovo_sogno=nuovo_sogno
    )
    return messaggio


@app.get("/ai_summary")
def get_ai_summary_of_db():
    database = db.get_database()
    ai_response = get_db_summary(database)
    return {"message": ai_response.content}


@app.get("/ask_ai")
def get_ai_response(query: str):
    database = db.get_database()
    ai_response = ask_ai(
        query=query,
        db_info=database
        )
    return {"message": ai_response.content}
