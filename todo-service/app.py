from flask import Flask
from psycopg2 import extras

from todos.controller import setup_todos_controler
from db.todos_storage import TodosStorage

extras.register_uuid()

app = Flask('TodoService')

storage = TodosStorage()
setup_todos_controler(app, storage)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
