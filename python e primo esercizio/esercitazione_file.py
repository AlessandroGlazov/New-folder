# Creiamo un semplice script Python che legge un file di testo e ne stampa il contenuto sulla console. 

# apertura semplice
#with open("./requirements.txt", "r") as file:
#    contenuto = file.read()
#
#print(f"Il contenuto del file è:\n{contenuto}\n\nIl tipo della variabile è: {type(contenuto)}")

# apertura con readlines
# with open("./requirements.txt", "r") as file:
#     contenuto_file = file.readlines()

# print(f"Il contenuto del file è:\n{contenuto_file}\n\nIl tipo della variabile è: {type(contenuto_file)}")

# contenuto_pulito = []
# for nome_libreria in contenuto_file:
#     nome_libreria_pulito = nome_libreria.strip("\n")
#     contenuto_pulito.append(nome_libreria_pulito)

# print(f"Il contenuto del file è:\n{contenuto_pulito}\n\nIl tipo della variabile è: {type(contenuto_pulito)}")


with open("./commedia.txt", "r", encoding="utf-8") as file:
    testo_commedia = file.read()

testo_commedia = testo_commedia.replace("\n", " ")
testo_commedia = testo_commedia.split()

def cleaning_parole(parola):
    return parola.replace(" ", "").replace(".", "").replace(",", "").replace(":", "").replace("'", " ").strip()

# list comprehension
lista_di_parole_pulite = [cleaning_parole(x) for x in testo_commedia]

#print(lista_di_parole_pulite)
print(f"Nel testo dell'inferno della divina commedia ci sono: {len(testo_commedia)} parole!")

# Introdurre dizionari 
    # contiamo le parole tramite dict
count_delle_parole: dict = {}

for parola in lista_di_parole_pulite:
    if parola in count_delle_parole.keys():
        count_delle_parole[parola] += 1
    else:
        count_delle_parole[parola] = 1

# codice di ordinamento dizionario in base alla count dei valori
count_delle_parole = dict(sorted(count_delle_parole.items(), key=lambda item: item[1]))

# aggiungiamo stopwords
with open("./stop-words-italian.txt", 'r', encoding="utf-8") as file:
    stopwords = [x.strip("\n") for x in file.readlines()]

for stopword in stopwords:
    if stopword in count_delle_parole.keys():
        del count_delle_parole[stopword]


#print(count_delle_parole)

import json

# Scrittura da dict python a json
with open("risultati_count.json", 'w', encoding="utf-8") as file:
    json.dump(count_delle_parole, file, indent=4, ensure_ascii=False)



# lettura da json a dict python
with open("risultati_count.json", "r", encoding="utf-8") as file:
    json_caricato = json.load(file)



print(type(json_caricato))
# codifica json
    #creiamo un record personale di chat utente con info

# lettura file in json, modifica, salvataggio




# JSON -> dict Python
# dict X-> JSON (non è possibile SEMPRE convertire un dict in JSON)


class DB_Handler():
    def __init__(self):
        self.db = "Il mio database"
        pass

    def connect_database():
        print("Connected")

db = DB_Handler()

risorse_per_architettura_ai={
    "database_per_chat_ai": db
}

# Questo oggetto di tipo db personalizzato NON è Json-Serilizable 
# Cosa lo è?
# JSON le chiavi devono essere stringhe, su dict python no
# il valore deve essere json-serializable
# dict, liste, stringhe, numeri

lista_di_nomi: list = ['mario', 'alfonso', 'giovanni']

data = {
    "nomi": lista_di_nomi,
    "istituto": "Liceo scientifico Lioy, Vicenza",
    "anno_di_corso": 4,
    "hanno_conseguito_diploma": False,
    "lista_di_diplomi": None
}

# questo dict è json-compatibile
