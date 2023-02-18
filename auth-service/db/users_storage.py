from users.user import User
from users.repository import UserAlreadyExistsError, UserNotFoundError


class UsersStorage():
    """Repository is an abstraction above an user storage."""

    def __init__(self) -> None:
        self.users: dict[str, User] = {}

    def get_user(self, login: str) -> User:
        if login not in self.users:
            raise UserNotFoundError(f'user "{ login }" not found')

        return self.users[login]

    def create_user(self, user: User) -> None:
        if user.login in self.users:
            raise UserAlreadyExistsError(
                f'user with "{ user.login }" already exists')

        self.users[user.login] = user

    def close(self) -> None:
        pass