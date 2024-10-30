from openai import OpenAI

# get api key
with open("openai_key.txt", "r") as file:
    openai_api_key = file.read()

client = OpenAI(api_key=openai_api_key)


def get_db_summary(db_info: dict):
    prompt = f"""
    Ecco il mio database in input con le informazioni degli utenti:
    {str(db_info)}
    Restituiscimi un summary dei contenuti e delle info degli utenti.
    """
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Sei una API che riceverà il dump in JSON di un database e delle informazioni dei realtivi utenti. Il tuo compito è quello di fornire un resoconto degli utenti presenti sul db."},
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message



def ask_ai(query: str, db_info: dict):
    prompt = f"""
    Ecco il mio database in input con le informazioni degli utenti:
    {str(db_info)}
    
    Ecco la query dell'utente:
    {query}

    Rispondi alla query in maniera completa ed esaustiva.
    """
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Sei una API che riceverà il dump in JSON di un database e delle informazioni dei realtivi utenti. Il tuo compito è quello di fornire una risposta, basandoti sulle informazioni contenute nel db e sulla query dell'utente."},
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message
