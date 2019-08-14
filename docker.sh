docker pull mukul005/omdb-api-latest:API-Container
docker run --name Movie-CONTAINER -td mukul005/omdb-api-latest:API-Container
docker cp python-api-program.py Movie-CONTAINER:/tmp/python-api-program.py
docker exec -it Movie-CONTAINER bash 
