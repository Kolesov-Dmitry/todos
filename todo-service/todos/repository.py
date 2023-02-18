import abc
from typing import List
from uuid import UUID

from .todo import Todo

class NoConnectionError(Exception):
    """Exception raised if there is no connection with a storage."""


class CreateTodoError(Exception):
    """Exception raised if there is no connection with a storage."""

    def __init__(self, msg: set) -> None:
        self.message = msg


class Repository(metaclass=abc.ABCMeta):
    """Repository is an abstraction above an todos storage."""

    @abc.abstractmethod
    def get_todos_by_user_id(self, user_id: UUID) -> List[Todo]:
        pass

    @abc.abstractmethod
    def create_todo(self, todo: Todo) -> None:
        pass

    @abc.abstractmethod
    def complete_todo(self, todo_id: UUID) -> None:
        pass
