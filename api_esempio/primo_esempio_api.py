from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Hello world, my name is Mario!"}













#@app.get("/user")
#async def return_user_info():
#    return {"user_info": {"name": "Mario", "age": 30}}
    # codice per prendere le info dell'utente e ritornale al chiamante

#@app.post("/user")
#async def create_new_user():
#    db.create_user()
#    return {"user_id": "Mario"}
    # codice per creare un nuovo utente

# api_url = "www.apidiamario.it"

# richiesta get all'endpoint www.apidiamario.it/ -> {"message": "Hello world!"}


# richiesta GET a www.apidiamario.it/user -> info dell'utente

# richiesta POST a www.apidiamario.it/user -> creo un nuovo utente