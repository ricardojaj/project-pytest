from flask import Flask, jsonify, request

app = Flask(__name__)

# Dados para teste
produtos = [
    {"id": 1, "nome": "Notebook", "preco": 3000},
    {"id": 2, "nome": "Teclado", "preco": 150},
    {"id": 3, "nome": "Mouse", "preco": 50}
]

# Rota para obter todos os produtos
@app.route('/produtos', methods=['GET'])
def get_produtos():
    return jsonify(produtos)

# Rota para adicionar um novo produto
@app.route('/produtos', methods=['POST'])
def add_produto():
    novo_produto = request.get_json()
    produtos.append(novo_produto)
    return jsonify(novo_produto), 201

# Rota para obter um produto pelo ID
@app.route('/produtos/<int:id>', methods=['GET'])
def get_produto(id):
    produto = next((item for item in produtos if item["id"] == id), None)
    if produto:
        return jsonify(produto)
    else:
        return jsonify({"error": "Produto não encontrado"}), 404

@app.route('/produtos/<int:id>', methods=['DELETE'])
def delete_produto(id):
    global produtos
    produto = next((item for item in produtos if item["id"] == id), None)
    if produto:
        produto = [item for item in produtos if item["id"] != id]
        return jsonify({"message": "Produto deletado com sucesso"}), 200
    else:
        return jsonify({"error": "Produto nao encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)
