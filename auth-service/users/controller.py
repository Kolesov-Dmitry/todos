from flask import Flask, request, Response

from .service import Service, InvalidPasswordError
from .repository import Repository, UserAlreadyExistsError, UserNotFoundError


def setup_users_controler(app: Flask, users_storage: Repository) -> None:
    user_service = Service(users_storage)

    @app.post("/api/v1/signup")
    def post_signup() -> Response:
        body = request.get_json()
        login = body['login']
        passwd = body['password']

        try:
            user_service.create_user(login, passwd)

            app.logger.info('user "%s" created successfully', login)
            return Response(status=200)

        except UserAlreadyExistsError as err:
            app.logger.error(err.message)
            return Response(status=409, response=err.message)

    @app.post("/api/v1/login")
    def post_login() -> Response:
        body = request.get_json()
        login = body['login']
        passwd = body['password']

        try:
            token = user_service.validate_user(login, passwd)

            app.logger.info('user "%s" logged in successfully', login)

            resp = Response(status=200)
            resp.set_cookie(key='accessToken', value=token)

            return resp

        except UserNotFoundError as err:
            app.logger.error(err.message)
            return Response(status=404, response=err.message)

        except InvalidPasswordError:
            app.logger.error('user "%s" failed to login', login)
            return Response(status=403)
