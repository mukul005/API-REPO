docker pull mukul005/omdb-api:API-Container
docker run --name Movie-CONTAINER -td mukul005/omdb-api:API-Container
docker cp python-api-program.py Movie-CONTAINER:/var/tmp/python-api-program.py
docker exec -it Movie-CONTAINER bash 
