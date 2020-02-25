# ZXVenturesCodeChallenge
Solution to [Back-end Challenge](https://github.com/ZXVentures/code-challenge/blob/master/backend.md) from [ZXVentures](https://github.com/ZXVentures)

## Dependencies
- [Docker](https://www.docker.com/)

## Installation
```
sudo docker-compose build && sudo docker-compose up -d
```
Two containers will be initialized:
- ZXVenturesCodeChallengeBackend-python-mongo (MongoDB)
- ZXVenturesCodeChallengeBackend-python-app (REST API connected to the host port 5000)

#### Database
Import data based in this [json file](https://raw.githubusercontent.com/ZXVentures/ze-code-challenges/master/files/pdvs.json):
```
sudo docker exec -it ZXVenturesCodeChallengeBackend-python-app sh -c "python3 ./import.py"
```

### Tests
```
sudo docker exec -it ZXVenturesCodeChallengeBackend-python-app sh -c "python3 -m unittest -v tests.models.pdv_test tests.routes.pdv_test"
```

## REST API
```
POST    /pdv
GET     /pdv/:pdv_id
PUT     /pdv/:pdv_id
DELETE  /pdv/:pdv_id
GET     /pdv/covers?lng=:lng&lat=:lat
```
[Postman](https://www.getpostman.com/) collection with some examples: [download](https://raw.githubusercontent.com/enicioli/ZXVenturesCodeChallengeBackend-python/master/resources/ZXVenturesCodeChallengeBackend-python.postman_collection.json).

#### Main technologies
- [Docker](https://www.docker.com/)
- [Python3](https://www.python.org/)
- [MongoDB](https://www.mongodb.com/)
- [Flask](https://palletsprojects.com/p/flask/)
- [MongoFrames MongoDB ODM](http://mongoframes.com/)
- [JSON Schema](http://json-schema.org/)
