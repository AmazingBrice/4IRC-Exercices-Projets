FROM postgres:11.6-alpine

COPY InsertData.sql ./docker-entrypoint-initdb.d/InsertData.sql
COPY CreateScheme.sql ./docker-entrypoint-initdb.d/CreateScheme.sql

EXPOSE 5432
