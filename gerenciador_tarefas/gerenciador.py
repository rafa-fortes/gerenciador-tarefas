from fastapi import FastAPI

TAREFAS = []                       # Definindo uma tarefa que é uma lista. 

app = FastAPI()

@app.get("/tarefas")  # Esse @ é uma forma de vc vincula essa função com o verbo get no recurso "/terefas" 
def listar():
    return TAREFAS    # To retornando a TAREFAS. 

