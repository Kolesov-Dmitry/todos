from psycopg2 import connect, errors
from psycopg2.extras import DictCursor
from uuid import UUID
from typing import List

from todos.todo import Todo
from todos.repository import NoConnectionError, CreateTodoError


class TodosStorage():

    def __init__(self) -> None:
        self.conn = connect(
            dbname='todosdb',
            user='test',
            password='test',
            host='localhost',
            port=5432
        )
        self.conn.set_client_encoding('UNICODE')

    def create_todo(self, todo: Todo) -> None:
        insert = 'INSERT INTO todos.todos (id, user_id, title, completed, created_at) VALUES (%s, %s, %s, %s, %s)'
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(insert, (todo.id, todo.user_id,
                               todo.title, todo.completed, todo.created_at))

            self.conn.commit()

        except errors.ConnectionException or errors.ConnectionDoesNotExist or errors.ConnectionFailure:
            raise NoConnectionError()

        except errors.OperationalError as err:
            raise CreateTodoError(err.pgerror)

    def get_todos_by_user_id(self, user_id: UUID) -> List[Todo]:
        select = 'SELECT id, user_id, title, completed, created_at FROM todos.todos WHERE user_id=%s'

        try:
            with self.conn.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute(select, [user_id])

                todos = []
                for row in cursor:
                    print(row['title'])
                    todos.append(Todo(
                        id=row['id'],
                        user_id=row['user_id'],
                        title=row['title'],
                        completed=row['completed'],
                        created_at=row['created_at']
                    ))

                return todos

        except errors.ConnectionException or errors.ConnectionDoesNotExist or errors.ConnectionFailure:
            raise NoConnectionError()

        except errors.OperationalError as err:
            raise CreateTodoError(err.pgerror)

    def complete_todo(self, todo_id: UUID) -> None:
        update = 'UPDATE todos.todos SET completed=true WHERE id=%s'
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(update, [todo_id])

            self.conn.commit()

        except errors.ConnectionException or errors.ConnectionDoesNotExist or errors.ConnectionFailure:
            raise NoConnectionError()

        except errors.OperationalError as err:
            raise CreateTodoError(err.pgerror)
