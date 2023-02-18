from flask import Flask
import atexit

from users.controller import setup_users_controler
from db.users_storage import UsersStorage


app = Flask('AuthService')

user_storage = UsersStorage()
setup_users_controler(app, user_storage)

atexit.register(lambda: user_storage.close())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)