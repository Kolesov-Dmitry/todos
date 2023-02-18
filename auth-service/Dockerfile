FROM python:3.10.10-alpine3.17

WORKDIR /app
COPY . /app

RUN pip3 install bcrypt 
RUN pip3 install -r ./requirements.txt

ENTRYPOINT [ "python3", "/app/app.py" ]