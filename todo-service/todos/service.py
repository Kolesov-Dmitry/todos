import uuid
from typing import List

from .todo import Todo
from .repository import Repository


class Service:

    def __init__(self, todos_storage: Repository) -> None:
        self.ts = todos_storage

    def fetch_todos(self, user_id: uuid.UUID) -> List[Todo]:
        return self.ts.get_todos_by_user_id(user_id)

    def create_todo(self, todo: Todo) -> Todo:
        todo.id = uuid.uuid4()
        self.ts.create_todo(todo)
        
        return todo

    def complete_todo(self, id: uuid.UUID) -> None:
        self.ts.complete_todo(id)
