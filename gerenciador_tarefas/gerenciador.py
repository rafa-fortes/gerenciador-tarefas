from fastapi import FastAPI

TAREFAS = []  # Definindo uma tarefa que é uma lista.

app = FastAPI()


@app.get(  
    "/tarefas"
)
def listar():
    return TAREFAS  # To retornando a TAREFAS.
