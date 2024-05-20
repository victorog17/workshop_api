from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/outro_recurso")
def pegar_recurso():
    return "message"

@app.post("/outro_recurso/{id}")
def criar_recurso():
    return {"message": id}