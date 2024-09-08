import requests

BASE_URL = "http://127.0.0.1:5000/produtos"

# Testar GET todos os produtos
def test_get_produtos():
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Verifica se a resposta é uma lista

# Testar GET de um produto específico pelo ID
def test_get_produto_by_id():
    response = requests.get(BASE_URL + "/1")
    assert response.status_code == 200
    assert response.json()["nome"] == "Notebook"

# Testar POST para adicionar um novo produto
def test_add_produto():
    novo_produto = {"id": 4, "nome": "Monitor", "preco": 800}
    response = requests.post(BASE_URL, json=novo_produto)
    assert response.status_code == 201
    assert response.json()["nome"] == "Monitor"

def test_delete_produto():
    novo_produto = {"id": 2, "nome": "Teclado", "preco": 150}
    requests.post(BASE_URL, json=novo_produto)

    response = requests.delete(BASE_URL + "/2")
    assert response.status_code == 200
    assert response.json()["message"] == "Produto deletado com sucesso"

