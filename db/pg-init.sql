CREATE USER test WITH LOGIN PASSWORD 'test';
CREATE DATABASE todosdb;

\c todosdb;

CREATE SCHEMA IF NOT EXISTS todos;

CREATE TABLE IF NOT EXISTS todos.users (
    id         UUID NOT NULL,
    user_name  TEXT NOT NULL,
    passwd     TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL,

    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS todos.todos (
    id         UUID NOT NULL,
    user_id    UUID NOT NULL,
    title      TEXT NOT NULL,
    completed  BOOLEAN NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL,

    PRIMARY KEY (id)
);

GRANT ALL PRIVILEGES ON DATABASE todosdb TO test;
GRANT USAGE ON SCHEMA todos TO test;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA todos TO test;
