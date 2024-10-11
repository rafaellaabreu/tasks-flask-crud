"""
Desenvolvimento de APIs com Flask. 
Flask: framework para desenvolvimento web em Python.
Para utilizar o Flask, é necessário instalar suas dependências: pip3 install flask ou criando um arquivo de requisitos e instalando as dependências através do comando pip install -r requirements.txt
Vamos abordar o conceito de APIs, API REST, requisições, protocolo HTTP, métodos e como usar o Python e o Flask para construir uma API funcional.
Rota: caminho que guia uma requisição, permitindo que o servidor atenda às necessidades do cliente de forma organizada e eficiente. é o caminho que os pacotes de dados percorrem para chegar ao destino, seja na internet ou em uma aplicação web.
"""

# importando a biblioteca Flask 
from flask import Flask
 
# criar uma instância da classe Flask
app = Flask(__name__) # __name__ = "__main__"

# definir uma rota chamada "/hello-world" que retorna uma string em formato HTML
@app.route("/") # rota
def hello_word(): # função
    return "Hello Word!" # string

# Acessamos a rota no navegador e vimos o texto "/hello-world" sendo exibido - usar run python file

# criamos uma segunda rota chamada "sobre" que retorna a string "página sobre"
@app.route("/about") # rota
def about(): # função
    return "Página sobre" # string

# método run para executar o servidor localmente, com a opção debug ativada para visualizar informações de depuração
if __name__ == "__main__": # garante que só executando de forma manual subirá o servidor abaixo
    app.run(debug=True)

# códigos de resposta HTTP, como o 200 que indica uma resposta bem-sucedida
    # 127.0.0.1 - - [10/Oct/2024 17:27:40] "GET /about HTTP/1.1" 200