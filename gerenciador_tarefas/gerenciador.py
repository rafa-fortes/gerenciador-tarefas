from fastapi import FastAPI

TAREFAS = []  # Definindo uma tarefa que é uma lista.

app = FastAPI()


@app.get(  # Esse @ é uma forma de vc vincula essa função com o verbo get no recurso "/terefas"
    "/tarefas"
)
def listar():
    return TAREFAS  # To retornando a TAREFAS.
