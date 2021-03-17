docker build -t tp1-postgres .
docker run -p 5432:5432 --name tp1-postgres --network=mybridge -e POSTGRES_PASSWORD=pwd -d tp1-postgres