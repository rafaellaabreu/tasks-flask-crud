# importando a biblioteca Flask 
from flask import Flask, request, jsonify
from models.task import Task
 
# criar uma instância da classe Flask
app = Flask(__name__) # __name__ = "__main__"

# Endpoints
# lista para armazenar as atividades
tasks = []
# variável taskIdControl para gerar um identificador único para cada tarefa
task_id_control = 1

##### funcionalidade de criação (CREATE) das atividades

# rota de criação de tarefas, utilizando o método POST e recebendo os dados do cliente
@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_control
    # recupera o que o cliente enviou
    data = request.get_json() 
    # título da tarefa, que é recuperado do cliente usando o método get. criar uma tarefa sem um título ou descrição, definindo um valor padrão    
    new_task = Task(id=task_id_control, title=data['title'], description=data.get("description", ""))
    task_id_control += 1
    # método append para adicionar a nova tarefa à lista de tarefas existente
    tasks.append(new_task)
    # print para verificar se os dados estavam sendo recebidos corretamente
    print(tasks)
    # retornar a mensagem de sucesso em formato JSON usando o método jsonify
    return jsonify({"message": "Nova tarefa criada com sucesso!"})

##### funcionalidade de leitura (READ)

# listagem de todas as tarefas com método GET no endpoint "/tasks"
@app.route('/tasks', methods=['GET'])
def get_tasks():
    #task_list = []
    # transformar as instâncias de atividades em um formato de dicionário utilizando o método "to_dict"
    #for task in tasks:
    #    task_list.append(task.to_dict())
    task_list = [task.to_dict() for task in tasks]

    # retornar todas as atividades em formato JSON
    output = {
    "tasks": task_list,
    "total_tasks": len(task_list)
    }
    return jsonify(output)


# listar uma atividade específica método GET no endpoint "/tasks"
@app.route('/tasks/<int:id>', methods=['GET'])
# função chamada "get_task" para recuperar a atividade com base no identificador fornecido
def get_task(id):
    # loop "for" para percorrer a lista de atividades e verificar se o identificador corresponde
    for t in tasks:
        if t.id == id:
            # Se encontrarmos a atividade, a retornamos usando o jsonify
            return jsonify(t.to_dict())
    # Caso contrário, retornamos uma mensagem de erro com o código de resposta 404
    return jsonify({"message": "Não foi possível encontrar a atividade"}), 404

    # Salvamos essa requisição na nossa coleção para uso futuro

##### funcionalidade de leitura (UPDATE)

# criar uma rota para atualizar uma tarefa já cadastrada no sistema
# método PUT para realizar a atualização
@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    # Recebemos um identificador e dados em JSON no corpo da requisição, como título, descrição e se foi completada ou não
    task = None
    for t in tasks:
        if t.id == id:
            task = t
    print(task)
    # Caso a tarefa não seja encontrada, retornamos uma mensagem de erro
    if task == None:
        return jsonify({"message": "Não foi possível encontrar a atividade"}), 404

    # Caso contrário, atualizamos os dados da tarefa e retornamos uma mensagem de sucesso.
    data = request.get_json()
    task.title = data['title']
    task.description = data['description']
    task.completed = data['completed']
    print(task)
    return jsonify({"message": "Tarefa atualizada com sucesso!"})

##### funcionalidade de leitura (DELETE)

# recebe o identificador da tarefa que queremos deletar e remove a tarefa da lista de atividades cadastradas.
# Criamos uma nova rota com o método DELETE
@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = None
    # percorremos a lista de atividades para verificar se o identificador existe
    for t in tasks:
        print(t)
        if t.id == id:
            if t.id == id:
                task = t
                break
                # dica de performance, utilizando o comando BREAK para interromper o loop assim que encontrarmos o alvo, evitando percorrer toda a lista.

    # Caso contrário, retornamos uma mensagem informando que o recurso não foi encontrado.
    if not task:
        return jsonify({"message": "Não foi possível encontrar a atividade"}), 404
    
    # Se encontrarmos a atividade, removemos da lista. 
    tasks.remove(task)
    return jsonify({"message": "Tarefa deletada com sucesso!"})


# método run para executar o servidor localmente, com a opção debug ativada para visualizar informações de depuração
if __name__ == "__main__": # garante que só executando de forma manual subirá o servidor abaixo
    app.run(debug=True)

