from fastapi import status
from fastapi.testclient import TestClient

from gerenciador_tarefas.gerenciador import TAREFAS, app

# aqui eu importo as funções do gerenciado_tarefas.


# Definindo uma função de teste.
def test_quando_listar_tarefas_devo_ter_como_retorno_codigo_de_status_200():
    cliente = TestClient(app)
    resposta = cliente.get("/tarefas")
    assert resposta.status_code == status.HTTP_200_OK


def test_quando_listar_tarefas_formato_de_retorno_deve_ser_jason():
    cliente = TestClient(app)
    resposta = cliente.get("/tarefas")
    assert (
        resposta.headers["Content-Type"] == "application/json"
    )  # Aqui eu estou verificado se o cabeçalho esta no formato json.


def test_quando_listar_tarefas_formato_de_retorno_deve_ser_uma_lista():
    cliente = TestClient(app)
    resposta = cliente.get("/tarefas")
    assert isinstance(resposta.json(), list)


# adicionando uma tarefa na lista de TAREFAS da minha aplicação.
def test_quando_listar_tarefas_formato_de_retorno_deve_possuir_id():
    TAREFAS.append(
        {
            "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "titulo": "titulo 1",
            "descricao": "descricao 1",
            "estado": "finalizado",
        }
    )
    cliente = TestClient(app)
    resposta = cliente.get("/tarefas")
    assert "id" in resposta.json().pop()
    TAREFAS.clear()


def test_quando_listar_tarefas_a_tarefa_retornada_deve_possuir_titulo():
    TAREFAS.append(
        {
            "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "titulo": "titulo 1",
            "descricao": "descricao 1",
            "estado": "finalizado",
        }
    )
    cliente = TestClient(app)
    resposta = cliente.get("/tarefas")
    assert "titulo" in resposta.json().pop()
    TAREFAS.clear()


def test_quando_listar_tarefas_a_tarefa_retornada_deve_possuir_descricao():
    TAREFAS.append(
        {
            "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "titulo": "titulo 1",
            "descricao": "descricao 1",
            "estado": "finalizado",
        }
    )
    cliente = TestClient(app)
    resposta = cliente.get("/tarefas")
    assert "descricao" in resposta.json().pop()
    TAREFAS.clear()


def test_quando_listar_tarefas_a_tarefa_retornada_deve_possuir_um_estado():
    TAREFAS.append(
        {
            "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "titulo": "titulo 1",
            "descricao": "descricao 1",
            "estado": "finalizado",
        }
    )
    cliente = TestClient(app)
    resposta = cliente.get("/tarefas")
    assert "estado" in resposta.json().pop()
    TAREFAS.clear()


def test_recurso_tarefas_deve_aceitar_o_verbo_post():
    cliente = TestClient(app)
    resposta = cliente.post("/tarefas")
    assert resposta.status_code != status.HTTP_405_METHOD_NOT_ALLOWED


def test_quando_uma_tarefa_e_submetida_deve_possuir_um_titulo():
    cliente = TestClient(app)
    resposta = cliente.post("/tarefas", json={})
    assert resposta.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
