# metodi HTTP più comuni

# GET
# POST
# PUT
# DELETE
"""
Metodo GET -> ottenere risorse SENZA modificare lo stato del server
    e delle risorse stesse.
    Può essere cacheable, per ottimizzare le risorse.
    Se rieseguo una get uguale ad una che ho già eseguito, 
    posso riutilizzare l'output salvato dalla prima
    senza rieseguire tutto il flusso di codice (finché le risorse
    alla base non cambiano)

Metodo POST -> metodo per creare nuove risorse, in questo caso
    sto modificando lo stato interno.
    Se rieseguo la stessa POST ottengo risultati diversi.
    POST non può essere cacheable.
    Ma ogni post modifica lo stato delle risorse.


Metodo PUT -> metodo per aggiornare risorse già esistenti, oppure 
    crearne di nuove, se già non esistono.


Metodo DELETE -> eliminare risorse dal server.
    DELETE non può essere cacheable.
"""
