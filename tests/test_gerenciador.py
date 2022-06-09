from fastapi import status
from fastapi.testclient import TestClient

# aqui eu importo as funções do gerenciado_tarefas.

from gerenciador_tarefas.gerenciador import (
    TAREFAS,  
)

from gerenciador_tarefas.gerenciador import app


# Definindo uma função de teste.
def test_quando_listar_tarefas_devo_ter_como_retorno_codigo_de_status_200():
    cliente = TestClient(
        app
    )  # Aqui eu estou criando um cliente de teste com base nessa aplicação. 
    resposta = cliente.get(
        "/tarefas"
    )  
    assert (
        resposta.status_code == status.HTTP_200_OK
    )  # o assert ele vai checando essa expressão que eu passei aqui. 


def test_quando_listar_tarefas_formato_de_retorno_deve_ser_jason():
    cliente = TestClient(app)
    resposta = cliente.get("/tarefas")
    assert (
        resposta.headers["Content-Type"] == "application/json"
    )  # Aqui eu estou verificado se o cabeçalho esta no formato json.


def test_quando_listar_tarefas_formato_de_retorno_deve_ser_uma_lista():
    cliente = TestClient(app)
    resposta = cliente.get("/tarefas")
    assert isinstance(
        resposta.json(), list
    )  # Essa função isinstance ela verifica se aquilo é uma lista, 
       # então eu to falando para ele pega a resposta transforma esse valor 
       # que vai estar em um formato Json esse formato é um formato textual para podermos 
       # transitar valores.


def test_quando_listar_tarefas_formato_de_retorno_deve_possuir_id():
    TAREFAS.append(  # adicionando uma tarefa na lista de TAREFAS da minha aplicação.
        {
            "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "titulo": "titulo 1",
            "descricao": "descricao 1",
            "estado": "finalizado",
        }
    )
    cliente = TestClient(
        app
    )  # criando um cliente p/ consumir a minha a aplicação.
    resposta = cliente.get("/tarefas")  # acessando o recurso de tarefas.
    assert (
        "id" in resposta.json().pop()
    )                                
    TAREFAS.clear()  
    
    # limpando a lista de tarefas é importante sempre 
    # limpar um recurso que foi modificado, nesse caso foi a tarefa, 
    # para não influenciar nos outros testes.
