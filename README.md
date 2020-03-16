# python-redis-test

## Generating Pipfile.lock

1. `pipenv lock`

## docker-compose.yml

* Brings up Redis instance
* Brings up python container
* Runs `redis_test.py`

## docker-compose-dev.yml

* Brings up Redis instance
* Brings up python container
* Stays running for development