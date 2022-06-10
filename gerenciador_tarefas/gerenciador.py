from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Tarefa(BaseModel):
    titulo: str

TAREFAS = []  # Definindo uma tarefa que é uma lista.

@app.get("/tarefas")
def listar():
    return TAREFAS  # To retornando a TAREFAS.

@app.post("/tarefas")
def criar(tarefa: Tarefa):
    pass 