import abc
from .user import User


class UserAlreadyExistsError(Exception):
    """Exception raised if user with given name already exists in a repository."""

    def __init__(self, msg: str) -> None:
        self.message = msg


class UserNotFoundError(Exception):
    """Exception raised if user does not exist in a repository."""

    def __init__(self, msg: str) -> None:
        self.message = msg


class Repository(metaclass=abc.ABCMeta):
    """Repository is an abstraction above an user storage."""

    @abc.abstractmethod
    def get_user(self, login: str) -> User:
        pass

    @abc.abstractmethod
    def create_user(self, user: User) -> None:
        pass
