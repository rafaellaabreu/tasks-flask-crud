import pytest
import requests

# variável URL do servidor que vamos testar 
BASE_URL = 'http://127.0.0.1:5000'
# lista para armazenar as tarefas criadas.
tasks = []

### Testes Automatizados com Pytest - POST
# Vamos começar testando o endpoint de criação de tarefas (createTask)
def test_create_task():
    new_task_data = {
        "title": "Nova tarefa",
        "description": "Descrição da nova tarefa"
    }
    # requisição POST enviar os dados da nova tarefa
    response = requests.post(f"{BASE_URL}/tasks", json=new_task_data)

    # Usando o PyTest, verificaremos se a resposta da requisição é um código 200, indicando que a tarefa foi criada com sucesso.
    assert response.status_code == 200

    response_json = response.json()
    assert "message" in response_json
    assert "id" in response_json
    tasks.append(response_json['id'])

### Testes Automatizados com Pytest - Read

#  testes de leitura (read) em um endpoint. Vamos validar dois endpoints: um para recuperar todas as atividades cadastradas e outro para recuperar uma atividade específica. 

# Para testar o endpoint de todas as atividades, faremos uma requisição GET na URL "/tasks"
def test_get_tasks():
    response = requests.get(f"{BASE_URL}/tasks")
    # validaremos o status code 200
    assert response.status_code == 200
    # presença das chaves "tasks" e "total tasks" na resposta
    response_json = response.json()
    assert "tasks" in response_json
    assert "total_tasks" in response_json

# Para testar o endpoint de uma atividade específica, utilizaremos o ID da atividade criada anteriormente
def test_get_task():
    if tasks:
        task_id = tasks[0]
        # requisição GET na URL "/tasks/{id}"
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        # Validaremos novamente o status code 200 e se o ID retornado é igual ao ID enviado na requisição
        assert response.status_code == 200
        response_json = response.json()
        assert task_id == response_json['id']

### Testes automatizados com Pytest - Update e Delete

# Criamos a função testUpdateTask para enviar uma requisição de atualização para o endpoint correspondente
def test_update_task():
    if tasks:
        task_id = tasks[0]
        payload = {
            "completed": False,
            "description": "Nova descrição",
            "title": "Título atualizado"
        }
        response = requests.put(f"{BASE_URL}/tasks/{task_id}", json=payload)
        # Validamos o status code da resposta
        response.status_code == 200
        # conteúdo do JSON retornado
        response_json = response.json()
        assert "message" in response_json

        # Nova  requisição a tarefa especifica
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        # Validamos o status code da resposta
        assert response.status_code == 200
        # conteúdo do JSON retornado
        response_json = response.json()
        assert response_json['title'] == payload['title']
        assert response_json['description'] == payload['description']
        assert response_json['completed'] == payload['completed']

# criamos a função testDeleteTask para enviar uma requisição de exclusão
def test_delete_task():
    if tasks:
        task_id = tasks[0]
        response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
        # validamos o status code
        response.status_code == 200
       
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        # validamos o status code
        assert response.status_code == 404