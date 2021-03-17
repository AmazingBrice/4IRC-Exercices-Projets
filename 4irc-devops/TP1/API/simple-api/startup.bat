docker build -t tp1-api .
docker run -p 8080:8080 --name tp1-api --network=mybridge -d tp1-api