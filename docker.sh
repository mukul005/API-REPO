docker pull mukul005/omdb-api:API-Container
docker run --name OMDB-API-CONTAINER -td mukul005/omdb-api:API-Container
docker cp python-api-program.py OMDB-API-CONTAINER:/var/tmp/python-api-program.py
docker exec -it OMDB-API-CONTAINER bash 
