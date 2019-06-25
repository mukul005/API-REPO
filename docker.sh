docker pull mukul005/omdb-api:API-Container
docker run -td mukul005/omdb-api:API-Container
docker cp python-api-program.py API-Container:/var/tmp/python-api-program.py
docker exec -it API-Container bash 
