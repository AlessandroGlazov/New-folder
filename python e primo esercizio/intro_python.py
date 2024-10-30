# Primo comando hello world
print("Ciao Mondo")


# Definizione di variabili non tipizzate
numero = 10
numero_reale = 3.14
nome = "Alice"
nome_2 = 'Tommaso'
is_active = True # standard consigliato con snake_case
isActive = False # standard NON utilizzato camelCase

# Definizione di variabili tipizzate
numero: int = 10
numero_reale: float = 3.14
nome: str = "Alice"
nome_2: str = 'Tommaso'
is_active: bool = True # standard consigliato con snake_case
isActive: bool = False # standard NON utilizzato camelCase

a = b = c = 0
x,y,z=1,2,3 # non leggibile
x, y, z = 1, 2, 3 # leggibile

# inserire spazi prima e dopo l'uguale
# spazio dopo la virgola

#Parole riservate
#if else def input ....

#Tipologie di variabili fondamentali
# int numeri interi
# float numeri a virgola mobile
# str stringhe
# bool booleani

# tipizzazione dinamica python (permessa ma non consigliata)
variabile = 10
variabile = "Pippo"

# Operatori matematici
somma = 5 + 3
sottrazione = 5 - 3
moltiplicazione = 5 * 3
divisione = 5 / 3

# Operatori logici

# operatore confronto ==
sono_uguali: bool = ("Mario" == "Giovanni") # = -> assegnazione, == -> confronto -> False
sono_uguali_numeri: bool = (4 == 4) # = -> assegnazione, == -> confronto -> True

# operatore diverso !=
sono_diversi: bool = ("Mario" != "Giovanni") # != diverso -> True
sono_diversi_numeri: bool = (4 != 4) # != diverso -> False

# operatore minore maggiore minore_uguale maggiore_uguale
confronto_minore: bool = 2 < 3
confronto_minore_uguale: bool = 2 <= 3
confronto_maggiore: bool = 2 > 3
confronto_maggiore_uguale: bool = 2 >= 3

# operatori and, or, not

# and -> (tutte le condizioni DEVONO essere vere)
risultato: bool = True and False # -> False
risultato_esempio_and: bool = (2 == 2) and (3 != 3) # -> False

# or -> (almeno UNA condizione deve essere vera)
risultato_esempio_or: bool = (2 == 2) or (3 != 3) # -> Vera

# truth tables di and e or

#operatore not -> negare la condizione
risultato_not: bool = not True # -> False

# esempio: db_is_active: bool 
# if not db_is_active -> activate_db() codice per attivare il db

# manipolazione di stringhe

# concatenare con l'operatore somma

saluto: str = "Auguri!"
nome: str = "Mario"
messaggio: str = saluto + nome

print(messaggio) # -> # CiaoMario

messaggio: str = saluto + " " + nome

print(messaggio) # -> # Ciao Mario

# f-strings -> inserire variabili ed espressioni direttamente all'interno di una stringa

messaggio_senza_f_sting     =  "oggi è il compleanno di " + nome + "ti faccio tanti" + saluto# -> oggi è il compleanno di Mario
messaggio_con_f_string: str = f"oggi è il compleanno di {nome}, ti faccio tanti {saluto}" # -> oggi è il compleanno di Mario

# esempio pratico con log f"il database {db.name} è nello stato {db.state}"


# slicing

testo: str = "Programmazione"
parte_iniziale: str = testo[0:7] #Program
parte_finale: str = testo[7:14] #mazione

parte_iniziale: str = testo[:7] #Program
parte_finale: str = testo[7:] #mazione

parte_intermedia: str = testo[5:10] 

testo = "ciao"
testo.upper() # -> CIAO

testo = "CIAO"
print(testo.lower()) # -> ciao

testo = "    CIAO    "
print(testo.strip().lower()) # -> "ciao"


testo = "    CIAO    "
print(testo.strip().lower().replace("ciao", "come va?")) # -> "come va?"
#"    CIAO    " -> "CIAO" -> "ciao" -> "come va?"
testo_strippato = testo.strip()
testo_in_lowercase = testo_strippato.lower()
testo_con_replace = testo_in_lowercase.replace("ciao", "come va?")


### CONTROLLO DI PROCESSO 
#struttura di controllo if else elif

punteggio_test = 82
# if / else
if punteggio_test < 60:
    print("insufficiente")# codice if con 1 indentazione 
elif punteggio_test < 80:
    print("buono")
elif punteggio_test < 90:
    print('distinto')
else:
    print('ottimo')


# lista
lista_di_elementi = [1, 2, 3, "Pippo", 5, 6, 3.14, "ciao".upper()]
# cicli for e ciclo while
for elemento in lista_di_elementi:
    # codice da applicare ad ogni elemento
    print(elemento)

somma = 0
while somma <= 100:
    somma = somma + 10
    print(somma)
    #codice

# definizione e utilizzo di funzioni

def somma(numero_1, numero_2):
    #codice della funzione
    somma = numero_1 + numero_2
    return somma

def cleaning_stringa(string_input):
    stringa_no_spazi_no_punti = string_input.replace(" ", "").replace(".", "")
    stringa_lower_case = stringa_no_spazi_no_punti.lower()
    return stringa_lower_case


testo_documento = "    TESTO DEL DOCUMENTO      ."
testo_ripulito = cleaning_stringa(testo_documento) # -> "testodeldocumento"


# importazione moduli e pacchetti

#librerie esterne installate tramite pip (o altri package installer)
# (nel terminale) pip install numpy
# import numpy as np

# lista_di_numeri = [1, 2, 3, 4, 5]
# std = np.std(lista_di_numeri)

# import nome_modulo as alias
# from numpy import std
# std = std(lista_di_numeri)

# libreria già incluse in python (built-in)
import os
current_directory = os.getcwd()


# lettura e scrittura di file
# per aprire i file esiste la funzione 'open()'

# modalità di apertura
# 'r' read (lettura)
# 'w' write (scrittura)
# 'a' append (aggiunta)
# 'rb' read bytes (lettura dei byte)
# 'wb' write bytes (scrittura dei byte)



file = open('./requirements.txt', 'r')
contenuto = file.read()
print(contenuto)
linea = file.readline()
print(linea) # prima linea
lista_di_linee = file.readlines()
print(lista_di_linee) # ['numpy', 'pandas']

#file.write("Questo è un esempio di scrittura.\n")
file.close()


# consigliato
with open('./requirements.txt', 'r') as file:
    contenuto = file.read()
    print(contenuto)

    linea = file.readline()
    print(linea) # prima linea

    lista_di_linee = file.readlines()
    print(lista_di_linee) # ['numpy', 'pandas']

# python gestisce da solo apertura e chiusura con il blocco with

lista = []

persona = {
    "nome": "Mario",
    "cognome": "Napoli",
    "qualifica": ["AI Specialist", "Data Scientist", 'Data Engineer'],
    "anni": 30 
}

persona["nome"] # -> "Mario"
persona.get("nome") # -> "Mario"