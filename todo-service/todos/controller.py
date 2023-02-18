from flask import Flask, request, Response
import uuid
import json

from .service import Service
from .repository import Repository
from .todo import Todo
from jsontools.todos_encoder import Encoder


def setup_todos_controler(app: Flask, todos_storage: Repository) -> None:
    todo_service = Service(todos_storage)

    @app.post("/api/v1/todo")
    def post_todo() -> Response:
        body = request.get_json()
        todo = Todo(**body)

        try:
            app.logger.info('create todo')
            todo_service.create_todo(todo)

            app.logger.info('todo created successfully')
            return Response(status=200)

        except Exception as err:
            app.logger.info(err)
            return Response(status=500)

    @app.patch("/api/v1/todo/complete/<todo_id>")
    def patch_todo_complete(todo_id) -> Response:
        id = uuid.UUID(todo_id)

        try:
            app.logger.info(f'complete todo with id: { todo_id }')
            todo_service.complete_todo(id)

            return Response(status=200)

        except Exception as err:
            app.logger.info(err)
            return Response(status=500)

    @app.get("/api/v1/todo/<user_id>")
    def get_todo(user_id) -> Response:
        id = uuid.UUID(user_id)

        try:
            app.logger.info('read todos')
            todos = todo_service.fetch_todos(id)

            todos_json = json.dumps(todos, cls=Encoder, ensure_ascii=False)

            return Response(status=200, response=todos_json)

        except Exception as err:
            app.logger.info(err)
            return Response(status=500)
