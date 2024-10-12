# classe chamada "Task" para representar as atividades
class Task:
    def __init__(self, id, title, description, completed=False) -> None:
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed

    # método "toDict" para retornar as informações em formato de dicionário
    def to_dict(self):
        return{
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed
        }