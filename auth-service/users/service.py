import uuid
import bcrypt
import jwt

from .user import User
from .repository import Repository


class InvalidPasswordError(Exception):
    pass

class Service:

    def __init__(self, users_storage: Repository) -> None:
        self.us = users_storage

    def create_user(self, login: str, passwd: str) -> None:
        id = uuid.uuid4().hex
        hashed = bcrypt.hashpw(passwd, bcrypt.gensalt())

        self.us.create_user(User(
            id=id,
            login=login,
            passwd=hashed
        ))

    def validate_user(self, login: str, passwd: str) -> uuid.UUID:
        user = self.us.get_user(login)
        if not bcrypt.checkpw(passwd, user.passwd):
            raise InvalidPasswordError()

        token = jwt.encode({ 'id': user.id.hex, 'login': login }, "Secret.Key", algorithm="HS256")
        return token
